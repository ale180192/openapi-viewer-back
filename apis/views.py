from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from apis.serializers import ApiSerializer
from apis.models import Api
from apis.filters import ApiFilter

class ApiListView(ListCreateAPIView):

    serializer_class = ApiSerializer
    queryset = Api.objects.all()
    filterset_class = ApiFilter
    
