from django.urls import path

from .views      import PendingLectureListView, PendingLectureDetailView

urlpatterns = [
    path('', PendingLectureListView.as_view()),
    path('/<int:pending_lecture_id>', PendingLectureDetailView.as_view())
]