from rest_framework import serializers
from .models import ProjectUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectUser
        fields = "__all__"