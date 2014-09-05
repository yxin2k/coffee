from django.db import models
from memberships.models import GrindType, SubscriptionType
from django.contrib.auth.models import User

class ActionType(models.Model):
    action = models.CharField(max_length=64)

    class Meta:
        app_label = 'memberships'

     # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.userId


class SubscriptionHistory(models.Model):
    userId = models.ForeignKey(User)
    actionType = models.ForeignKey(ActionType)
    date = models.DateTimeField(auto_now_add=True)
    notes = models.CharField(max_length=2000)
    subType = models.ForeignKey(SubscriptionType)
    grindType = models.ForeignKey(GrindType)
    price = models.DecimalField(max_digits=4, decimal_places=2)


    class Meta:
        app_label = 'memberships'

     # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.userId