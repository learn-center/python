from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, ProductForm


def home(request):
    return HttpResponse("Hello from Django!")


def hello(request):
    products = Product.objects.all()
    product_form = ProductForm()
    return render(
        request,
        "hello.html",
        {
            "message": "message passed in from a view",
            "product_form": product_form,
            "products": products,
        },
    )


def save_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Product Saved Successfully!")
        else:
            return HttpResponse("Invalid request")
