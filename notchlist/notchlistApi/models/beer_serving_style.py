from django.db import models


class Beer_Serving_Style(models.Model):

    name = models.CharField(max_length=50)

    class Meta:

        verbose_name = "beer serving style"
        verbose_name_plural = "beer serving styles"

    def __str__(self):
        return self.name