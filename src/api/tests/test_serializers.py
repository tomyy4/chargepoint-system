from django.test import TestCase

from api.serializers import ChargePointSerializer


class TestChargePointSerializer(TestCase):
    def test_will_raise_validation_error_if_empty_name(self):
        data = {'status': 'Ready'}
        serializer = ChargePointSerializer(data=data)
        assert not serializer.is_valid()

    def test_will_raise_validation_error_if_empty_status(self):
        data = {'name': 'chargepoint'}
        serializer = ChargePointSerializer(data=data)
        assert not serializer.is_valid()