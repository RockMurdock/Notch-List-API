from django.db import models
from django.db.models import F
from django.contrib.auth.models import User


class Cocktail(models.Model):

    user = models.OneToOneField(User, related_name='cocktail_reviewer', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    location_name = models.CharField(max_length=50)
    location_address = models.CharField(max_length=255)
    brewery = models.CharField(max_length=50)
    rating = models.IntegerField()
    description = models.CharField(max_length=500)
    image_path = models.ImageField(upload_to="cocktails", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    ingredients = models.ManyToManyField("Ingredient", through="Cocktail_Ingredient",)

    class Meta:
        ordering = (F('created_at').desc(nulls_last = False),)
        verbose_name = "cocktail"
        verbose_name_plural = "cocktails"

    def __str__(self):
        return self.name