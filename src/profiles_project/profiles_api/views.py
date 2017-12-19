from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View."""

    def get(self, request, format=None):
        """Return list of APIView features."""

        api_view = [
            'Use HTTP methods as functions(get, post, patch, put, delete)'
        ]

        return Response({
                         'message':'Hello!',
                         'api_view':api_view,
                         })
