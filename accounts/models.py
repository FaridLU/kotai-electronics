from django.contrib.auth.models import AbstractUser, BaseUserManager, UserManager as AuthUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password=None):
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    email_confirmed = models.BooleanField(
        _('email confirmed'),
        help_text=_('Designates whether the email is confirmed.'),
        default=False,
    )

    database_permission = models.BooleanField(
        _('database permission'),
        help_text=_('Designates whether the user has database permission or not.'),
        default=False,
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name',]
