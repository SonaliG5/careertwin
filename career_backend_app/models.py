from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    skills = models.TextField()
    interests = models.TextField()

    def _str_(self):
        return self.name


class CareerRecommendation(models.Model):
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    recommended_career = models.CharField(max_length=100)
    confidence_score = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.userprofile.name} - {self.recommended_career}"
