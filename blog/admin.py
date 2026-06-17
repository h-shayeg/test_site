from django.contrib import admin
from blog.models import Post, Category, Comment
from django_summernote.admin import SummernoteModelAdmin

class PostaAmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    #empty_value_display = '-empty-'
    list_display = ('title', 'author', 'counted_view', 'status', 'published_date', 'created_date')
    list_filter = ('status', 'author')
    # ordering = ['-created_date']
    search_fields = ['title', 'counted']
    summernote_fields = ('content',)
class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('name', 'post', 'email', 'subject', 'approved', 'created_date')
    list_filter = ('post', 'approved',)
    search_fields = ['name', 'email', 'subject']

admin.site.register(Comment, CommentAdmin)
admin.site.register(Category)
admin.site.register(Post, PostaAmin)
# Register your models here.
