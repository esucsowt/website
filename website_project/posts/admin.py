from django.contrib import admin

from . import models


class PostsAdmin(admin.ModelAdmin):
    search_fields = ['user', 'group']
    list_filter = ['group']
    list_display = ['created_at', 'user', 'group', 'message']


admin.site.register(models.Post, PostsAdmin)
