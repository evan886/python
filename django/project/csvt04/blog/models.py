from django.db import models
class Entry(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

class Blog(models.Model):
    name = models.CharField(max_length=30)
    entry = models.ForeignKey(Entry)

    def __unicode__(self):
        return self.name
# Create your models here.
