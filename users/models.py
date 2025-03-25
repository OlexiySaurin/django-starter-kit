from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django_countries.fields import CountryField




class User(AbstractUser):
    class Gender(models.TextChoices):
        NOT_SPECIFIED = 'Not Specified'
        MALE = 'Male'
        FEMALE = 'Female'
        OTHER = 'Other'

    avatar = models.ImageField(upload_to='users/', blank=True, default="users/default.png")
    gender = models.CharField(max_length=15, choices=Gender.choices, default=Gender.NOT_SPECIFIED)
    birth_date = models.DateField(null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = CountryField(null=True, blank=True)
    website = models.URLField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    is_private = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_online = models.BooleanField(default=False)
    last_seen = models.DateTimeField(null=True, blank=True)

    @property
    def age(self):
        if self.birth_date:
            return timezone.now().year - self.birth_date.year - (
                    (timezone.now().month, timezone.now().day) < (self.birth_date.month, self.birth_date.day)
            )
        return None
