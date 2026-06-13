from django.contrib import admin
from blog.models import Post, Category
from django_summernote.admin import SummernoteModelAdmin

class PostaAmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    #empty_value_display = '-empty-'
    list_display = ('title', 'author', 'counted_view', 'status', 'published_date', 'created_date')
    list_filter = ('status', 'author')
    # ordering = ['-created_date']
    search_fields = ['title', 'counted']
    summernote_fields = ('content',)

admin.site.register(Category)
admin.site.register(Post, PostaAmin)
# Register your models here.
