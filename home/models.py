from django.db import models

# Create your models here.

class Candidates(models.Model):
    name=models.CharField(max_length=50)
    job=models.CharField(max_length=50)
    image=models.ImageField(upload_to='Candidates/')
    email=models.CharField(max_length=50,null=True)
    phone=models.CharField(max_length=50,null=True)
    city=models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.name
class Companies(models.Model):
    title=models.CharField(max_length=50)
    image=models.ImageField(upload_to='companies/')
    def __str__(self):
        return self.title