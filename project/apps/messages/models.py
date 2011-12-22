from django.db import models


class Message(models.Model):

    text = models.TextField()
    name = models.CharField(max_length=80)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('-created', )
