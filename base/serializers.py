from base.models import *
from rest_framework import serializers


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'


class EditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edition
        fields = '__all__'


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'
