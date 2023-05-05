from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from core.models import ChargePoint


class ChargePointSerializer(ModelSerializer):
    class Meta:
        model = ChargePoint
        fields = '__all__'
        read_only_fields = ['pk', 'created_at', 'deleted_at']

    def validate(self, data):
        if not data.get('name'):
            raise ValidationError('Name is required')

        if not data.get('status'):
            raise ValidationError('Status is required')
        return data