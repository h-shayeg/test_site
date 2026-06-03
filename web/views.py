from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from web.models import contact
from web.forms import NameForm, ContactForm

def about_view(request):
    return render(request, 'website/about.html')

def content_view(request):
    return render(request, 'website/contact.html')
    
def index_view(request):
    return render(request, 'website/index.html')

def test_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('done')
        else:
            return HttpResponse('not valid')
    form = ContactForm()
    return render(request, 'test.html', {'form': form})

# Create your views here.
