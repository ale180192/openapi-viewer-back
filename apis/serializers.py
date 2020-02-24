from rest_framework import serializers

from apis.models import ApiModel

class ApiSerializer(serializers.ModelSerializer):

    class Meta:
        model = ApiModel
        fields = ['name', 'description']
