from rest_framework import serializers

from apis.models import Api, ApiFake

class ApiSerializer(serializers.ModelSerializer):

    class Meta:
        model = Api
        fields = ['name', 'description', 'user']

class ApiFakeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ApiFake
        fields = ['name', 'description', 'id']
