from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from account.models import User
from nfctag.models import NFCTag

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


@login_required
@csrf_exempt
def register(requests):
    '''NFCを登録する(ログイン必要)'''
    try:
        # リクエストの取得
        data = json.loads(requests.body)

        # 入力値が足りているかのチェック
        if 'IDm' in data and requests.user:
            # もし入力値が足りていた場合

            # NFCタグの生成
            nfc_tag = NFCTag(
                user_id=int(requests.user.id),
                IDm=data['IDm']
            )

            # DBへ保存
            nfc_tag.save()

            # 成功用レスポンスの返却
            return JsonResponse(OK)

    except:
        pass

    # 失敗用レスポンスの返却
    return JsonResponse(NG)


@csrf_exempt
def check(requests):
    '''NFCタグが正しいか確認する'''
    try:
        # リクエストの取得
        data = json.loads(requests.body)

        # 入力値が足りているかのチェック
        if 'IDm' in data:
            # もし入力値が足りていた場合

            # NFCタグの検索
            nfc_tag = NFCTag.objects.filter(
                IDm__contains=data['IDm']
            )

            if len(nfc_tag) == 0:
                # 見つからなかった場合
                result = {
                    'state' : 'not found'
                }
            else:
                # 見つかった場合
                # ユーザを探す
                user = User.objects.filter(
                    id__contains=nfc_tag[0].user_id
                )

                result = {
                    'state' : 'hit',
                    'name'  : user[0].name
                }
            
            # 成功用レスポンスの返却
            return JsonResponse(result)

    except:
        pass

    # 失敗用レスポンスの返却
    return JsonResponse(NG)
