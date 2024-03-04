from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']  # Define los campos que deseas serializar
        extra_kwargs = {'password': {'write_only': True}}  # Asegúrate de que la contraseña no se muestre al serializar


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']  # Incluye los campos que deseas mostrar en la API