from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

#def services(request):
#    return render(request, 'core/services.html')

def visit(request):
    return render(request, 'core/visit.html')

#def contact(request):
#    return render(request, 'core/contact.html')

#def blog(request):
#    return render(request, 'core/blog.html')

def history(request):
    return render(request, 'core/history.html')

#def other(request):
#    return render(request, 'core/other.html')