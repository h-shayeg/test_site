from django.contrib import admin
from blog.models import Post

@admin.register(Post)
class PostaAmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    #empty_value_display = '-empty-'
    list_display = ('title', 'counted_view', 'status', 'published_date', 'created_date')
    list_filter = ('status',)
    # ordering = ['-created_date']
    search_fields = ['title', 'counted']
# Register your models here.
