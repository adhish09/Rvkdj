from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Donation


class DonationSerializer(ModelSerializer):
    created_at = SerializerMethodField()

    class Meta:
        model = Donation
        fields = '__all__'

    
    def get_created_at(self, obj):

        # Get the datetime object
        created_at = obj.created_at


        formatted_date = created_at.strftime("%Y-%m-%d")

        return formatted_date