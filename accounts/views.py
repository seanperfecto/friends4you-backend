from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
import pdb
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.password_validation import validate_password
from accounts.serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

class SignUp(APIView):
    @csrf_exempt
    def post(self, request, format='json'):
        username = request.data["username"]
        email = request.data["email"]
        password = request.data["password"]
        user = User(username=username, email=email, password=password)
        try:
            user.full_clean()
        except ValidationError as e:
            return JsonResponse(e.message_dict)
        try:
            validate_password(password, user)
        except ValidationError as e:
            return JsonResponse({'errors': e.messages})
        user.set_password(user.password)
        user.save()
        login(request, user)
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data, safe=False)

    def get(self, request, format='json'):
        return JsonResponse({'yoo': 'hey'})


class Session(APIView):

    def post(self, request, format='json'):
        username = request.data["username"]
        password = request.data["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            serializer = UserSerializer(user)
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse({'errors': ["Invalid login credentials"]})


    def delete(self, request, format='json'):
        logout(request)
        return JsonResponse({'errors': 'none'})

    def get(self, request, format='json'):
        return JsonResponse({'yoo': 'hi'})
