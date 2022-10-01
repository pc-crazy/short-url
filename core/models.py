import os
from random import choice
from string import ascii_letters, digits

from django.db import models


AVAILABLE_CHARS = ascii_letters + digits


def create_random_code(chars=AVAILABLE_CHARS):
    """Create a random string from the given chars

    :parameter
    chars (str) : unique string
    :return string of size length."""
    size = int(os.environ.get("URL_SIZE", 4))
    return "".join(
        [choice(chars) for _ in range(size)]
    )


class ShortenUrl(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    url = models.URLField()
    count = models.PositiveSmallIntegerField(default=0)
    short_url = models.URLField(unique=True)

    def __str__(self):
        return self.url

    def save(self, *args, **kwargs):
        """
        set new short url and save object.
        :param args:
        :param kwargs:
        :return:
        """
        while not self.short_url:
            random_code = create_random_code()
            if not self.__class__.objects.filter(
                    short_url=random_code
            ).exists():
                self.short_url = random_code

        super().save(*args, **kwargs)