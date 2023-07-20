# views.py

from django.http import JsonResponse
from django.conf import settings
import time

def status_view(request):
    # Use the server startup timestamp from settings
    server_startup_time = settings.SERVER_STARTUP_TIME

    # Get the current timestamp
    current_time = time.time()

    # Calculate the uptime in milliseconds
    uptime_ms = int((current_time - server_startup_time) * 1000)

    # Prepare the response data
    response_data = {
        "serviceName": "Document Normaliser Service",
        "upTime": uptime_ms,
    }

    return JsonResponse(response_data)
