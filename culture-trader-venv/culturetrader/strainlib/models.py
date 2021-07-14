import datetime
from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager


class Strain(models.Model):
    created_at = models.DateTimeField('date created')
    genus = models.CharField(max_length=200)
    species = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    stable = models.BooleanField
    public = models.BooleanField
    parent1 = models.ForeignKey('self', on_delete=models.CASCADE)
    parent2 = models.ForeignKey('self', on_delete=models.CASCADE)
    tags = TaggableManager()
    notes = models.TextField

    def __str__(self):
        return self.genus + self.species + self.name
