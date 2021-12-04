from django.db import models

# Create your models here.

class Contact(models.Model):
    name= models.CharField(max_length=200)
    email=models.CharField(max_length=30)
    phone=models.CharField(max_length=16)
    message=models.TextField()

    def __str__(self):
        return self.name