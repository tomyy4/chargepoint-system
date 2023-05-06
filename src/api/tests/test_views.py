from datetime import datetime
from unittest.mock import patch

from django.test import TestCase
from django.urls import reverse
from model_bakery import baker

from core.models import ChargePoint


class TestDeleteChargePointView(TestCase):
    def test_charge_point_delete_view(self):
        charge_point = baker.make(ChargePoint, pk=1)
        response = self.client.delete(reverse('charge_point_delete', kwargs={'pk': charge_point.pk}))
        result = response.json()
        assert response.status_code == 200
        assert result.get('success') == 'Charge point set as deleted'

    def test_charge_point_delete_view_will_raise_404_if_charge_point_does_not_exist(self):
        baker.make(ChargePoint, pk=1)
        response = self.client.delete(reverse('charge_point_delete', kwargs={'pk': 2}))
        assert response.status_code == 404


class TestChargeSerializerListView(TestCase):
    def test_charge_point_list_view(self):
        baker.make(ChargePoint, _quantity=3)
        response = self.client.get(reverse('charge_point_list'))
        result = response.json()
        assert len(result) == 3

    def test_charge_point_list_view_wont_list_deleted_at_charge_points(self):
        baker.make(ChargePoint, _quantity=3)
        baker.make(ChargePoint, deleted_at=datetime.now())
        response = self.client.get(reverse('charge_point_list'))
        result = response.json()
        assert len(result) == 3

    @patch('api.views.ChargePointService')
    def test_charge_point_list_view_will_call_service_get_all_charge_points(self, mock_service):
        self.client.get(reverse('charge_point_list'))
        mock_service.get_all_charge_points.assert_called_once()


class TestChargePointDetailView(TestCase):
    def test_charge_point_detail_view(self):
        charge_point = baker.make(ChargePoint, pk=1, name='first charge point')
        response = self.client.get(reverse('charge_point_detail', kwargs={'pk': charge_point.pk}))
        result = response.json()
        assert result.get('name') == charge_point.name
        assert result.get('status') == charge_point.status

    def test_charge_point_detail_view_will_raise_404_if_charge_point_does_not_exist(self):
        baker.make(ChargePoint, pk=1, name='first charge point')
        response = self.client.get(reverse('charge_point_detail', kwargs={'pk': 2}))
        assert response.status_code == 404


class CreateChargePointView(TestCase):
    def test_charge_point_create_view(self):
        data = {'name': 'chargepoint', 'status': 'Ready'}
        response = self.client.post(reverse('charge_point_create'), data=data)
        self.assertEquals(response.status_code, 201)

    def test_charge_point_create_returns_400_if_invalid_status(self):
        data = {'name': 'chargepoint', 'status': 'Pending'}
        response = self.client.post(reverse('charge_point_create'), data=data)
        assert response.status_code == 400

    @patch('api.views.CreateChargePointSerializer')
    def test_assert_create_serializer_used(self, mock_serializer):
        data = {'name': 'chargepoint', 'status': 'Ready'}
        self.client.post(reverse('charge_point_create'), data=data)
        mock_serializer.assert_called_once()

    @patch('api.views.ChargePointService')
    def test_charge_point_create_view_will_call_service_create_charge_point(self, mock_service):
        data = {'name': 'chargepoint', 'status': 'Ready'}
        self.client.post(reverse('charge_point_create'), data=data)
        mock_service.create_charge_point.assert_called_once()
