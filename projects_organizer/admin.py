from django.contrib import admin

# Register your models here.
from .models import Project # imports the model "Topic" from model.py which is located in the        # current directory and specified with "."
admin.site.register(Project) # registers the imported topic