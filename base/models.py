from django.db import models
from django.urls import reverse

# Create your models here.

class Package(models.Model):
    name = models.TextField(unique = True)
    human_description = models.TextField(blank=True)
    machine_description = models.TextField(blank=True)
    main_prog_language = models.TextField(blank=True)
    supercategory = models.TextField(blank=True)
    category = models.TextField(blank=True)
    subcategory = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.__str__()

    def get_absolute_url(self):
        return reverse('package-view', kwargs={'pk': self.id})

    class Meta:
        ordering = ['name']



class PackageTag(models.Model):
    key = models.TextField()
    value = models.TextField()
    package = models.ForeignKey(Package, blank=True, null=True, related_name='packagetag_package', on_delete=models.CASCADE, )

    def __str__(self):
        return ' '.join([self.key, self.value])

    def __unicode__(self):
        return self.__str__()

    def get_absolute_url(self):
        return reverse('packagetag-view', kwargs={'pk': self.id})

    class Meta:
        ordering = ['key', 'value']
        unique_together = ('key', 'value', 'package')



class Edition(models.Model):
    name = models.TextField(unique = True)
    human_description = models.TextField(blank=True)
    machine_description = models.TextField(blank=True)
    edition_number = models.TextField(blank=True)
    package = models.ForeignKey(Package, blank=True, null=True, related_name='edition_package', on_delete=models.CASCADE,)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.__str__()

    def get_absolute_url(self):
        return reverse('edition-view', kwargs={'pk': self.id})

    class Meta:
        ordering = ['name']


class Resource(models.Model):
    text = models.TextField(unique = True)
    human_description = models.TextField(blank=True)
    machine_description = models.TextField(blank=True)
    scheme = models.TextField(blank=True)
    host = models.TextField(blank=True)
    full_path = models.TextField(blank=True)
    dirname = models.TextField(blank=True)
    basename = models.TextField(blank=True)
    supercollection = models.TextField(blank=True)
    collection = models.TextField(blank=True)
    subcollection = models.TextField(blank=True)
    is_installation = models.BooleanField(default=False)
    is_source = models.BooleanField(default=False)
    edition = models.ForeignKey(Edition, blank=True, null=True, related_name='resource_edition', on_delete=models.CASCADE,)

    def __str__(self):
        return self.text

    def __unicode__(self):
        return self.__str__()

    def get_absolute_url(self):
        return reverse('resource-view', kwargs={'pk': self.id})

    class Meta:
        ordering = ['text']