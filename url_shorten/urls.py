"""url_shorten URL Configuration"""

from django.contrib import admin
from django.urls import path, include
from core.views import ShortenUrlRedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
    path('<str:shortened_part>', ShortenUrlRedirectView.as_view(),
         name='short-n-redirect'),
]
