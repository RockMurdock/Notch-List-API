from django.db import models
from django.db.models import F
from django.contrib.auth.models import User
from .drink_style import Drink_Style

class Wine(models.Model):

    user = models.OneToOneField(User, related_name='wine_reviewer', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    drink_style = models.ForeignKey(Drink_Style, on_delete=models.CASCADE)
    location_name = models.CharField(max_length=50)
    location_address = models.CharField(max_length=255)
    winery = models.CharField(max_length=50)
    rating = models.IntegerField()
    description = models.CharField(max_length=500)
    abv = models.CharField(max_length=10)
    year = models.CharField(max_length=10)
    image_path = models.ImageField(upload_to="beer", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = (F('created_at').desc(nulls_last = False),)
        verbose_name = "wine"
        verbose_name_plural = "wines"

    def __str__(self):
        return self.name