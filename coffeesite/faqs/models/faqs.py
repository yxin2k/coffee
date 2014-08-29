from django.db import models

class FaqsCategory(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        app_label = 'faqs'
    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.name

class Faqs(models.Model):
    #Link userprofile to Django User model
    category = models.ForeignKey(FaqsCategory)
    question = models.CharField(max_length=2000)
    answer = models.CharField(max_length=2000)

    class Meta:
        app_label = 'faqs'
    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.question