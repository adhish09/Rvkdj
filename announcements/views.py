from rest_framework import viewsets
from .serializers import AnnouncementSerializer
from .models import Announcement



class AnnouncementViewset(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    http_method_names = ["get"]