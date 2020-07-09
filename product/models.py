from django.db import models
from django.contrib.auth.models import User


class Products(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    photo = models.ImageField(upload_to="product_photo", null=True, blank=True)
    active = models.BooleanField(default=True)








# Create your models here.
