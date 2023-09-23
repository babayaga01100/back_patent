from django.urls import path

from patentNotice.views import (
    PatentNoticeListView,
)

app_name = "patentAttorneys"

urlpatterns = [
    path("notice/", PatentNoticeListView.as_view(), name="patent-notice-list"),
]