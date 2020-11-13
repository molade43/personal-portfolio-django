from django.contrib import admin
from .models import Project
# Register your models here.

# this code automatically creates a Project DB in the admin on the browser
admin.site.register(Project)
