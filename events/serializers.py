from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Event
from accounts.serializers import UserGetSerializer



class EventSerializer(ModelSerializer):
    registrants = UserGetSerializer(many=True)
    event_image = SerializerMethodField()
    
    def get_event_image(self, obj):
        if obj.event_image:
            return self.context['request'].build_absolute_uri(obj.event_image.url)
        else:
            return None
        
    class Meta:
        model = Event
        fields = '__all__'


