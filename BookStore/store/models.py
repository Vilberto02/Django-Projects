from django.db import models

# Create your models here.
class MetodoPago(models.Model):
  title = models.CharField()

class OrdenCompra(models.Model):
  title = models.CharField()

class Estado(models.Model):
  title = models.CharField()