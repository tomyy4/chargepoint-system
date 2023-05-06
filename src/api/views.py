from django.core.exceptions import ValidationError
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from api.serializers import ChargePointSerializer, CreateChargePointSerializer, UpdateChargePointSerializer
from core.models import ChargePoint
from core.services import ChargePointService


class ChargePointList(APIView):
    def get(self, request):
        charge_points = ChargePointService.get_all_charge_points()
        serializer = ChargePointSerializer(charge_points, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ChargePointDetail(APIView):
    def get(self, request, pk):
        try:
            charge_point = ChargePointService.get_charge_point(charge_point_id=pk)
        except ChargePoint.DoesNotExist:
            raise Http404

        serializer = ChargePointSerializer(instance=charge_point, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ChargePointCreate(APIView):
    http_method_names = ['post', ]

    def post(self, request, format=None):
        serializer = CreateChargePointSerializer(data=request.data)

        if serializer.is_valid():
            try:
                ChargePointService.create_charge_point(
                    name=request.POST.get('name'),
                    status=request.POST.get('status'))
                return Response(status=status.HTTP_201_CREATED)
            except ValidationError as error:
                return Response({'error': str(error)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChargePointEdit(APIView):
    http_method_names = ['put', ]

    def put(self, request, pk, format=None):
        serializer = UpdateChargePointSerializer(data=request.data)

        if serializer.is_valid():
            try:
                ChargePointService.update_charge_point(
                    charge_point_id=pk,
                    name=request.data.get('name'),
                    status=request.data.get('status'))
                return Response(status=status.HTTP_200_OK)
            except ValidationError as error:
                return Response({'error': str(error)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChargePointDelete(APIView):
    http_method_names = ['delete', ]

    def delete(self, request, pk):
        try:
            ChargePointService.delete_charge_point(charge_point_id=pk)
        except ChargePoint.DoesNotExist:
            raise Http404

        return Response({'success': 'Charge point set as deleted'}, status=status.HTTP_200_OK)