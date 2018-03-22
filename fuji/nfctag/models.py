from django.db import models

class NFCTag(models.Model):
    '''NFCタグを表すクラス'''
    # 所有主のID
    user_id = models.IntegerField(blank=False, unique=True)
    # nfcの固有IDをハッシュ化したもの
    IDm = models.CharField(max_length=32, blank=False)

