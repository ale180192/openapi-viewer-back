from rest_framework import serializers

from apis.models import Api

class ApiSerializer(serializers.ModelSerializer):

    class Meta:
        model = Api
        fields = ['name', 'description']
