from django.db import models

# Create your models here.
class servidores(models.Model):
	mac = models.CharField(max_length=18, null=False, blank=False)
	ip = models.CharField(max_length=18, null=False, blank=False)
	hostname = models.CharField(max_length=30, null=False, blank=False)
	estado = models.CharField(max_length=30, null=False, blank=False)
	token = models.CharField(max_length=70, null=False, blank=False)

class user(models.Model):
	usuario = models.CharField(max_length=10)
	nombre = models.CharField(max_length=10)
	password = models.CharField(max_length=15)	