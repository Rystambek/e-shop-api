from django.db import models
from django.contrib.auth.models import User
    # 
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField()
    ram = models.IntegerField()
    color = models.CharField(max_length=20)
    memory = models.IntegerField()

    def __str__(self):
        return self.name
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product =  models.ForeignKey(Product,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)
class Comment(models.Model):
    text=models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product =  models.ForeignKey(Product, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)

class Like(models.Model):
    like = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product =  models.ForeignKey(Product, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)



