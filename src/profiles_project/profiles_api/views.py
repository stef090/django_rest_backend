from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers


class HelloApiView(APIView):
    """Test API View."""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return list of APIView features."""

        api_view = [
            'Use HTTP methods as functions(get, post, patch, put, delete)'
        ]

        return Response({
                         'message':'Hello!',
                         'api_view':api_view,
                         })

    def post(self, request):
        """Create a hello message with name."""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {name}'.format{name=name}
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)
