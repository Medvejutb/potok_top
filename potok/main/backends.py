from django.contrib.auth.backends import ModelBackend
from .models import User

class TGAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, tg=None, token=None, **kwargs):
        """
        Переопределяю функцию аутентификации, так как для проверки нужны только телега и персональный токен юзера
        для привязки самого ТГ

        Поддерживает и авторизацию через админку (username+password),
        и кастомную через tg+token.
        """
        # Авторизация через админку (username = tg, password)
        if username and password:
            try:
                user = User.objects.get(tg=username)
                if user.check_password(password):
                    return user
            except User.DoesNotExist:
                return None

        # Авторизация через бота/токен
        if tg and token:
            try:
                user = User.objects.get(tg=tg, token=token, is_verified=True)
                return user
            except User.DoesNotExist:
                return None

        return None
