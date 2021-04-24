from django.contrib import admin
from .import models


# Register your models here.
class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember


class GroupsAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_filter = ['name']
    list_display = ['name', 'description']


admin.site.register(models.Group, GroupsAdmin)
