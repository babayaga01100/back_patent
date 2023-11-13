from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import PatentNotice, PatentNoticeDate
from .serializers import PatenetNoticeBaseModelSerializer,PatenetNoticeDateBaseModelSerializer

# Create your views here.
# 공지사항 리스트 보기
class PatentNoticeListView(generics.ListAPIView):
    queryset = PatentNotice.objects.all()
    serializer_class = PatenetNoticeBaseModelSerializer

# class PatentNoticeDateListView(generics.ListAPIView):
    # queryset = PatentNoticeDate.objects.all()
    # serializer_class = PatenetNoticeDateBaseModelSerializer
class PatentNoticeDateListView(APIView):
    def get(self, request, pk):
        try:
            patentNotice = PatentNotice.objects.get(id=pk)
        except PatentNotice.DoesNotExist:
            return Response({'detail': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
        
        queryset = PatentNoticeDate.objects.filter(title=PatentNoticeDate)
        queryset_serializer = PatenetNoticeBaseModelSerializer(queryset, many=True) # many : 중복 표현 값에 대한 list를 받고자 할 때 사용
        
        return Response(queryset_serializer.data, status=status.HTTP_200_OK)