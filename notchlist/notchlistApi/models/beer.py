from django.db import models
from django.db.models import F
from django.contrib.auth.models import User
from .beer_serving_style import Beer_Serving_Style
from .drink_style import Drink_Style

class Beer(models.Model):

    user = models.ForeignKey(User, related_name='beer_reviewer', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    drink_style = models.ForeignKey(Drink_Style, related_name='drink_style', on_delete=models.CASCADE)
    location_name = models.CharField(max_length=50)
    location_address = models.CharField(max_length=255)
    brewery = models.CharField(max_length=50)
    rating = models.IntegerField()
    description = models.CharField(max_length=500)
    abv = models.CharField(max_length=10)
    ibu = models.CharField(max_length=10)
    beer_serving_style = models.ForeignKey(Beer_Serving_Style, related_name='beer_serving_style', on_delete=models.CASCADE)
    image_path = models.ImageField(upload_to="beer", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = (F('created_at').desc(nulls_last = False),)
        verbose_name = "beer"
        verbose_name_plural = "beers"

    def __str__(self):
        return self.name


