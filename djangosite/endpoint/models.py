from django.db import models
from jsonfield import JSONField
from taggit.managers import TaggableManager
from slugify import slugify
#import editarea

class JsonEndpoint(models.Model):
    name = models.CharField(max_length=255, unique=True)
    blob = JSONField()
    #blob = editarea.EditAreaField()
    slug = models.SlugField(max_length=255, unique=True)

    tags = TaggableManager(blank=True)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(JsonEndpoint, self).save(*args, **kwargs)

    def url(self):
        return "/%s/" % self.slug


class AuthEndpoint(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    enabled = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(AuthEndpoint, self).save(*args, **kwargs)

    def url(self):
        return "/%s/" % self.slug

