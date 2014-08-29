from django.db import models
from django.contrib.auth.models import User

#Model for State
class Province(models.Model):
    name = models.CharField(max_length=64, null=False)

    #Include model into same app
    class Meta:
        app_label = 'memberships'

    def __unicode__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=64, null=False)

    class Meta:
        app_label = 'memberships'

    def __unicode__(self):
        return self.name

class ShippingAddress(models.Model):

    #Additional attributes for user
    userId = models.ForeignKey(User)
    address1 = models.CharField(max_length=128)
    address2 = models.CharField(max_length=128, null=True)
    city = models.CharField(max_length=64)
    provinceId = models.ForeignKey(Province)
    postalCode = models.IntegerField(default=0)
    countryId = models.ForeignKey(Country)

    class Meta:
        app_label = 'memberships'
    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.address1

class BillingAddress(models.Model):

    #Additional attributes for user
    userId = models.OneToOneField(User, primary_key=True)
    address1 = models.CharField(max_length=128)
    address2 = models.CharField(max_length=128, null=True)
    city = models.CharField(max_length=64)
    provinceId = models.ForeignKey(Province)
    postalCode = models.IntegerField(default=0)
    countryId = models.ForeignKey(Country)

    #Include model into same app
    class Meta:
        app_label = 'memberships'

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.address1

