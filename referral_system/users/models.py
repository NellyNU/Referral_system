from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import random
import string

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, phone_number):
        if not phone_number:
            raise ValueError('Номер телефона обязателен!')
        invite_code = self.generate_invite_code()

        user = self.model(
            phone_number = phone_number,
            invite_code = invite_code
        )
        user.save(using=self._db)
        return user

    def generate_invite_code(self,length=6):
        while True:
            code = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
            if not User.objects.filter(invite_code=code).exists():
                return code


class User(AbstractBaseUser):
    phone_number = models.CharField(max_length=15,unique=True)
    invite_code = models.CharField(max_length=6,unique= True)
    activated_invite_code = models.CharField(max_length=6, null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'

    def get_invited_users(self):
        return User.objects.filter(invite_code=self.invite_code)

class AuthCode(models.Model):
    phone_number = models.CharField(max_length=15)
    code = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('phone_number', 'code')