from django.shortcuts import render
from main.models import Page, Category, Product

def index(request):
    page = Page.objects.get(alias='mainpage')
    cats = Category.objects.all()
    products = Product.objects.all()
    return render(request,'index.html', {"page": page, "cats": cats, "products": products})


def about(request):
    page = Page.objects.get(alias='about')
    cats = Category.objects.all()
    return render(request,'about.html', {"page": page, "cats": cats})