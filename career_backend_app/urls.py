from django.urls import path
from . import views

urlpatterns = [
    path('userprofile/', views.UserProfileAPI.as_view(), name='user_profile_api'),
    path('recommendation/', views.CareerRecommendationAPI.as_view(), name='career_recommendation_api'),
]