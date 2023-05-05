from datetime import datetime

from django.core.exceptions import ValidationError
from django.test import TestCase
from model_bakery import baker

from core.models import ChargePoint
from core.services import ChargePointService


class TestChargePointService(TestCase):
    def test_get_all_charge_points(self):
        baker.make(ChargePoint)
        self.assertEquals(len(ChargePointService.get_all_charge_points()), 1)

    def test_get_all_charge_points_wont_return_deleted_at_charge_points(self):
        baker.make(ChargePoint, deleted_at=datetime.now())
        self.assertEquals(len(ChargePointService.get_all_charge_points()), 0)

    def test_get_charge_point_by_id(self):
        charge_point = baker.make(ChargePoint, pk=1)
        self.assertEquals(charge_point, ChargePointService.get_charge_point(charge_point_id=1))

    def test_delete_charge_point_will_set_deleted_at(self):
        charge_point = baker.make(ChargePoint, pk=1)
        ChargePointService.delete_charge_point(charge_point_id=1)
        charge = ChargePointService.get_charge_point(charge_point_id=charge_point.pk)
        self.assertIsNotNone(charge.deleted_at)

    def test_create_charge_point(self):
        ChargePointService.create_charge_point(name='first chargepoint', status='Ready')
        self.assertEquals(len(ChargePointService.get_all_charge_points()), 1)

    def test_create_charge_point_will_raise_validation_error_if_invalid_status(self):
        with self.assertRaises(ValidationError):
            ChargePointService.create_charge_point(name='first chargepoint', status='Wrong')

    def test_create_charge_point_will_raise_validation_error_if_not_unique_name(self):
        baker.make(ChargePoint, pk=1, name='first chargepoint')
        with self.assertRaises(ValidationError):
            ChargePointService.create_charge_point(name='first chargepoint', status='Ready')

    def test_update_charge_point_status(self):
        charge_point = baker.make(ChargePoint, pk=1, name='first chargepoint', status='Ready')
        ChargePointService.update_charge_point(charge_point_id=charge_point.pk, status='Waiting')
        self.assertEquals(charge_point.status, 'Ready')

    def test_wont_update_charge_point_with_invalid_status(self):
        charge_point = baker.make(ChargePoint, pk=1, name='first chargepoint', status='Ready')
        with self.assertRaises(ValidationError):
            ChargePointService.update_charge_point(charge_point_id=charge_point.pk, status='Fake')