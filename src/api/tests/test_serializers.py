from django.test import TestCase

from api.serializers import CreateChargePointSerializer, UpdateChargePointSerializer


class TestCreateChargePointSerializer(TestCase):
    def test_with_both_fields(self):
        data = {'name': 'chargepoint', 'status': 'Ready'}
        serializer = CreateChargePointSerializer(data=data)
        assert serializer.is_valid()

    def test_will_raise_validation_error_if_empty_name(self):
        data = {'status': 'Ready'}
        serializer = CreateChargePointSerializer(data=data)
        assert not serializer.is_valid()

    def test_will_raise_validation_error_if_empty_status(self):
        data = {'name': 'chargepoint'}
        serializer = CreateChargePointSerializer(data=data)
        assert not serializer.is_valid()


class TestUpdateChargePointSerializer(TestCase):
    def test_with_both_fields(self):
        data = {'name': 'chargepoint', 'status': 'Ready'}
        serializer = UpdateChargePointSerializer(data=data)
        assert serializer.is_valid()

    def test_with_name_and_not_status(self):
        data = {'name': 'chargepoint'}

        serializer = UpdateChargePointSerializer(data=data)
        assert serializer.is_valid()

    def test_with_status_and_not_name(self):
        data = {'status': 'Ready'}
        serializer = UpdateChargePointSerializer(data=data)
        assert serializer.is_valid()

    def test_will_raise_error_if_all_fields_are_empty(self):
        serializer = UpdateChargePointSerializer(data={})
        assert not serializer.is_valid()
