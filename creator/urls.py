from django.urls import path

from creator.views import TitleAndCoverView, ClassIntroductionView, SummaryView, CreatorIntroductionView, BasicInformationView

urlpatterns = [
    path('/basic-information', BasicInformationView.as_view()),
    path('/title-and-cover', TitleAndCoverView.as_view()),
    path('/class-introduction', ClassIntroductionView.as_view()),
    path('/summary', SummaryView.as_view()),
    path('/creator-introduction', CreatorIntroductionView.as_view()),
]
