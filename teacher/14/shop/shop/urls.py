"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main.views import index, about, feedback, filter, product_detail , make_order, search, logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('about', about),
    path('feedback', feedback),
    path('filter/<int:category_id>', filter),
    path('product/detail/<int:product_id>', product_detail),
    path('make/order', make_order),
    path('search', search),
    path('tinymce/', include('tinymce.urls')),
    path('logout', logout),
]


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = urlpatterns + static(settings.MEDIA_URL, 
                                   document_root=settings.MEDIA_ROOT)