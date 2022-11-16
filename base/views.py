from base.serializers import *
from rest_framework.response import Response
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
        'packagetags': reverse('api-packagetag', request=request),
        'editions': reverse('api-edition', request=request),
        'resources': reverse('api-resource', request=request),
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
class ApiPackageTag(viewsets.ModelViewSet):
    """
    API endpoint that represents a list of objects.
    """
    queryset = PackageTag.objects.all()
    serializer_class = PackageTagSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields=('key', 'value')
    search_fields=('key', 'value')


@authentication_classes((SessionAuthentication, BasicAuthentication, TokenAuthentication,))
@permission_classes((IsAuthenticated,))
class ApiEdition(viewsets.ModelViewSet):
    """
    API endpoint that represents a list of objects.
    """
    queryset = Edition.objects.all()
    serializer_class = EditionSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields=('name',)
    search_fields=('name',)


@authentication_classes((SessionAuthentication, BasicAuthentication, TokenAuthentication,))
@permission_classes((IsAuthenticated,))
class ApiResource(viewsets.ModelViewSet):
    """
    API endpoint that represents a list of objects.
    """
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields=('text',)
    search_fields=('text',)
