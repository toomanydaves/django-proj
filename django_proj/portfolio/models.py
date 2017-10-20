from django.db import models
from django.utils.translation import gettext_lazy as _

class Project(models.Model):
    url = models.URLField(unique=True)
    name = models.CharField(
        max_length=200,
    )
    description = models.TextField(
        blank=True,
    )
    UPCOMING = 'UPCOMING'
    ACTIVE = 'ACTIVE'
    ARCHIVED = 'ARCHIVED'
    status = models.CharField(
        choices=(
            (UPCOMING, _('upcoming')), 
            (ACTIVE, _('active')),
            (ARCHIVED, _('archived')),
        ),
        default=UPCOMING,
        max_length=20,
    )
    INTERNAL = 'INTERNAL'
    EXTERNAL = 'EXTERNAL'
    origin = models.CharField(
        choices=(
            (INTERNAL, _('internal')),
            (EXTERNAL, _('external')),
        ),
        default=INTERNAL,
        max_length=20,
    )
    logo = models.FileField(
        blank=True,
        upload_to='project_logos'
    )

    def __str__(self):
        return self.name
