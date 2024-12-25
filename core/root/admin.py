from django.contrib import admin
from .models import Posts
from django.utils.html import format_html

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'photo_tag']

    def photo_tag(self, obj):
        if obj.photo:
            return format_html(f'<img src="{obj.photo.url}" width=80 height=auto>')
        else:
            return format_html('-')
    photo_tag.short_description = 'Photo'
    
admin.site.register(Posts, PostAdmin)