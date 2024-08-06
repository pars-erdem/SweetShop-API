from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    stock= models.IntegerField()
    in_stock = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.in_stock = self.stock > 0
        super().save(*args, **kwargs)

    def __str__(self):
        return f"product name:{self.product} stock:{self.stock} price:{self.price}"