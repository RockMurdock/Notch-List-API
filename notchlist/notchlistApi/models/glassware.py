from django.db import models

class Glassware(models.Model):

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    image_path = models.ImageField(upload_to="glassware", null=True, blank=True)

    class Meta:

        verbose_name = "glassware"
        verbose_name_plural = "glasswares"

    def __str__(self):
        return self.name
