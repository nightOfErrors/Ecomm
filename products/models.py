from django.db import models

# Create your models here.

class Product(models.Model):
    
    name = models.CharField(max_length=50)
    pic = models.ImageField(null=True, blank=True)
    price = models.IntegerField()
    description = models.TextField()


    def __str__(self):
        return self.name

    
