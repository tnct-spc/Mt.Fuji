from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth import authenticate

from django.contrib.auth import get_user_model


#from django.contrib.auth.models import User
from account.models import User

def register(request):
    email = request.GET.get('email')
    name = request.GET.get('name')
    password = request.GET.get('password')

    print(email, name, password)

    user = User.objects.create_user(email, name, password)

    print(user)

    return HttpResponse("Hello, World")

