from rest_framework.serializers import ModelSerializer

from .models import PatentNotice, PatentNoticeDate

class PatenetNoticeBaseModelSerializer(ModelSerializer):
    class Meta:
        model = PatentNotice
        fields = "__all__"
        
class PatenetNoticeDateBaseModelSerializer(ModelSerializer):
    class Meta:
        model = PatentNoticeDate
        fields = "__all__"