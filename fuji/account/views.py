from django.contrib.auth import authenticate
from django.contrib.auth import login as login_
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse

from account.models import User

import json


# レスポンスとして送信するJson
# 成功
OK = {
    'state' : 'OK'
}

# 失敗
NG = {    
    'state' : 'NG'
}


@csrf_exempt
def register(request):
    '''ユーザを作成する'''
    try:
        # リクエストの取得
        data = json.loads(request.body)

        # 入力値が足りているかのチェック
        if 'email' in data \
            and 'name' in data \
            and 'password' in data:
            # もし入力値が足りていた場合

            # ユーザの生成
            user = User.objects.create_user(
                email=data['email'],
                name=data['name'],
                password=data['password']
            )

            # 成功用レスポンスの返却
            return JsonResponse(OK)
    except:
        pass
            
        # 失敗用レスポンスの返却
    return JsonResponse(NG)


@csrf_exempt
def login(request):
    '''ユーザを認証し、cookieを返す'''
    # リクエストの取得
    try:
        data = json.loads(request.body)

        # 入力値が足りているかのチェック
        if 'email' in data and 'password' in data:
            # もし入力値が足りていた場合

            # ユーザの認証
            user = authenticate(
                email=data['email'],
                password=data['password']
            )
            # 認証できたかチェック
            if user is not None:
                # 認証に成功した場合はログイン
                login_(request, user)
                
                # 成功用レスポンスの返却
                return JsonResponse(OK)

    except:
        pass

    # 失敗用レスポンスの返却
    return JsonResponse(NG)
