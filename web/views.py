from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def About(request):
    return render(request, 'website/about.html')

def Contact(request):
    return render(request, 'website/contact.html')
    
def Index(request):
    return render(request, 'website/index.html')

def test_view(request):
    contex = {'name': 'hadi', 'lastname': 'shayeq'}
    return render(request, 'website/test.html', contex)

# Create your views here.
