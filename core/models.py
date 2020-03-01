from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):

    def create_user(self, username, password):
        if not username:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=self.normalize_email(username),
            rol__id='freemium'
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        if not username:
            raise ValueError('Users must have an email address')
        rol = Rol.objects.get(name='admin')
        user = self.model(
            username=self.normalize_email(username),
            rol=rol
        )
        user.set_password(password)
        user.save()
        return user

class Rol(models.Model):
    name = models.CharField(max_length=32, null=False, primary_key=True)
    description = models.CharField(max_length=64, null=False)

class User(AbstractUser):
    username = models.EmailField(max_length=32, unique=True)
    is_active = models.BooleanField(null=False, default=True)
    rol = models.ForeignKey(to=Rol, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'username'

    objects = UserManager()

