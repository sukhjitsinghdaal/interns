from .models import Company
from rest_framework import serializers
from Meta.models import State
class CompanySerializer(serializers.ModelSerializer):

    state = serializers.SerializerMethodField()
    class Meta:
        model = Company
        fields = '__all__'

    def get_state(self,req):
        state = State.objects.get(id=req.id)
        return state.name
        

