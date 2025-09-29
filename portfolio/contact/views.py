from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import Contact
import logging
import sentry_sdk

logger = logging.getLogger(__name__)


def contact_view(request):
    """
    Gère le formulaire de contact
    """
    context = {}

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Création d'une instance (mais on ne la retourne pas !)
        Contact.objects.create(name=name, email=email, message=message)

        try:
            send_mail(
                subject=f"Nouveau message de {name}",
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_EMAIL],
                fail_silently=False,
            )
            context['success'] = True
        except Exception as e:
            context['error'] = True
            logger.warning("Erreur d'envoi d'email : %s", e)
            sentry_sdk.capture_exception(e)

    return render(request, 'contact/contact.html', context)
