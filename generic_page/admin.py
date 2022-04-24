from django.contrib import admin
from .models import Page

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', )
    
    ordering = ('title',)
    search_fields= ('title',)
    #date_hierarchy = 'published'
    list_filter = ('title',)
    
    
admin.site.register(Page, PageAdmin)
