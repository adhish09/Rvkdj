from django.shortcuts import render
from .serializers import VolunteerSerializer
from rest_framework import viewsets
from .models import Volunteer
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny


class VolunteerViewset(viewsets.ModelViewSet):
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    permission_classes = [AllowAny]


   