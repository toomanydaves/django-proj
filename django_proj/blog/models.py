from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from network.models import Peep
from portfolio.models import Project

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
    content = models.TextField(
        blank=True,
    )
    title = models.CharField(
        blank=True,
        max_length=200,
    )
    created_at = models.DateTimeField(editable=False)
    written_by = models.ForeignKey(
        Peep,
        on_delete=models.CASCADE,
    )
    associated_with = models.ForeignKey(
        Project,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    published_at = models.DateTimeField(
        blank=True,
        null=True,
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True,
    )
    cover_photo = models.FileField(
        blank=True,
        upload_to='post_cover-photo'
    )

    # TODO API
    # def publish()
    # def unpublish()
    # def delete()

    # https://stackoverflow.com/questions/1737017
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        return super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.written_by.first_name + ' | ' + (self.title if self.title else str(self.created_at))

    class Meta:
        ordering = ('created_at',)

class SEO(models.Model):
    key_word = models.CharField(max_length=50)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.key_word

    class Meta:
        ordering = ('post', 'key_word',)
