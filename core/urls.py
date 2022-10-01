from django.urls import path

from core.views import *

app_name = 'core'
urlpatterns = [
    path('short-n-url/create/', ShortenedUrlCreateView.as_view())
]