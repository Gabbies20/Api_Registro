from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from .models import Usuario
from .serializers import UsuarioSerializer

@api_view(['POST'])
def registro_usuario(request):
    if request.method == 'POST':
        print("Recibida solicitud de registro de usuario:", request.data)  # Imprime los datos recibidos en la solicitud
        username = request.data.get('username')
        if Usuario.objects.filter(username=username).exists():
            # El nombre de usuario ya está en uso
            print("Error: El nombre de usuario ya está en uso")
            return Response({'error': 'El nombre de usuario ya está en uso'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            # Crea el nuevo usuario
            serializer = UsuarioSerializer(data=request.data)
            if serializer.is_valid():
                usuario = serializer.save()
                print("Usuario registrado exitosamente:", serializer.data)  # Imprime los datos del usuario registrado
                return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
            print("Error en la validación del serializador:", serializer.errors)  # Imprime los errores de validación del serializador
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def lista_usuarios(request):
    if request.method == 'GET':
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)


# class UsuarioRegistro(APIView):
#     def post(self, request):
#         serializer = UsuarioSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)