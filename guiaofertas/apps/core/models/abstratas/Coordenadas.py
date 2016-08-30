from django.db import models


class Coordenadas(object):
    latitude = models.DecimalField("Latitude", max_digits=15, decimal_places=12, null=True, blank=False)
    longitude = models.DecimalField("Latitude", max_digits=15, decimal_places=12, null=True, blank=False)

    class Meta:
        abstract = True