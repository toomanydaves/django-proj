from django.conf import settings
from django.db import models

class Peep(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=150)
    profile_picture = models.FileField(
        blank=True,
        upload_to='profile_pictures'
    )

    def get_name(self):
        return self.get_full_name()
        
    def get_full_name(self):
        """
        Return the first_name plus the last_name with a space in between
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def __str__(self):
        return self.get_name()
