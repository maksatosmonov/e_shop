from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(
        max_length=255)
    age_limit = models.BooleanField(default=True)
    active = models.BooleanField(default=True)
    description = models.TextField(
        blank=True,
        null=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"











# Create your models here.
