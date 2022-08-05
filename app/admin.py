from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'created_on')
    list_filter = ['created_on']
    search_fields = ['title', 'author']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)