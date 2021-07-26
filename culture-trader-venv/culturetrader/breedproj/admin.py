from django.contrib import admin

from .models import Project, Generation

admin.site.register([Project, Generation])
