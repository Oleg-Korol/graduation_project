# from datetime import datetime, timedelta
#
# import jwt
# from django.conf import settings
# from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
# from django.contrib.auth.models import PermissionsMixin, UserManager
# from django.db import models
#
# class UserManager(BaseUserManager):
#     """"django требует, чтобы кастомные пользователи определяли свой
#     собственный класс менеджера.Унаследовавшись от класса BaseUserManager.
#     Мы переопределяем его под создание своего пользователя"""
#
#     def create_user(self,username,email,password = None):
#         """"Создает и возвращает пользователя"""
#
#         if not username:
#             raise TypeError("Users must have username")
#
#         if not email:
#             raise TypeError("Users must have email address")
#
#         user = self.model(username = username,
#                           email = self.normalize_email(email),
#                           )
#
#         user.set_password(password)
#         user.save()
#
#         return user
#
#     def create_superuser(self,username,email,password):
#         """"Создает и возвращает пользователя с привелегиями суперпользователя
#         """
#
#         if not password:
#             raise TypeError("Superusers must have a password")
#
#         user = self.create_user(username =username,
#                                 email=email,
#                                 password=password)
#         user.is_superuser = True
#         user.is_staff = True
#         user.save()
#
#         return user
#
#
# class User(AbstractBaseUser,PermissionsMixin):
#
#         USERNAME_FIELD = 'email'
#         REQUIRED_FIELDS = ['username']
#
#         username = models.CharField(db_index=True,max_length=255,unique=True)
#         email =models.EmailField(db_index=True,
#                                  unique=True)
#         is_active = models.BooleanField(default=True)
#
#         is_staff = models.BooleanField(default=False)
#
#         create_at = models.DateTimeField(auto_now_add=True)
#
#         update_at = models.DateTimeField(auto_now=True)
#
#
#
#         object = UserManager()
#
#         def __str__(self):
#             return f'{self.username}-{self.email}'
#
#         def _generate_jwt_token(self):
#             dt = datetime.now() + timedelta(days = 1)
#
#             payload = {
#                 'id':self.pk,
#                 'exp': int(dt.strftime('%s'))
#             }
#             return jwt.encode(payload,settings.SECRET_KEY, algorithm = 'HS256')
#
#
#
#
#         @property
#         def token(self):
#             return self._generate_jwt_token()
#
#         def get_full_name(self):
#             return self.username
#

from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='profile')
    description = models.TextField(blank=True, null=True)

    create_at = models.DateTimeField(auto_now_add=True)

    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username}{self.user.email}'
