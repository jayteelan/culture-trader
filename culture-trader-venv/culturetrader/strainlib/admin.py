from django.contrib import admin

from .models import Strain, Project, Generation

admin.site.register([Strain, Project, Generation])
