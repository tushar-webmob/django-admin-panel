from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ['title', 'author',"price"]   
    list_display = ["thumbnail",'title','author','price','in_stock']
    list_filter = ['in_stock', 'is_active']
    list_editable = ['price', 'in_stock']
    prepopulated_fields = {'slug': ('title',)}
    list_per_page = 1

    def thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 40px; height:40px; border-radius: 50px;">'.format(obj.image.url))
        else:
            return '-'

    thumbnail.allow_tags = True
    thumbnail.short_description = 'Image'