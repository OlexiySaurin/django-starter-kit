from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import random
import colorsys

from django_countries.fields import CountryField


def generate_pastel_color():
    hue = random.random()  # Random hue
    saturation = 0.5 + random.random() * 0.5  # Keep saturation high (0.5 - 1.0)
    value = 0.7 + random.random() * 0.3  # Keep value high (0.7 - 1.0)

    r, g, b = colorsys.hsv_to_rgb(hue, saturation, value)

    return "#{:02X}{:02X}{:02X}".format(int(r * 255), int(g * 255), int(b * 255))

class User(AbstractUser):
    avatar = models.ImageField(upload_to='users/', null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = CountryField(null=True, blank=True)
    website = models.URLField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    is_private = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    color = models.CharField(max_length=7, default=generate_pastel_color, editable=False)
    is_online = models.BooleanField(default=False)
    last_seen = models.DateTimeField(null=True, blank=True)

    @property
    def age(self):
        if self.birth_date:
            return timezone.now().year - self.birth_date.year - (
                    (timezone.now().month, timezone.now().day) < (self.birth_date.month, self.birth_date.day)
            )
        return None
