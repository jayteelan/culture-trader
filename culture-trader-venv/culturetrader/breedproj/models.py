from django.db.models.signals import post_save, post_delete
from django.db.models import F
from django.dispatch import receiver
import datetime
from django.db import models
from django.utils import timezone
from strainlib.models import Strain


class Project(models.Model):
    created_at = models.DateTimeField('date created', auto_now_add=True)
    name = models.CharField(max_length=200, default="New breeding project")
    root1 = models.ForeignKey(
        Strain,
        related_name='first_root_strain',
        on_delete=models.CASCADE
    )
    root2 = models.ForeignKey(
        Strain,
        related_name='second_root_strain',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    latest_generation = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Generation(models.Model):
    created_at = models.DateTimeField('date created', auto_now_add=True)
    project = models.ForeignKey(
        Project,
        related_name="generations",
        on_delete=models.CASCADE
    )
    children = models.ManyToManyField(Strain, blank=True)
    f_number = models.IntegerField(
        default=1, editable=False)

    def __str__(self):
        return "project{} gen{}".format(self.project_id, self.f_number)

# Signals, with help from dani herrera [https://stackoverflow.com/questions/68424408/getting-all-records-with-same-foreign-key-in-django]


@receiver(post_save, sender=Generation)
def add_project(sender, instance, created, **kwargs):
    if not created:
        return
    current_proj = instance.project
    current_proj.latest_generation = F('latest_generation') + 1
    current_proj.save()
    current_proj.refresh_from_db()


@receiver(post_save, sender=Generation)
def add_gen(sender, instance, created, **kwargs):
    if not created:
        return
    current_gen = instance.project.latest_generation
    instance.f_number = current_gen
    instance.save()
    instance.refresh_from_db()


@receiver(post_delete, sender=Generation)
def rm_project(sender, instance, **kwargs):
    current_proj = instance.project
    current_proj.latest_generation = F('latest_generation') - 1
    current_proj.save()
    current_proj.refresh_from_db()


@receiver(post_delete, sender=Generation)
def rm_gen(sender, instance, **kwargs):
    current_gen = instance.project.latest_generation
    instance.f_number = current_gen
    instance.save()
    instance.refresh_from_db()
