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
            return JsonResponse(OK)

    except:
        pass

    # 失敗用レスポンスの返却
    return JsonResponse(NG)


