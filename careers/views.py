from django.shortcuts import render
from .serializers import CareerSerailizer
from rest_framework import viewsets
from .models import Career
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny
from rest_framework.parsers import MultiPartParser

class CareerViewset(viewsets.ModelViewSet):
    queryset = Career.objects.all()
    serializer_class = CareerSerailizer
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    parser_classes = [MultiPartParser]
    permission_classes = [AllowAny]


   