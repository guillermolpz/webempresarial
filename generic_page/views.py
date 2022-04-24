from django.shortcuts import render
from .models import Page

# Create your views here.

def Page_g(request, page_id):
    #page = Page.objects.all()
    page = Page.objects.get(id = page_id)
    return render(request, 'other.html', {'page':page})