from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(
        max_length=255)

    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="product")

    category = models.ForeignKey(
        "Category", 
        on_delete=models.SET_NULL,
        related_name="product",
        null=True,
        blank=True)

    description = models.TextField(
        null=True, 
        blank=True)

    price = models.DecimalField(
        default=0,
        max_digits=11,
        decimal_places=2)

    quantity = models.IntegerField(
        default=0)

    photo = models.ImageField(
        upload_to="product_photo", 
        null=True, 
        blank=True)

    active = models.BooleanField(
        default=True)

    deleted = models.BooleanField(
        default=False)

    def __str__(self):
        return self.name 
    
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Category(models.Model):
    name = models.CharField(
        max_length=255)
    age_limit = models.BooleanField(default=True)
    active = models.BooleanField(default=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"











# Create your models here.
