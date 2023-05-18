from django.db import models

# Create your models here.


class data(models.Model):
    place = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)

    class Meta:
        verbose_name = ("data")
        verbose_name_plural = ("data")

    def __str__(self):
        return self.email
