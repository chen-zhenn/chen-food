from django.db import models

# Create your models here.

class Category(models.Model):
    name =  models.CharField(max_length=45, null=False, blank=False)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Culinary(models.Model):
    name =  models.CharField(max_length=45, null=False, blank=False)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Dish(models.Model):
    name =  models.CharField(max_length=45, null=False, blank=False)
    image =  models.CharField(max_length=100, blank=False)
    description =  models.TextField(null=False, blank=False)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    category =  models.ForeignKey(Category, on_delete=models.PROTECT)
    culinary =  models.ForeignKey(Culinary, on_delete=models.PROTECT, default=None, null=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class Ingredient(models.Model):
    name =  models.CharField(max_length=45, null=False, blank=False)
    dish =  models.ForeignKey(Dish, on_delete=models.PROTECT, default=None, null=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name