from django.contrib import admin
from main.models import Page, Category, Product, Order
from image_cropping import ImageCroppingMixin

class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'alias']

admin.site.register(Page, PageAdmin)


class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ['name', 'category', 'image_tag']
    list_filter = ['category']
    search_fields = ['name']

admin.site.register(Product, ProductAdmin)




class OrderAdmin(admin.ModelAdmin):
    pass

admin.site.register(Order, OrderAdmin)