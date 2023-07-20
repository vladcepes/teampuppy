from django.urls import path
from knowledge.views import status_view

urlpatterns = [
    path('v1.0/team/knowledge/status/', status_view, name='status'),
    # Add other URL patterns as needed
]
