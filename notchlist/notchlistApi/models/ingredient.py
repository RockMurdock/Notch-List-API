from django.db import models
from .cocktail import Cocktail


class Ingredient(models.Model):

    name = models.CharField(max_length=50)
    cocktails = models.ManyToManyField("Cocktail", through="Cocktail_Ingredient",)

    class Meta:
        verbose_name = "ingredient"
        verbose_name_plural = "ingredients"