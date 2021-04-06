from django.urls import path

from creator.views import BasicInformationView, TitleAndCoverView, ClassIntroduction, SummaryView, CreatorIntroductionView, FinalChecklistsView

urlpatterns = [
    path('/basic-information', BasicInformationView.as_view()),
    path('/title-and-cover', TitleAndCoverView.as_view()),
    path('/class-introduction', ClassIntroduction.as_view()),
    path('/summary', SummaryView.as_view()),
    path('/creator-introduction', CreatorIntroductionView.as_view()),
    path('/final-checklists', FinalChecklistsView.as_view()),
]