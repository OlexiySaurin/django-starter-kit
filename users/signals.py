from allauth.account.signals import email_confirmed
from django.dispatch import receiver

from users.models import User


@receiver(email_confirmed)
def email_confirmed_(request, email_address, **kwargs):
    user = User.objects.get(email=email_address.email)
    user.is_verified = True
    user.save()
    return user