
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer

@api_view(['GET'])
@permission_classes([AllowAny])
def get_user_detail(request, id):
    user = User.objects.get(pk=id)
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)