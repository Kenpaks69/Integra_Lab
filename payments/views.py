from rest_framework import viewsets
from django.http import JsonResponse
import logging

logger = logging.geLogger(__name__)

@ratelimit(key='ip', rate='5/m', block=True)
def secure_payment_views(request):
    logger.warning("Payment EndPoint Accessed")
    return JsonRespone({"status": "Secured connection established"})
    