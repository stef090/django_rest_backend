from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """
    Serialize the name field.
    """

    name = serializers.CharField(max_length=10)
