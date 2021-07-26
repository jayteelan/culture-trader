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

    def __str__(self):
        return self.name


class Generation(models.Model):
    created_at = models.DateTimeField('date created', auto_now_add=True)
    project = models.ForeignKey(
        Project, related_name="generations", on_delete=models.CASCADE)
    children = models.ManyToManyField(Strain, blank=True)

    # def increment_f_number():
    #     "Returns the F-number of the generation"
    #     test = Project.objects.all().count()
    #     return test
    # return 5

    # f_number = models.IntegerField(default=1, editable=True)
    # project_generations = Generation.objects.filter(
    #     project_id=self.project.id)
    # return project_generations.length+1

#     def children(self):
#         "Returns all children in the current generation"
#         project_all = Strain.objects.filter(
#             self.project_id in Strain.in_projects)
#         return project_all.filter

#     # return generations.length+1
#     # f_number = models.IntegerField(default=get_f)
#     # def get_children:
#     # get all generations by project_id
#     # get previous generation (f_number===generations.length)
#     # # return all strains with same project_id and f_number

#     def __str__(self):
#         return "{} gen{}".format(self.project_id, self.f_number)
