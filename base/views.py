from base.models import *
from base.serializers import *
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

# Create your views here.

@api_view(['GET'])
@authentication_classes((SessionAuthentication, BasicAuthentication, TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def api_root(request, format=None):
    """
    The entry endpoint of our API.
    """
    return Response({
        'packages': reverse('api-package', request=request),
        'replicas': reverse('api-replica', request=request),
        'modules': reverse('api-module', request=request),
        'sourcereplicas': reverse('api-sourcereplica', request=request),
        'fsobjects': reverse('api-fsobject', request=request),
    })


@authentication_classes((SessionAuthentication, BasicAuthentication, TokenAuthentication,))
@permission_classes((IsAuthenticated,))
class ApiPackage(viewsets.ModelViewSet):
    """
    API endpoint that represents a list of objects.
    """
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields=('name',)
    search_fields=('name',)


@authentication_classes((SessionAuthentication, BasicAuthentication, TokenAuthentication,))
@permission_classes((IsAuthenticated,))
class ApiReplica(viewsets.ModelViewSet):
    """
    API endpoint that represents a list of objects.
    """
    queryset = Replica.objects.all()
    serializer_class = ReplicaSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields=('name',)
    search_fields=('name',)


@authentication_classes((SessionAuthentication, BasicAuthentication, TokenAuthentication,))
@permission_classes((IsAuthenticated,))
class ApiModule(viewsets.ModelViewSet):
    """
    API endpoint that represents a list of objects.
    """
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields=('name',)
    search_fields=('name',)


@authentication_classes((SessionAuthentication, BasicAuthentication, TokenAuthentication,))
@permission_classes((IsAuthenticated,))
class ApiSourceReplica(viewsets.ModelViewSet):
    """
    API endpoint that represents a list of objects.
    """
    queryset = SourceReplica.objects.all()
    serializer_class = SourceReplicaSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields=('name',)
    search_fields=('name',)


@authentication_classes((SessionAuthentication, BasicAuthentication, TokenAuthentication,))
@permission_classes((IsAuthenticated,))
class ApiFSObject(viewsets.ModelViewSet):
    """
    API endpoint that represents a list of objects.
    """
    queryset = FSObject.objects.all()
    serializer_class = FSObjectSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields=('name',)
    search_fields=('name',)
