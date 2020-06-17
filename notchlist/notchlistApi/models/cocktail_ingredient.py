from django.db import models
from .cocktail import Cocktail
from .ingredient import Ingredient

class Cocktail_Ingredient(models.Model):

    cocktail = models.ForeignKey(Cocktail, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "cocktail ingredient"
        verbose_name_plural = "cocktails ingredients"

   