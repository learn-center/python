from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse("Hello from Django")


def hello(request):
    return render(request, "hello.html", {"message": "message passed in from a view"})
