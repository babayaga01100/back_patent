from rest_framework import generics

from .models import PatentNotice
from .serializers import (
    PatenetNoticeBaseModelSerializer,
)

# 공지사항 리스트 보기
class PatentNoticeListView(generics.ListAPIView):
    queryset = PatentNotice.objects.all()
    serializer_class = PatenetNoticeBaseModelSerializer


# Create your views here.
