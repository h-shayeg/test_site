from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from web.models import contact
from web.forms import NameForm, ContactForm, NewsletterForm

def about_view(request):
    return render(request, 'website/about.html')

def content_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ContactForm()
    return render(request, 'website/contact.html', {'form': form})

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')

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
