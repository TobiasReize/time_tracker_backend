from django.urls import path
from .views import TimestampListCreateView

urlpatterns = [
    path('time_tracker', TimestampListCreateView.as_view(), name='timestamp'),
]
