from django.db import models
from django_extensions.db.models import TimeStampedModel
from django_extensions.db.fields import AutoSlugField


class Region(models.Model):
    name = models.CharField(max_length=255)

class Country(models.Model):
    name = models.CharField(max_length=255)
    region = models.ForeignKey(Region, on_delete=models.RESTRICT)

class City(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.RESTRICT)

class Gym(TimeStampedModel, models.Model):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name')
    city = models.ForeignKey(City, on_delete=models.RESTRICT)

    website = models.URLField(blank=True)
    photo = models.URLField(blank=True)

    status = models.BooleanField()
    photo_version = models.BooleanField()
    ready_to_link = models.BooleanField()
    ordernum = models.IntegerField()
    bad_standing = models.BooleanField()
    zip = models.CharField(blank=True, max_length=15)
    country_short_code = models.CharField(max_length=15)
    address = models.TextField(blank=True)
    lat = models.TextField(blank=True)
    lon = models.TextField(blank=True)
    aid = models.IntegerField()
    org_type = models.CharField(blank=True, max_length=255)
    effective_date = models.DateTimeField()
    active = models.BooleanField()
    show_on_map = models.BooleanField()
    kids = models.BooleanField()
    name_search = models.CharField(blank=True, max_length=255)
    state_code = models.CharField(blank=True, max_length=15)
    full_state = models.CharField(blank=True, max_length=255)


