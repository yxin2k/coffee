from django.contrib import admin
from communications.models.feedbacks import Submissions
from communications.models.feedbacks import ContentType

admin.site.register(Submissions)
admin.site.register(ContentType)
