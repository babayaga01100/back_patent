from rest_framework.serializers import ModelSerializer

from .models import PatentNotice

class PatenetNoticeBaseModelSerializer(ModelSerializer):
    class Meta:
        model = PatentNotice
        fields = "__all__"