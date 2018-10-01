from django.contrib.gis.db import models

class PowerPlant(models.Model):
    shp_id =  models.CharField(max_length=255, default="NULL")
    name = models.CharField(max_length=255)
    plant = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    total_power = models.CharField(max_length=255)
    type_of = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    power_mw = models.FloatField()
    power_cat = models.FloatField()
    built = models.FloatField()
    connected = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    lon = models.FloatField()
    lat = models.FloatField()
    elev = models.FloatField()
    image = models.CharField(max_length=255)

    mpoly = models.PointField()

    # Returns the string representation of the model.
    def __str__(self):
        return self.name