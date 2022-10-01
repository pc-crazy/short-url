from rest_framework.serializers import ModelSerializer

from core.models import ShortenUrl


class UrlSerializer(ModelSerializer):
    class Meta:
        model = ShortenUrl
        fields = ['url']
