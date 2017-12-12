from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from toomanydaves_auth.models import User

class Tag(models.Model):
    name=models.CharField(
        max_length=200,
        unique=True
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class Post(models.Model):
    content = models.TextField(
        blank=True,
    )

    DELETED = 'DELETED'
    DRAFT = 'DRAFT'
    PUBLISHED = 'PUBLISHED'
    status = models.CharField(
        choices=(
            (DELETED, _('deleted')), 
            (DRAFT, _('draft')),
            (PUBLISHED, _('published')),
        ),
        default=DRAFT,
        max_length=20
    )
    
    written_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(editable=False)
    published_at = models.DateTimeField(
        blank=True,
        null=True,
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True
    )
    cover_photo = models.FileField(
        blank=True,
        upload_to='post_cover-photo'
    )

    # def publish()
    # def unpublish()
    # def delete()
    # https://stackoverflow.com/questions/1737017
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        return super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.written_by.first_name + ' | ' + str(self.created_at)

    class Meta:
        ordering = ('created_at',)
