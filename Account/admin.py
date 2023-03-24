from django.contrib import admin
from .models import Register

@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    search_fields = ['username', 'email']   
    list_filter = ['name', 'username'] 
    list_display = ['name','email','username']  


