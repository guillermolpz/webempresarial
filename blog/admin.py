from django.contrib import admin
from .models import Categoria, Blog

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    
class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'published', 'author', 'blog_categories')
    
    ordering = ('author',)
    search_fields= ('title','author__username', 'categories__name')
    date_hierarchy = 'published'
    list_filter = ('author__username', 'categories__name')
    
    def blog_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    
    blog_categories.short_description = "Categorías"
    
    
admin.site.register(Categoria, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)
