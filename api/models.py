from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=150, blank=False)
    state = models.CharField(max_length=150, blank=False)
    latitude = models.DecimalField(decimal_places=8)
    longitude = models.DecimalField(decimal_places=8)

    def __str__(self):
        return self.name + '|' + self.state