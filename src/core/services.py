from datetime import datetime

from django.core.exceptions import ValidationError

from core.models import ChargePoint, Status


class ChargePointService:

    @staticmethod
    def get_all_charge_points():
        return ChargePoint.objects.filter(deleted_at__isnull=True)

    @staticmethod
    def get_charge_point(charge_point_id):
        return ChargePoint.objects.get(pk=charge_point_id)

    @staticmethod
    def create_charge_point(name=None):
        charge_point = ChargePoint.objects.filter(name=name)

        if charge_point.exists():
            raise ValidationError('A ChargePoint with that name exists')

        charge_point = ChargePoint.objects.create(name=name)
        return charge_point

    @staticmethod
    def update_charge_point(charge_point_id, name=None, status=None):
        charge_point = ChargePoint.objects.get(pk=charge_point_id)

        if name:
            charge_point.name = name

        if status:
            available_status = [s.value for s in Status]
            if status not in available_status:
                raise ValidationError(f'Status {status} is not a valid option')

        charge_point.status = status

        charge_point.save()

    @staticmethod
    def delete_charge_point(charge_point_id):
        charge_point = ChargePoint.objects.get(pk=charge_point_id)
        charge_point.deleted_at = datetime.now()
        charge_point.save()

