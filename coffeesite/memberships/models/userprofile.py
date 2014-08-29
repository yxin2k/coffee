from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    #Link userprofile to Django User model
    user = models.OneToOneField(User)

    #Additional attributes for user
    date_created = models.DateField(auto_now_add=True)
    isSubscribed = models.BooleanField(default=True)
    isEmailOptIn = models.BooleanField(default=False)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

class Meta:
    app_label = 'memberships'