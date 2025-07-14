from django import forms
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    photo = models.ImageField(upload_to="images/")


class Review(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="reviews"
    )
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_created=True)


class Inventory(models.Model):
    product = models.OneToOneField(
        Product, on_delete=models.CASCADE, related_name="inventory"
    )
    quantity = models.PositiveIntegerField()
    last_updated = models.DateTimeField(auto_now=True)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "photo"]
