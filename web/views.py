from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from web.models import contact

def about_view(request):
    return render(request, 'website/about.html')

def content_view(request):
    return render(request, 'website/contact.html')
    
def index_view(request):
    return render(request, 'website/index.html')

def test_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        c = contact()
        c.name = name
        c.email = email
        c.subject = subject
        c.message = message
        c.save()
        print(name,email,subject,message)
    return render(request, 'test.html', {})

# Create your views here.
