from django.urls import path
from .views import Home,CareerRecommendationAPI, RegisterUser, LoginUser

urlpatterns = [
     path('', Home.as_view(), name='home'),
    path('predict/', CareerRecommendationAPI.as_view(), name='predict'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
]
from django.urls import path
from .views import predict_career

urlpatterns = [
    path('predict/', predict_career),
]