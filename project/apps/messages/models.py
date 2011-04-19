from django.db import models

class Message(models.Model):

	text = models.TextField()
	name = models.CharField(max_length=80)

	def __unicode__(self):
		return self.name

