from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator

from django.utils.translation import gettext as _


class UserManager(UserManager):
    '''部員を管理するクラス'''
    def create_user(self, email, name, password, **extra_fields):
        '''ユーザを作成'''
        # 値の入力をチェック 
        if not email or not name or not password:
            raise ValueError('The given arugments are not enough.')

        # メールアドレスのバリデーションチェック
        email = self.normalize_email(email)

        # ユーザの生成
        user = self.model(name=name, email=email, **extra_fields)

        # パスワードを設定
        user.set_password(password)

        # ユーザを保存
        user.save(using=self._db)

        # ユーザの返却 
        return user


class User(AbstractBaseUser, PermissionsMixin):
    '''部員を表すクラス'''

    # メールアドレス
    email = models.EmailField(
        _('email'),
        blank=False,
        unique=True
    )

    # 名前
    name = models.CharField(
        _('name'),
        max_length=150,
        blank=False,
        unique=False,
        validators=[UnicodeUsernameValidator()],
    )

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        # DB名
        db_table = 'account_user'
