from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('a', 'Admin'),
        ('s', 'Student'),
        ('t', 'Teacher'),
        ('p', 'Parent')
    )
    roles = models.CharField(max_length=1, choices=ROLE_CHOICES)


class AuthorModel(models.Model):
    name = models.CharField(max_length=200, default='')
    fname = models.CharField(max_length=200, default='')
    country = models.CharField(max_length=200, default='')

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = 'author'


class BookModel(models.Model):
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default='')
    page = models.PositiveSmallIntegerField(default=1)
    price = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = 'book'
