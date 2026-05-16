from django.urls import path
from web.views import About, Contact, Index, test_view

app_name = 'web'

urlpatterns = [
    path('about',About, name = 'about'),
    path('contact', Contact, name = 'contact'),
    path('', Index, name = 'index'),
    path('test', test_view, name = 'test')
]
