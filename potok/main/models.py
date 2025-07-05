from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

class User(AbstractUser):
    username = None
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=20, blank=True)
    tg = models.CharField(max_length=30, unique=True)
    token = models.CharField(
        max_length=20,
        unique=True,
        blank=True,
        null=True
    )
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'tg'
    REQUIRED_FIELDS = []

    rank_choices = [
        ('A', 'Смешарик'),
        ('B', 'Малышарик'),
        ('C', 'Биомасса')
    ]
    rank = models.CharField(
        max_length=1,
        choices=rank_choices,
        default='C'
    )
    points = models.IntegerField(default=0)
    hookah_smoked = models.IntegerField(default=0)
    money_spent = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    objects = CustomUserManager()

    def __str__(self):
        return (f'Пользователь {self.first_name} {self.last_name or "Фамилия"} - {self.tg},\n'
                f'Ранг - {self.rank}, очки - {self.points},\n'
                f'Скурено кальянов - {self.hookah_smoked},\n'
                f'Потрачено бабла - {self.money_spent}\n')
