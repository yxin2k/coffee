from django.db import models

class ContentType(models.Model):

    name = models.CharField(max_length=128)

    #Include model into same app
    class Meta:
        app_label = 'communications'

    def __unicode__(self):
        return self.name

class Submissions(models.Model):

    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=254)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    contentType = models.ForeignKey(ContentType)

    #Include model into same app
    class Meta:
        app_label = 'communications'

    def __unicode__(self):
        return self.name