from base.models import *
from rest_framework import serializers


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'


class ReplicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Replica
        fields = '__all__'


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'


class SourceReplicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SourceReplica
        fields = '__all__'


class FSObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = FSObject
        fields = '__all__'
