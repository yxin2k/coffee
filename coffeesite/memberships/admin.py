from django.contrib import admin
from memberships.models import UserProfile
from memberships.models import Province
from memberships.models import Country
from memberships.models import SubscriptionType
from memberships.models import GrindType
from memberships.models import ActionType

admin.site.register(UserProfile)
admin.site.register(Province)
admin.site.register(Country)
admin.site.register(SubscriptionType)
admin.site.register(GrindType)
admin.site.register(ActionType)