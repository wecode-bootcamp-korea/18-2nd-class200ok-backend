from django.urls import path
from user.views import KakaoSignInView

urlpatterns = [
    path('/signin', KakaoSignInView.as_view())
    
]