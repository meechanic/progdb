"""progdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from rest_framework import routers
from base.views import *
from rest_framework.authtoken import views
from rest_framework.schemas import get_schema_view as get_schema_view_rf
from django.urls import path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

schema_view_rf = get_schema_view_rf(
    title="ProgDB",
    description="Open API for the infsources DB",
    version="1.0.0",
    public=True,
)

router = routers.DefaultRouter()
router.register(r'apipackage', ApiPackage)
router.register(r'apirepilca', ApiReplica)
router.register(r'apimodule', ApiModule)
router.register(r'apisourcereplica', ApiSourceReplica)
router.register(r'apifsobject', ApiFSObject)

admin.site.site_header = 'ProgDB'
admin.site.index_title = 'Administration'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    #url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    #url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    url(r'^openapi/$', schema_view_rf, name='openapi-schema'),
    url(r'', include(router.urls)),
]
