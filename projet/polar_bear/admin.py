from django.contrib import admin

from .models import *

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')
    list_filter = ('author', 'date')
    search_fields = ('title', 'content')