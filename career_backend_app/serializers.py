from rest_framework import serializers
from .models import CareerRecommendation, UserProfile
from django.contrib.auth.models import User

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class CareerRecommendationSerializer(serializers.ModelSerializer):
    # 👇 this line is the key fix
    userprofile = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all())

    class Meta:
        model = CareerRecommendation
        fields = '__all__'