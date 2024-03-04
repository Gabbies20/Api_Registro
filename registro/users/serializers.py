from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['username', 'correo_electronico', 'pais', 'password']

    def create(self, validated_data):
        usuario = Usuario.objects.create_user(
            username=validated_data['username'],
            correo_electronico=validated_data['correo_electronico'],
            pais=validated_data.get('pais'),
            password=validated_data['password']
        )
        return usuario


"""
        {
    "nombre": "Ejemplo",
    "apellidos": "Apellido",
    "correo_electronico": "ejemplo@example.com",
    "pais": "Ejemplo",
    "password1": "contraseña123",
    "password2": "contraseña123"
}

"""