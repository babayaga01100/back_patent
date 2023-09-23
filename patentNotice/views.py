from rest_framework import generics

from .models import PatentNotice, PatentNoticeDate
from .serializers import PatenetNoticeBaseModelSerializer,PatenetNoticeDateBaseModelSerializer

# 공지사항 리스트 보기
class PatentNoticeListView(generics.ListAPIView):
    queryset = PatentNotice.objects.all()
    serializer_class = PatenetNoticeBaseModelSerializer

class PatentNoticeDateListView(generics.ListAPIView):
    queryset = PatentNoticeDate.objects.all()
    serializer_class = PatenetNoticeDateBaseModelSerializer

# Create your views here.
