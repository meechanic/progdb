from django.contrib import admin
from import_export import resources
from base.models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class PackageResource(resources.ModelResource):

    class Meta:
        model = Package


class EditionResource(resources.ModelResource):

    class Meta:
        model = Edition


class ResourceResource(resources.ModelResource):

    class Meta:
        model = Resource


@admin.register(Package)
class PackageAdmin(ImportExportModelAdmin):
    resource_class = PackageResource


@admin.register(Edition)
class EditionAdmin(ImportExportModelAdmin):
    resource_class = EditionResource


@admin.register(Resource)
class ResourceAdmin(ImportExportModelAdmin):
    resource_class = ResourceResource
