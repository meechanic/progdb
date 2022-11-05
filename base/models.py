from django.db import models
from django.urls import reverse

# Create your models here.

class Package(models.Model):
    name = models.TextField(unique = True)
    human_description = models.TextField()
    machine_description = models.TextField()
    main_prog_language = models.TextField()
    package_collection = models.TextField()

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.__str__()

    def get_absolute_url(self):
        return reverse('source-view', kwargs={'pk': self.id})

    class Meta:
        ordering = ['name']


class Replica(models.Model):
    name = models.TextField(unique = True)
    human_description = models.TextField()
    machine_description = models.TextField()
    is_main = models.TextField()
    is_installation = models.TextField()
    location = models.TextField()
    replica_collection = models.TextField()
    module = models.ForeignKey(Package, blank=True, null=True, related_name='replica_package', on_delete=models.CASCADE,)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.__str__()

    def get_absolute_url(self):
        return reverse('source-view', kwargs={'pk': self.id})

    class Meta:
        ordering = ['name']


class Module(models.Model):
    name = models.TextField(unique = True)
    human_description = models.TextField()
    machine_description = models.TextField()
    prog_language = models.TextField()
    location = models.TextField()
    sourcereplica_collection = models.TextField()
    module = models.ForeignKey(Package, blank=True, null=True, related_name='module_package', on_delete=models.CASCADE,)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.__str__()

    def get_absolute_url(self):
        return reverse('source-view', kwargs={'pk': self.id})

    class Meta:
        ordering = ['name']


class SourceReplica(models.Model):
    name = models.TextField(unique = True)
    human_description = models.TextField()
    machine_description = models.TextField()
    is_main = models.TextField()
    module = models.ForeignKey(Package, blank=True, null=True, related_name='sourcereplica_package', on_delete=models.CASCADE,)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.__str__()

    def get_absolute_url(self):
        return reverse('source-view', kwargs={'pk': self.id})

    class Meta:
        ordering = ['name']

class FSObject(models.Model):
    name = models.TextField(unique = True)
    human_description = models.TextField()
    machine_description = models.TextField()
    location = models.TextField()
    module = models.ForeignKey(Module, blank=True, null=True, related_name='fsobject_module', on_delete=models.CASCADE,)
    replica = models.ForeignKey(Replica, blank=True, null=True, related_name='fsobject_replica', on_delete=models.CASCADE,)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.__str__()

    def get_absolute_url(self):
        return reverse('source-view', kwargs={'pk': self.id})

    class Meta:
        ordering = ['name']
