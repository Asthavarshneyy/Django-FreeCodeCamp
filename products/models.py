from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
  title= models.CharField(max_length=120)
  description=models.TextField(null=True, blank=True) 
  price=models.DecimalField(default= 0, decimal_places=2, max_digits=100000)
  summary=models.TextField()
  featured=models.BooleanField(default=False)

  def get_absolute_url(self):
    # return f"/product/{self.id}/"
    return reverse("product-detail",kwargs={"id": self.id})