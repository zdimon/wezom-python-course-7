from django.contrib import admin
from main.models import Page, Category, Product, Order, Testimonial
from image_cropping import ImageCroppingMixin

class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'alias']

admin.site.register(Page, PageAdmin)


class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ['name', 'category', 'image_tag', 'desc']
    list_filter = ['category']
    search_fields = ['name']

admin.site.register(Product, ProductAdmin)




class OrderAdmin(admin.ModelAdmin):
    list_display = ['product', 'phone', 'done']
    list_editable = ['done']

admin.site.register(Order, OrderAdmin)


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['product', 'content']
   

admin.site.register(Testimonial, TestimonialAdmin)