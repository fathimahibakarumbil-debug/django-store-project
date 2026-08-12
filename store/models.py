from django.db import models

# Create your models here.

class Product(models.Model):
   
    price = models.FloatField()
    image_url = models.URLField()
    is_saved = models.BooleanField(default=False)

    def __str__(self):
        return self.price
    