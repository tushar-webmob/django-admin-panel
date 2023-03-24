from django.contrib import admin
from . import models
from django.utils.html import format_html
# Register your models here

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'author',"price"]   
    list_display = ["thumbnail",'title','author','body']
    list_filter = ['favourties','created']


    def thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 40px; height:40px; border-radius: 50px;">'.format(obj.image.url))
        else:
            return '-'

    thumbnail.allow_tags = True
    thumbnail.short_description = 'Image'


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ['name', 'author']   
    list_display = ["thumbnail",'name','author','message']

    def thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 40px; height:40px; border-radius: 50px;">'.format(obj.image.url))
        else:
            return '-'

    thumbnail.allow_tags = True
    thumbnail.short_description = 'Image'