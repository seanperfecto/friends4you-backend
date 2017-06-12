# In consumers.py
import pdb
from channels import Channel, Group
from realtime.models import Connection
from channels.sessions import channel_session
from channels.auth import channel_session_user, channel_session_user_from_http
import json

# Connected to websocket.connect
@channel_session_user_from_http
def ws_add(message):
    # Accept the connection
    #TODO ADD USER AUTHENTIXATION HERE
    # if request.user.is_authenticated:
    message.reply_channel.send({"accept": True})
    #get all chatrooms
    connections = Connection.objects.all()
    #see if there are any chatrooms that are open (only 1 user)
    for connection in connections:
        if connection.users.count() == 1:
            connection.users.add(message.user.pk)
            Group(str(connection.pk)).add(message.reply_channel)
            message.reply_channel.send(json.dumps({'disconnected': 'true'}))
            return

    #if no open chats
    connection = Connection()
    connection.save()
    connection.users.add(message.user.pk)
    Group(str(connection.pk)).add(message.reply_channel)

# Connected to websocket.receive
@channel_session_user
def ws_message(message):
    #LOOK INTO LOOKIN UP USER BY REPLY CHANNEL HERE, otherwise find group by user id
    user = message.user
    #find channel that you're logged in on
    connection = user.connection_set.first()
    data = json.loads(message['text'])
    data['username'] = message.user.username
    Group(str(connection.pk)).send({
        "text": json.dumps(data)
    })

# Connected to websocket.disconnect
@channel_session_user
def ws_disconnect(message):
    connection_id = message.user.connection_set.first().pk
    connection = Connection.objects.get(pk=connection_id)
    #TODO : handle logged in user in two separate browsers issue with deleting from connection
    #when still in group
    connection.users.remove(message.user)
    Group(str(connection.pk)).discard(message.reply_channel)
    if connection.users.count() == 0:
        connection.delete()
    else:
        Group(str(connection.pk)).send({"text": json.dumps({'disconnected': 'true'})})
