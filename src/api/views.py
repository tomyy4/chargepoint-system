from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def home_view(request):
    return Response({'foo': 'bar'})