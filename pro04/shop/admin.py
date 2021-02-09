from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    # slug 필드를 name 필드의 값으로 자동으로 설정
    prepopulated_fields = {'slug':['name']}

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'category', 'price', 'stock', 'available_display', 'available_order', 'created', 'updated']
    list_filter = ['available_display', 'created', 'updated', 'category']
    prepopulated_fields = {'slug':('name',)}
    list_editable = ['price', 'stock', 'available_display', 'available_order']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)