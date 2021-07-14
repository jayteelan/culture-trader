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
    parent1 = models.ForeignKey(
        'self', related_name='first_parent_strain', on_delete=models.CASCADE)
    parent2 = models.ForeignKey(
        'self', related_name='second_parent_strain', on_delete=models.CASCADE)
    tags = TaggableManager()
    notes = models.TextField

    def __str__(self):
        return self.genus + self.species + self.name


class Project(models.Model):
    created_at = models.DateTimeField('date created')
    name = models.CharField(max_length=200)
    root1 = models.ForeignKey(
        Strain, related_name='first_root_strain', on_delete=models.CASCADE)
    root2 = models.ForeignKey(
        Strain, related_name='second_root_strain', on_delete=models.CASCADE)
    # generations = models.ForeignKey(Generation, on_delete=CASCADE)

    def __str__(self):
        return self.name


class Generation(models.Model):
