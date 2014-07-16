from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=255)
    order = models.IntegerField(default=1)
