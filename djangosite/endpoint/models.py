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


class MockObjectClass(models.Model):
    class Meta:
        verbose_name_plural = "mock object classes"

    class_name = models.CharField(max_length=255, unique=True)

    def __unicode__(self):
        return self.class_name


class MockObject(models.Model):
    object_id = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255, unique=True)
    mock_class = models.ForeignKey(MockObjectClass)
    blob = JSONField()

    def __unicode__(self):
        return "%s/%s (%s)" % (self.mock_class.class_name, self.object_id, self.description)

