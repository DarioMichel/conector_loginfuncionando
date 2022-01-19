from django.db import models

# Create your models here.
class Campaña(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    statuscampaña = models.BooleanField()

    def __str__(self):
        return self.nombre
