from rest_framework.generics import ListCreateAPIView
from time_tracker_app.models import Timestamp
from .serializers import TimestampSerializer

class TimestampListCreateView(ListCreateAPIView):
    queryset = Timestamp.objects.all()
    serializer_class = TimestampSerializer


    def get_queryset(self):
        if self.request.user.is_superuser:
            return Timestamp.objects.all()
        else:
            return Timestamp.objects.filter(user=self.request.user)


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
