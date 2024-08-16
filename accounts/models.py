from django.conf import settings
from django.db import models


class Profile(models.Model):
    """ Создаем модель профиля пользователя """

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    address = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    def __str__(self):
        return f'Профиль: {self.user.email}'
