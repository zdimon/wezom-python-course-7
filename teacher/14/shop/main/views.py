from django.shortcuts import render
from main.models import Page, Category, Product, Order, Testimonial, ProductImage, Cart
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.contrib import messages


def make_order(request):
    cats = Category.objects.all()
    phone = request.POST.get('phone')
    product = Product.objects.get(pk=request.POST.get('product_id'))

    o = Order()
    o.phone = phone
    o.product = product
    o.save()

    # send email
    send_mail(
    'Subject here',
    'Here is the message.',
    'from@example.com',
    ['to@example.com'],
    fail_silently=False,
    )

    return render(request,'make_order.html', {"cats": cats})

def product_detail(request,product_id):

    if request.method == "POST":
        prod = Product.objects.get(id=request.POST.get('product_id'))
        message = request.POST.get('message')
        t = Testimonial()
        t.product = prod
        t.content = message
        t.save()


    product = Product.objects.get(id=product_id)
    images = ProductImage.objects.filter(product=product)
    cats = Category.objects.all()
    comments = Testimonial.objects.filter(product=product)
    return render(request,'product_detail.html', {"product": product, "cats": cats, "comments": comments, "images": images})


def filter(request,category_id):
    print(category_id)
    current_category = Category.objects.get(id=category_id)
    products = Product.objects.filter(category=current_category)
    cats = Category.objects.all()
    return render(request,'filter.html', {"current_category": current_category, "cats": cats, "products": products})


'''
from django.contrib.auth import authenticate
user = authenticate(username='john', password='secret')
if user is not None:
    # A backend authenticated the credentials
else:
    # No backend authenticated the credentials
'''
from django.contrib.auth import authenticate, login

def index(request):

    if request.method == "POST":
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        #print(request.POST['username'])
        if user is not None:
            login(request,user)
            messages.info(request, 'Welcome!!!!')
        else:
            messages.info(request, 'Error!!!')

     
    try:
        page_number = request.GET['page']
    except:
        page_number = 1

    page = Page.objects.get(alias='mainpage')
    cats = Category.objects.all()
    cat = Category.objects.get(name='food')
    products = Product.objects.filter(category=cat)
    products = Product.objects.all()
    paginator = Paginator(products, 3)
    products = paginator.get_page(page_number)

    return render(request,'index.html', {"page": page, "cats": cats, "products": products, "page_number": page_number})


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


def search(request):
    cats = Category.objects.all()
    keyword = request.GET.get('keyword','food')

    products = Product.objects.filter(name__contains=keyword)

    return render(request,'search.html',{"keyword": keyword, "products": products})

from django.contrib.auth import logout as l

def logout(request):
    l(request)
    return render(request,'logout.html')

from django.contrib.auth.models import User

def registration(request):
    if request.method == 'POST':
        user = User()
        user.username = request.POST.get('username','')
        user.set_password(request.POST.get('password',''))
        user.is_active = True
        user.save()
        messages.info(request, 'Вы были успешно зарегистрированы!')
        login(request,user)
    return render(request,'registration.html')

def add_to_cart(request,product_id):
    product = Product.objects.get(id=product_id)
    try:
        c = Cart.objects.get(user=request.user,product=product)
    except:
        c = Cart()
        c.user = request.user
        c.product = product
        c.save()
    products = Cart.objects.filter(user=request.user)
    return render(request,'cart.html',{"product": product, "products": products})