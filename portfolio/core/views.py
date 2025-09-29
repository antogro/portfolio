from django.shortcuts import render
import sentry_sdk
import logging

logger = logging.getLogger(__name__)


def index(request):
    """
    Affiche la page d'accueil
    :param request: HttpRequest
    """
    # This function handles the request to display the home page.
    return render(request, 'core/index.html')


def about(request):
    """
    Affiche la page à propos
    :param request: HttpRequest
    """
    # This function handles the request to display the about page.
    return render(request, 'core/about.html')


def services(request):
    """
    Affiche la page des services
    :param request: HttpRequest
    """
    # This function handles the request to display the services page.
    return render(request, 'services.html')


def custom_404_view(request, exception):
    """
    Affiche la page d'erreur 404
    :param request: HttpRequest
    :param exception: Exception
    """
    # Log de l'erreur 404
    logger.warning('Page not found: %s', request.path)
    sentry_sdk.capture_exception(f"Erreur 404: {request.path}")
    # Rendu de la page Erreur 404
    return render(request, '404.html', status=404)


def custom_500_view(request):
    """
    Affiche la page d'erreur 500
    :param request: HttpRequest
    """
    # Log de l'erreur 500
    logger.error('Server error: %s', request.path)
    sentry_sdk.capture_exception(f"Erreur 500: {request.path}")
    # Rendu de la page Erreur 500
    return render(request, '500.html', status=500)
