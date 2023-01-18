from django.db import models


# Create your models here.
class Article(models.Model):
  title= models.CharField(blank=False, null=False, max_length=20)
  