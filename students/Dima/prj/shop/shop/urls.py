from django.contrib import admin
from django.urls import path
from main.views import index,categories,cart,product,checkout,contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('categories', categories),
    path('cart', cart),
    path('product', product),
    path('checkout', checkout),
    path('contact', contact),
]
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = urlpatterns + static(settings.MEDIA_URL,
      document_root = settings.MEDIA_ROOT)
