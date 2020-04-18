from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response 
from .serializers import CategorySerializer,StateSerializer
from .models import Category,State

class CategoryView(viewsets.ViewSet):

    def list(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)

class StateView(viewsets.ViewSet):

    def list(self, request):
        queryset = State.objects.all()
        serializer = StateSerializer(queryset, many=True)
        return Response(serializer.data)