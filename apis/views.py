from django.views import View
from django.http.response import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


from apis.serializers import ApiSerializer
from apis.models import Api
from apis.filters import ApiFilter
from .filter_backend import CustomFilterBackend

class ApiViewList(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        print('get myview')
        queryset = Api.objects.all()
        ser = ApiSerializer(data=queryset, many=True)
        print(ser)
        ser.is_valid()
        return Response(data=ser.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        print('data received is: ', data)
        ser = ApiSerializer(data=data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(data=ser.data, status=status.HTTP_201_CREATED)

class ApiViewDetail(APIView):

    def get(self, request, pk):
        try:
            api = Api.objects.get(pk=pk)
        except ObjectDoesNotExist as _:
            raise Http404
        ser = ApiSerializer(api)
        return Response(data=ser.data, status=status.HTTP_200_OK)

