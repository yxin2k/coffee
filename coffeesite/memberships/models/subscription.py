from django.db import models
from django.contrib.auth.models import User
from memberships.models import BillingAddress, ShippingAddresses

class GrindType(models.Model):
    type = models.CharField(max_length=64)
    isActive = models.BooleanField(default=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.type

class SubscriptionType(models.Model):
    type = models.CharField(max_length=64)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.type

class SubscriptionPreferences(models.Model):
    userId = models.ForeignKey(User)
    grindType = models.ForeignKey(GrindType)
    isSubPaused = models.BooleanField(default=False)
    subPauseDate = models.DateField()
    subStartDate = models.DateField()
    subEndDate = models.DateField()
    subType = models.ForeignKey(SubscriptionType)
    shippingAddress = models.ForeignKey(ShippingAddresses)
    BillingAddress = models.ForeignKey(BillingAddress.userId)

class Meta:
    app_label = 'memberships'