import pdb

from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from network.models import Peep

"""
    It's highly recommended to set up a custom User and UserManager model,
    even if the default models seem sufficient.
    Make sure to point AUTH_USER_MODEL to the User model
    and to register the model in the app's admin.py.

    (from https://docs.djangoproject.com/en/1.11/topics/auth/customizing/#auth-custom-user)
"""

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, username, password, **extra_fields):
        if not email:
            raise ValueError('A user must have an email address.')

        email = self.normalize_email(email).lower()

        """
        This shouldn't be an error
        The user should be able to merge accounts
        TODO: merge user attributes
        
        """

        if User.objects.filter(email = email).exists():
            # TEMP don't merge just return user
            # raise ValueError('A user must have a unique email address.')
            return User.objects.filter(email=email).first()
            


        if not username:
            raise ValueError('A user must have a username')

        user = self.model(
            username=self.model.normalize_username(username),
            email=email,
            **extra_fields
        )

        user.set_password(password)

        # Save and catch IntegrityError (due to email being unique)
        try:
            user.save(using=self._db)

        except IntegrityError:
            raise ValueError('This email has already been registered.')

        return user

    def create_user(self, email, username, password=None, **extra_fields):
        pdb.set_trace()

        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, username, password, **extra_fields)
        

    def create_superuser(self, email, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, username, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):

    username_validator = UnicodeUsernameValidator()

    first_name = models.CharField(_('first name'), max_length=100)
    last_name = models.CharField(_('last name'), max_length=150)
    peep = models.OneToOneField(
        Peep,
        on_delete=models.CASCADE,
        unique=True,
    )
    email = models.EmailField(
        _('email address'),
        unique=True,
        help_text=_('Required. Must be a unique & valid email address.'),
        error_messages={
            'unique':_('This email has already been registered.')
        }
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
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether this user can log into the admin site.'),
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
    REQUIRED_FIELDS = ['username', ]

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

    def __str__(self):
        return self.get_full_name()
