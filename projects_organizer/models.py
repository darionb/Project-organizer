from django.db import models

# Create your models here.
class Project (models.Model):
    """Any service, provided by the company to a customer, for which resources, progress, and various interaction
     must be accounted for"""
    project_id = models.IntegerField()
