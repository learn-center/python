from django.urls import path
from . import views

urlpatterns = [path("", views.home), path("hello/", views.hello), path("save_product/", views.save_product)]
