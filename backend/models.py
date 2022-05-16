from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Products(models.Model):
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    
    name = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_trandy = models.BooleanField(default=False)
    is_arrived = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class NavSlide(models.Model):
    class Meta:
        verbose_name = 'Navbar slide'
        verbose_name_plural = 'Navbar slides'
    
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    image = models.ImageField()

    def __str__(self):
        return self.name

class ProductCategories(models.Model):
    class Meta:
        verbose_name = 'Product Category'
        verbose_name_plural = 'Product Categories'
    
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class ProductColor(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class ProductSize(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class ClotheTypeCategory(models.Model):
    class Meta:
        verbose_name = 'Clothe type category'
        verbose_name_plural = 'Clothe type categories'

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name