from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name



class Manufacturer(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    country = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Manufacturer'
        verbose_name_plural = 'Manufacturers'

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=150)
    size = models.CharField(max_length=5)
    manufac = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, null=True)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    price = models.IntegerField()

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name