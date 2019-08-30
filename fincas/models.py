from django.db import models
from users.models import User


class Property(models.Model):
    collaborator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Plot(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    latitude = models.DecimalField(max_digits=22, decimal_places=16)
    longitude = models.DecimalField(max_digits=22, decimal_places=16)

    def __str__(self):
        return self.name


class Tree(models.Model):
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE)
    diameter = models.DecimalField(max_digits=6, decimal_places=3)
    height = models.CharField(max_length=5)
    health = models.CharField(max_length=100)
    year = models.IntegerField()
