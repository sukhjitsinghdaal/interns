from rest_framework import serializers
from .models import ProjectUser
from Meta.models import State
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectUser
        fields = "__all__"

    
