from django.urls import path
from rest_framework import permissions

from api.views import ChargePointList, ChargePointDetail, ChargePointDelete, ChargePointCreate, ChargePointEdit

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny,],
)


urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('chargepoint/', ChargePointList.as_view(), name='charge_point_list'),
    path('chargepoint/create/', ChargePointCreate.as_view(), name='charge_point_create'),
    path('chargepoint/<int:pk>/update/', ChargePointEdit.as_view(), name='charge_point_edit'),
    path('chargepoint/<int:pk>/', ChargePointDetail.as_view(), name='charge_point_detail'),
    path('chargepoint/<int:pk>/delete/', ChargePointDelete.as_view(), name='charge_point_delete'),
]