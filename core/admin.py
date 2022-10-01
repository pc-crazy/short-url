from django.contrib import admin
from core.models import ShortenUrl
# Register your models here.


class ShortenUrlAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'url', 'count', 'short_url']


admin.site.register(ShortenUrl, ShortenUrlAdmin)