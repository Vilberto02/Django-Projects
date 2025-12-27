from django.db import models

# Create your models here.
class Libro(models.Model):
  title = models.CharField()

class Ejemplar(models.Model):
  title = models.CharField()

class LibroAutor(models.Model):
  title = models.CharField()