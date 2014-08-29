from django.contrib import admin
from faqs.models import FaqsCategory
from faqs.models import Faqs

admin.site.register(Faqs)
admin.site.register(FaqsCategory)
