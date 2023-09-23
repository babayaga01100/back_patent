from django.urls import path

from patentNotice.views import (
    PatentNoticeListView,
    PatentNoticeDateListView
)

app_name = "patentNotice"

urlpatterns = [
    path("notice/", PatentNoticeListView.as_view(), name="patent-notice-list"),
    path("noticedate/", PatentNoticeDateListView.as_view(), name="patent-notice-list"),
]