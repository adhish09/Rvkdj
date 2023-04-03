from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Career




class CareerSerailizer(ModelSerializer):
    class Meta:
        model = Career
        fields = '__all__'