from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from web.models import contact
from web.forms import NameForm, ContactForm, NewsletterForm
from django.contrib import messages

def about_view(request):
    return render(request, 'website/about.html')

def content_view(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your message has been sent successfully!')
            form = ContactForm()
        else:
            messages.add_message(request, messages.ERROR, 'There was an error sending your message. Please try again.')
       
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
