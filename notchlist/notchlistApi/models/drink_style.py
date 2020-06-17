from django.db import models
from .glassware import Glassware


class Drink_Style(models.Model):

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    glassware = models.ForeignKey(Glassware, on_delete=models.CASCADE)

    class Meta:

        verbose_name = "drink style"
        verbose_name_plural = "drink styles"

    def __str__(self):
        return self.name