"""
Я использую кастомный менеджер юзера для переопределения метода создания юзера,
т.к. вся проверка будет проводиться с помощью телеги.
"""

from django.contrib.auth.base_user import BaseUserManager
import secrets

class CustomUserManager(BaseUserManager):
    """
    Поскольку нужен буквально только ТГ, я делаю это поле обязательным и единственным необходимым.
    Проверка пароля фиктивно существует, т.к. джанго выдавал ошибки при дальнейших действиях с юзером.
    """

    def generate_unique_token(self): # функа для создания уникального персонального токена
        while True:
            token = secrets.token_urlsafe(20)
            if not self.model.objects.filter(token=token).exists():
                return token

    def create_user(self, tg, password=None, **extra_fields):
        if not tg:
            raise ValueError('Поле tg обязательно')

        token = self.generate_unique_token()
        user = self.model(tg=tg,token=token, **extra_fields)

        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()

        user.save(using=self._db)
        return user

    def create_superuser(self, tg, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if not password:
            raise ValueError('СУПЕРПОЛЬЗОВАТЕЛЬ ДОЛЖЕН ИМЕТЬ ПАРОЛЬ')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('суперюзер значит СУПЕР юзер, лол, это стафф.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Суперюзер это суперюзер...')

        user = self.create_user(tg, password, **extra_fields)

        return user
