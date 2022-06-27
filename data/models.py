from django.db import models

# Create your models here.
class profile(models.Model):
    name = models.CharField(max_length=200, blank=True,null=True)
    email = models.EmailField(max_length=500, blank=True,null=True )