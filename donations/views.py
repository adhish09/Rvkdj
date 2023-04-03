from django.shortcuts import render
from .serializers import DonationSerializer
from rest_framework import viewsets
from .models import Donation
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny


class DonationViewset(viewsets.ModelViewSet):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    permission_classes = [AllowAny]


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        


   