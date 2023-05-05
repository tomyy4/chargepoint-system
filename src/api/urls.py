from django.urls import path

from api.views import home_view

urlpatterns = [
    path('home/', home_view, name='home'),
]