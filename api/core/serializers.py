from rest_framework import serializers

from .models import LogModel

class ParseSerializer(serializers.ModelSerializer):
    """
    Serializador de log.
    """
    class Meta:
        model = LogModel
        depth = 1
        fields = [
            'url'
            ]


class LogSerializer(serializers.ModelSerializer):
    """
    Serializador de log.
    """
    class Meta:
        model = LogModel
        depth = 1
        fields = [
            'url',
            'success',
            'timestamp'
            ]
