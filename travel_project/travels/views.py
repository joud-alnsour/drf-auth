from django.shortcuts import render
from rest_framework import generics
from .serializers import TravelSerializer
from .models import Travel
from rest_framework.permissions import IsAuthenticated

class TravelList(generics.ListCreateAPIView):
  permission_classes=(IsAuthenticated,)
  queryset = Travel.objects.all()
  serializer_class = TravelSerializer

class TravelDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes=(IsAuthenticated,)
  queryset = Travel.objects.all()
  serializer_class = TravelSerializer