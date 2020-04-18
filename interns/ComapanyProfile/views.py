from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response 
from .serializers import CompanySerializer
from .models import Company

class CompanyView(viewsets.ViewSet):

    def list(self, request):
        queryset = Company.objects.all()
        serializer = CompanySerializer(queryset, many=True)
        return Response(serializer.data)