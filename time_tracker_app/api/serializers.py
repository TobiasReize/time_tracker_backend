from rest_framework import serializers
from time_tracker_app.models import Timestamp

class TimestampSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timestamp
        fields = '__all__'
