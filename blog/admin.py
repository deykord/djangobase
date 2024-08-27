from django.contrib import admin
from .models import Post

# Register your models here
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'counted_views', 'published_date', 'created_date', 'updated_date')
    list_filter = ('status', 'created_date', 'published_date')
    search_fields = ('title', 'content')
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    # ordering = ('-created_date',)
admin.site.register(Post, PostAdmin)
