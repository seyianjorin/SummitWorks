from django.contrib.auth.models import User
from django.db import models
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=50, null=False)
    price = models.IntegerField(null=False)
    description = models.CharField(max_length=200, null=False)
    quantity = models.IntegerField(null=False)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/', null=True, blank=True)

    def __str__(self):
        return self.name