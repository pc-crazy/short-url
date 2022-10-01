import os
from datetime import timedelta
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic.base import View
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from core.models import ShortenUrl
from core.serializers import UrlSerializer


class ShortenedUrlCreateView(CreateAPIView):
    """
    Make a new short url.
    """
    serializer_class = UrlSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = serializer.save()
        headers = self.get_success_headers(serializer.data)
        short_url = self.request.build_absolute_uri(
            reverse('short-n-redirect',
                    kwargs={"shortened_part": obj.short_url})
        )
        return Response({"short-url": short_url}, status=201,
                        headers=headers)


class ShortenUrlRedirectView(View):
    """
    redirects short n url to real url.
    """
    def get(self, request, shortened_part, *args, **kwargs):
        try:
            validity = int(os.environ.get("LINK_VALID", 4))
            time_threshold = timezone.now() - timedelta(days=validity)
            shortener = ShortenUrl.objects.get(
                short_url=shortened_part,
                created_at__gte=time_threshold
            )
            shortener.count += 1
            shortener.save()
            return HttpResponseRedirect(shortener.url)
        except ShortenUrl.DoesNotExist:
            return HttpResponse("Invalid link")
