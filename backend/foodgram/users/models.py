from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator
from django.db import models

from .validators import validate_username


class User(AbstractUser):
    email = models.EmailField(
        max_length=254,
        blank=False,
        unique=True,
        validators=[EmailValidator]
    )
    username = models.CharField(
        max_length=150,
        unique=True,
        validators=[validate_username]
    )
    first_name = models.CharField(
        max_length=150,
    )
    last_name = models.CharField(
        max_length=150,
    )
    password = models.CharField(max_length=150)


class Subscriptions(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following'
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        constraints = [models.UniqueConstraint(
            fields=['user', 'author'],
            name='unique_subscription'
        ),
            models.CheckConstraint(
            check=~models.Q(author=models.F('user')),
            name='user_not_author'
        )
        ]
