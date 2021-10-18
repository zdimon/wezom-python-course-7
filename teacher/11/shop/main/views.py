from django.shortcuts import render
from main.models import Page, Category, Product

def index(request):
    page = Page.objects.get(alias='mainpage')
    cats = Category.objects.all()
    cat = Category.objects.get(name='food')
    products = Product.objects.filter(category=cat)
    return render(request,'index.html', {"page": page, "cats": cats, "products": products})


def about(request):
    page = Page.objects.get(alias='about')
    cats = Category.objects.all()
    return render(request,'about.html', {"page": page, "cats": cats})

def feedback(request):
    message = None
    if request.method == 'POST':
        print('this is POST')
        print(request.POST.get('name','Dima'))
        #print(request.POST['name'])

        message = 'Thank you!!!!!!'

    cats = Category.objects.all()
    return render(request,'feedback.html', {"cats": cats, "message": message})