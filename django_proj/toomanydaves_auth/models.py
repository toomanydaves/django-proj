from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, first_name, last_name, password, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')
        if not email:
            raise ValueError('The given email must be set')
        if not first_name:
            raise ValueError('The given first name must be set')
        if not last_name:
            raise ValueError('The given last name must be set')

        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.sefdefault('is_superuser', False)
        return self._create_user(username, email, first_name, last_name, password, **extra_fields)
        

    def create_superuser(self, username, email, first_name, last_name, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, first_name, last_name, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    """
    It's highly recommended to set up a custom user model, even if the default User model seems sufficient.
    Make sure to point AUTH_USER_MODEL to it and register the model in the app's admin.py.
    (from https://docs.djangoproject.com/en/1.11/topics/auth/customizing/#auth-custom-user)

    In this case, we want to require a user's email address except during third party sign-on.
    """

    username_validator = UnicodeUsernameValidator()

    email = models.EmailField(
        _('email address'),
        unique=True,
        help_text=_('Required. Must be a valid email address.'),
    )
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=150)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', ]

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)
