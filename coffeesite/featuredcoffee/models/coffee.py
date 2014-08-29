from django.db import models

class Month(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        app_label = 'featuredcoffee'
    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.name

class Coffee(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    highlight_month = models.ForeignKey(Month)
    highlight_year = models.IntegerField(default=2015)
    origin = models.CharField(max_length=128)
    sort_number = models.IntegerField()

    class Meta:
        app_label = 'featuredcoffee'
    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.name