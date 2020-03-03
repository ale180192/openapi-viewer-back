from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.views import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication

from core.serializers import UserSerializer
from core.models import User

class UsersApiViewList(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        queryset = User.objects.all()
        print(queryset)
        ser = UserSerializer(data=queryset, many=True)
        ser.is_valid()
        return Response(data=ser.data, status=status.HTTP_200_OK)

    def post(self, request):
        ser = UserSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(data=ser.data, status=status.HTTP_201_CREATED)

class ObtainBadAuthToken(APIView):

    def get(self, request):
        return Response(data={'token': 'tokeninvalidosoloparapruebas'})
