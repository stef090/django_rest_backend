from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status


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
            message = 'Hello {name}'.format(name=name)
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """
        Updates an object.
        """
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """
        Updates only the provided fields.
        """
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """
        Deletes an object.
        """
        return Response({'method':'DELETE'})
