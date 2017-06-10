from rest_framework import serializers
from trips.models import Trip

class TripSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trip
        fields = ('id', 'title', 'users')
