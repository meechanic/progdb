from django.contrib import admin

from import_export import resources
from base.models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class PackageResource(resources.ModelResource):

    class Meta:
        model = Package


class ReplicaResource(resources.ModelResource):

    class Meta:
        model = Replica


class ModuleResource(resources.ModelResource):

    class Meta:
        model = Module


class SourceReplicaResource(resources.ModelResource):

    class Meta:
        model = SourceReplica


class FSObjectResource(resources.ModelResource):

    class Meta:
        model = FSObject


@admin.register(Package)
class CategoryAdmin(ImportExportModelAdmin):
    resource_class = PackageResource


@admin.register(Replica)
class CategoryAdmin(ImportExportModelAdmin):
    resource_class = ReplicaResource


@admin.register(Module)
class CategoryAdmin(ImportExportModelAdmin):
    resource_class = ModuleResource


@admin.register(SourceReplica)
class CategoryAdmin(ImportExportModelAdmin):
    resource_class = SourceReplicaResource


@admin.register(FSObject)
class CategoryAdmin(ImportExportModelAdmin):
    resource_class = FSObjectResource
