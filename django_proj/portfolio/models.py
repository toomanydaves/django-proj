from django.db import models
from django.utils.translation import gettext_lazy as _

class Project(models.Model):
    url = Models.UrlField(unique=True)
    name = Models.CharField()
    description = Models.TextField()
    UPCOMING = 'UPCOMING'
    ACTIVE = 'ACTIVE'
    ARCHIVED = 'ARCHIVED'
    status = Models.CharField(
        choices=(
            (UPCOMING, _('upcoming')), 
            (ACTIVE, _('active')),
            (ARCHIVED, _('archived')),
        ),
        default=UPCOMING,
    )
    INTERNAL = 'INTERNAL'
    EXTERNAL = 'EXTERNAL'
    origin = Models.CharField(
        choices=(
            (INTERNAL, _('internal')),
            (EXTERNAL, _('external')),
        ),
        default=INITIATIVE,
    )
