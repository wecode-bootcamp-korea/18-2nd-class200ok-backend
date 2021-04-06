from django.urls import path

from .views      import PendingLectureListView

urlpatterns = [
    path('', PendingLectureListView.as_view())
]