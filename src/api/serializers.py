from django.core.exceptions import ValidationError
from rest_framework import serializers

from core.models import ChargePoint


class ChargePointSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChargePoint
        fields = '__all__'


class CreateChargePointSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    status = serializers.CharField(required=True)


class UpdateChargePointSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    status = serializers.CharField(required=False)

    def validate(self, attrs):
        if not attrs:
            raise ValidationError('Please provide some value')

        return attrs
