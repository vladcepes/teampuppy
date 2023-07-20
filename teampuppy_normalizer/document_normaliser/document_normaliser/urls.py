from django.urls import path, include
from knowledge.views import status_view

urlpatterns = [
    path('', include('knowledge.urls')),
    # Add other URL patterns as needed
]
