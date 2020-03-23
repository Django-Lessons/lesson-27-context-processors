from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Category(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=30)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

