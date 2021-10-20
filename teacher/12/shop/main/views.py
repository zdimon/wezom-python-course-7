from django.shortcuts import render
from main.models import Page, Category, Product, Order, Testimonial
from django.core.paginator import Paginator


def make_order(request):
    cats = Category.objects.all()
    phone = request.POST.get('phone')
    product = Product.objects.get(pk=request.POST.get('product_id'))

    o = Order()
    o.phone = phone
    o.product = product
    o.save()

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
    cats = Category.objects.all()
    comments = Testimonial.objects.filter(product=product)
    return render(request,'product_detail.html', {"product": product, "cats": cats, "comments": comments})


def filter(request,category_id):
    print(category_id)
    current_category = Category.objects.get(id=category_id)
    products = Product.objects.filter(category=current_category)
    cats = Category.objects.all()
    return render(request,'filter.html', {"current_category": current_category, "cats": cats, "products": products})


def index(request):
     
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