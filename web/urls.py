from django.urls import path
from web.views import about_view, content_view, index_view, test_view

app_name = 'web'

urlpatterns = [
    path('about',about_view, name = 'about'),
    path('contact', content_view, name = 'contact'),
    path('', index_view, name = 'index'),
    path('test', test_view, name = 'test')
]
