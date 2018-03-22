from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth import authenticate
from django.contrib.auth import login as login_

from account.models import User


def register(request):
    # とりあえずGETで取得
    # TODO: RESTっぽくしたい
    email = request.GET.get('email')
    name = request.GET.get('name')
    password = request.GET.get('password')

    print(email, name, password)

    # ユーザの生成
    user = User.objects.create_user(email, name, password)

    return HttpResponse("Done !")

def login(request):
    # とりあえずGETで取得
    # TODO: RESTっぽくしたい

    email = request.GET.get('email')
    password = request.GET.get('password')

    print(email, password)

    # ユーザの認証
    user = authenticate(
        email=email,
        password=password
    )

    if user is not None:
        # ログインに成功した場合
        login_(request, user)
        print('Succeeded !')
        return HttpResponse("Succeeded !")

    else:
        # ログインに失敗した場合
        print('Failed !')
        return HttpResponse("Failed !")
