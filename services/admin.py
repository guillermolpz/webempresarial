from re import search
from django.contrib import admin

from .models import Services
# Register your models here.

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('id','image','title','subtitle', 'content','created')
    list_display_links = ('id','title',)
    
    list_filter = ('created','update')
    search_fields = ('title','subtitle')
    
    readonly_fields = ('created','update')
