from django.contrib import admin
from . import models

class ViewsInline(admin.TabularInline):
    model = models.View
    readonly_fields = ('session_id','timestamp')

class UrlAdmin(admin.ModelAdmin):
    list_display = ( 'url', 'hash', 'user', 'views' )
    list_filter = ['user']
    search_fields = ['url']
    inlines = [ViewsInline]

admin.site.register(models.Url, UrlAdmin)
