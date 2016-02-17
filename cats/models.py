from django.db import models
from django.contrib.auth.models import User


class Breed(models.Model):
    """Docstring for Cat Breed model"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.ForeignKey(Breed)
    age = models.PositiveIntegerField(default=0)
    photo = models.URLField(blank=True, null=True)

    owner = models.ForeignKey(User)

    def __str__(self):
        return "{name} | Breed {breed} | Owner {owner}".format(
            name=self.name,
            breed=self.breed.name,
            owner=self.owner.first_name,
        )
