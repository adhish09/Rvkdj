from django.shortcuts import render
from .serializers import EventSerializer
from rest_framework import viewsets
from .models import Event
from RVK_WEBPORTAL.permissions import ReadOnly
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from RVK_WEBPORTAL.pagination import CustomPagination
from django.utils import timezone
from rest_framework.response import Response

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by("-created_at")
    serializer_class = EventSerializer
    permission_classes = [ReadOnly]
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ('name',"location")
    pagination_class = CustomPagination


    @swagger_auto_schema(operation_description="Register for event", methods=["post",], responses={200: "Success"})
    @action(methods=['post'], detail=True,  name='register_event')
    def register(self, request, pk=None):
        event = self.get_object()

        event.registrants.add(request.user)

        return Response({200:"Successfully registed for the event"})
    

    @swagger_auto_schema(operation_description="All events", methods=["get",], responses={200: "Success"})
    @action(methods=['get'], detail=False,  name='all_events')
    def all_events(self, request,):

        upcoming_events = Event.objects.filter(start__gte=timezone.now())
        old_events = Event.objects.filter(start__lt=timezone.now(), end__lt=timezone.now())

        data = {
            "upcoming_events":EventSerializer(upcoming_events, many=True, context={"request":request}).data,
            "old_events":EventSerializer(old_events, many=True,context={"request":request}).data,
        }

        return Response(data)
        


