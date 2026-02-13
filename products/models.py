from django.db import models

# Create your models here.



class Category(models.Model):
    category_name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
         return self.category_name



class Vehicle(models.Model):
    name = models.CharField(max_length=200)
    make = models.CharField(max_length=100)
    year = models.IntegerField()
    image = models.ImageField(upload_to='Images')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    short_description = models.CharField(max_length=100, default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
