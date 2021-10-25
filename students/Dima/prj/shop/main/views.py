from django.shortcuts import render
from main.models import Page, Category,Product

def index(request):

    return render(request,'index.html')

def categories(request):
    page = Page.objects.get(alias='About')
    cats = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'categories.html', {'page': page, 'cats': cats, 'products': products})

def cart(request):

    return render(request,'cart.html')

def product(request):

    return render(request,'product.html')

def checkout(request):

    return render(request,'checkout.html')

def contact(request):

    return render(request,'contact.html')    
