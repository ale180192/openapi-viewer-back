from django.views import View
from django.http.response import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.sessions.backends import cache
from django.contrib.auth.middleware import AuthenticationMiddleware

from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication, SessionAuthentication

from apis.serializers import ApiSerializer, ApiFakeSerializer
from apis.models import Api, ApiFake
from apis.filters import ApiFilter
from .filter_backend import CustomFilterBackend

class ApiViewList(APIView):


    def get(self, request):
        queryset = Api.objects.all()
        ser = ApiSerializer(data=queryset, many=True)
        print(ser)
        ser.is_valid()
        return Response(data=ser.data, status=status.HTTP_200_OK)

    def post(self, request):
        print('post no fake ')
        data = request.data
        ser = ApiSerializer(data=data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(data=ser.data, status=status.HTTP_201_CREATED)

class ApiFakeViewList(APIView):


    def get(self, request):
        print('queryparams')
        print(request.query_params)
        queryset = ApiFake.objects.all()
        ser = ApiFakeSerializer(data=queryset, many=True)
        ser.is_valid()
        return Response(data={'items': ser.data, 'total': 10}, status=status.HTTP_200_OK)

    def post(self, request):
        print('post fake')
        data = request.data
        print(data)
        ser = ApiFakeSerializer(data=data)
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

class ApiFakeViewDetail(APIView):

    def get(self, request, pk):
        try:
            api = ApiFake.objects.get(pk=pk)
        except ObjectDoesNotExist as _:
            raise Http404
        ser = ApiFakeSerializer(api)
        return Response(data={'items': ser.data, 'total': 10}, status=status.HTTP_200_OK)
    
    def delete(self, request, pk):
        try:
            api = ApiFake.objects.get(pk=pk)
        except ObjectDoesNotExist as _:
            raise Http404
        api.delete()
        return Response(data=[], status=status.HTTP_204_NO_CONTENT)

class ApiSerializerPagination(ListCreateAPIView):
    queryset = ApiFake.objects.all()
    serializer_class = ApiFakeSerializer

    def list(self, request):
        print('request pagination')
        print(request.query_params)
        return super().list(request)