from rest_framework import serializers
from ..models import Shareholder
from .fie_serializer import FieSerializer
from .physical_serializer import PhysicalSerializer


class ShareholderSerializer(serializers.Serializer):
    class Meta:
        model = Shareholder
        fields = '__all__'

    def to_representation(self, instance):
        if instance.is_fie():
            return FieSerializer(instance).data
        elif instance.is_physical():
            return PhysicalSerializer(instance).data
        return super().to_representation(instance)
