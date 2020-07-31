from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from core import serializers
from apis import serializers as apis_serializers 
from core.models import User

class UsersApiViewList(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        queryset = User.objects.all()
        print(queryset)
        ser = serializers.UserSerializer(data=queryset, many=True)
        ser.is_valid()
        return Response(data=ser.data, status=status.HTTP_200_OK)

    def post(self, request):
        ser = serializers.UserSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(data=ser.data, status=status.HTTP_201_CREATED)

class ObtainBadAuthToken(APIView):

    def get(self, request):
        return Response(data={'token': 'tokeninvalidosoloparapruebas'})


test_param = openapi.Parameter('test', openapi.IN_QUERY, description="test manual param", type=openapi.TYPE_BOOLEAN)
user_response = openapi.Response('response description', serializers.UserSerializer)

@api_view(['GET'])
def test_api_view(request):
    return Response(data={'data': 'this is a function api_view'})


from drf_yasg.openapi import Schema, Response as OaResponse, TYPE_BOOLEAN 

schema = Schema(
    title='title schema',
    description='description schema',
    type='string',
    format='value format',
    enum=['enum1', 'enum2'],
    pattern='pattern'
)

error_schema = Schema(
    title='Error object',
    description='This is the error object',
    type='object',
    properties={
        'status': 404, 
        'error_code': Schema(
            title='Detail of error', 
            description='this field describe the error',
            type='str',
            enum=['NOT_FOUND_USER', 'NOT_FOUND_OBJECT']
        ),
        'detail': Schema(
            title='Detail of error', 
            description='this field describe the error',
            type='str'
        ),
    }
)

response_error_schema = Schema(
    title='title schema',
    description='description schema',
    type='object',
    properties={
        'ok': Schema(
            title="status' response", 
            description='this field describe the status of the response',
            type='boolean'
        ),
        'error': error_schema
    }
)



response = OaResponse(
    description="response's description",
    schema=response_error_schema,
    examples=None
)

response200 = OaResponse(
    description="response's description",
    schema=apis_serializers.ApiFakeSerializer,
    examples=None
)

@swagger_auto_schema(
    methods=['PATCH'], request_body=serializers.UserSerializer,
    responses={404: response, 201: response200})
@api_view(['PATCH'])
def test_api_view_detail(request):
    """
        This is a docstring
    """
    return Response(data={'data': 'this is a function api_view'})



