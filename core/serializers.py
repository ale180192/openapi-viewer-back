from rest_framework import serializers

from core.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id', 'first_name', 'last_name', 'username', 'email', 
            'is_active', 'is_staff', 'is_superuser', 'created_at', 'rol', 'groups', 'user_permissions'
        ]