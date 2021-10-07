from django.contrib import admin
from main.models import Page, Category, Product


class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'alias']

admin.site.register(Page, PageAdmin)


class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    list_filter = ['category']
    search_fields = ['name']

admin.site.register(Product, ProductAdmin)