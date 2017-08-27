from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# It's highly recommended to set up a custom user model, even if the default User model seems sufficient.
# Make sure to point AUTH_USER_MODEL to it and register the model in the app's admin.py.
# (from https://docs.djangoproject.com/en/1.11/topics/auth/customizing/#auth-custom-user)

class User(AbstractBaseUser):
    pass
