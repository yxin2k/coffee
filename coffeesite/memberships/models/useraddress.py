from django.db import models
from django.contrib.auth.models import User

class Address(models.Model):

    #Additional attributes for user
    address1 = models.CharField(max_length=128)
    address2 = models.CharField(max_length=128, null=True)
    city = models.CharField(max_length=64)
    provinceId = models.ForeignKey(Province)
    postalCode = models.IntegerField(default=0)
    countryId = models.ForeignKey(Country)
    refId = models.ForeignKey()

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.address1

#Model for State
class Province(models.Model):
    name = models.CharField(max_length=64, null=False)

    def __unicode__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=64, null=False)

    def __unicode__(self):
        return self.name

class ShippingAddresses(models.Model):

    userId = models.ForeignKey(User)

    def __unicode__(self):
        return self.userId.name

class BillingAddress(models.Model):

    #Additional attributes for user
    userId = models.ForeignKey(User)
    address1 = models.CharField(max_length=128)
    address2 = models.CharField(max_length=128, null=True)
    city = models.CharField(max_length=64)
    provinceId = models.ForeignKey(Province)
    postalCode = models.IntegerField(default=0)
    countryId = models.ForeignKey(Country)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.address1


class Meta:
    app_label = 'memberships'