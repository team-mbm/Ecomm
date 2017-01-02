from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.IntegerField()
    company = models.CharField(max_length=50)
    image = models.ImageField(upload_to="product_pics")
    wide_image = models.ImageField(upload_to="product_pics_wide", null=True)

    description = models.CharField(max_length=1000)
    def __str__(self):
        return self.title + " | " + self.company
