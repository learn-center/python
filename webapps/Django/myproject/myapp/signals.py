from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from .models import Product, Inventory, Review


@receiver(pre_save, sender=Product)
def pre_save_product(sender, instance, **kwargs):
    print("pre insert product")


@receiver(post_save, sender=Product)
def create_inventory_for_product(sender, instance, created, **kwargs):
    print("inside POST: create_inventory_for_product")
    if created:
        Inventory.objects.create(product=instance, quantity=0)
        print(f"Inventory created for new product: {instance.name}")


@receiver(post_save, sender=Review)
def review_added(sender, instance, created, **kwargs):
    if created:
        print(f"New review added for {instance.product.name} : {instance.comment}")
