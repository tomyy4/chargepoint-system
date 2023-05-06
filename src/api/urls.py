from django.urls import path

from api.views import ChargePointList, ChargePointDetail, ChargePointDelete, ChargePointCreate

urlpatterns = [
    path('chargepoint/', ChargePointList.as_view(), name='charge_point_list'),
    path('chargepoint/create/', ChargePointCreate.as_view(), name='charge_point_create'),
    path('chargepoint/<int:pk>/', ChargePointDetail.as_view(), name='charge_point_detail'),
    path('chargepoint/<int:pk>/delete/', ChargePointDelete.as_view(), name='charge_point_delete'),
]