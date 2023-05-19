from django.db import models
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.
class User(AbstractBaseUser):
    name = models.CharField(max_length=30, blank=True, null=True)
    user_id = models.CharField(max_length=30, blank=True, null=True)
    thumbnail = models.CharField(max_length=256, default='default_profile.png', blank=True, null=True)

    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = ['user_id']

    def __str__(self):
        return self.user_id

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        db_table = 'users'
