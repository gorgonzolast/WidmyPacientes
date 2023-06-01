from django.db import models

# Create your models here.
class Paciente(models.Model):
    id = models.AutoField(primary_key=True)
    idCard = models.IntegerField() 
    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=1, choices=(('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')))
    email= models.EmailField(max_length=254)
    phone = models.IntegerField()
    address = models.CharField(max_length=50)