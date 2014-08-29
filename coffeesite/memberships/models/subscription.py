from django.db import models
from django.contrib.auth.models import User
from memberships.models import BillingAddress, ShippingAddress

class GrindType(models.Model):
    type = models.CharField(max_length=64)
    isActive = models.BooleanField(default=True)

    #Include model into same app
    class Meta:
        app_label = 'memberships'
    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.type

class SubscriptionType(models.Model):
    type = models.CharField(max_length=64)

    #Include model into same app
    class Meta:
        app_label = 'memberships'
    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.type

class SubscriptionPreferences(models.Model):
    userId = models.OneToOneField(User, primary_key=True)
    grindType = models.ForeignKey(GrindType)
    isSubPaused = models.BooleanField(default=False)
    subPauseDate = models.DateField()
    subStartDate = models.DateField()
    subEndDate = models.DateField()
    subType = models.ForeignKey(SubscriptionType)
    shippingAddress = models.ForeignKey(ShippingAddress)
    billingAddress = models.OneToOneField(BillingAddress)

    class Meta:
        app_label = 'memberships'

     # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.userId