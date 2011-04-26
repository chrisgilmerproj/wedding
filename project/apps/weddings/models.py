from datetime import datetime

from django.contrib.localflavor.us.models import USStateField
from django.contrib.localflavor.us.us_states import US_STATES
from django.db import models

class Wedding(models.Model):

	featured          = models.BooleanField(default=True)
	contact_phone     = models.CharField(max_length=15,blank=True)
	contact_email     = models.EmailField(blank=True)

	bride             = models.CharField(max_length=80,blank=True)
	bride_parents     = models.CharField(max_length=80,blank=True)
	groom             = models.CharField(max_length=80,blank=True)
	groom_parents     = models.CharField(max_length=80,blank=True)

	def __unicode__(self):
		return '%s and %s Wedding' % (self.bride,self.groom)
	
	def save(self,*args,**kwargs):
		super(Wedding,self).save(*args,**kwargs)
		if self.featured:
			for wedding in Wedding.objects.exclude(id=self.id):
				wedding.featured=False,
				wedding.save()

class Event(models.Model):

	wedding  = models.ForeignKey(Wedding)
	name     = models.CharField(max_length=80)
	slug     = models.SlugField()
	date     = models.DateTimeField(blank=True, null=True)

	# Contact Information
	venue    = models.CharField(max_length=80, blank=True, null=True)
	email    = models.EmailField(blank=True, null=True)
	phone    = models.CharField(max_length=15, blank=True, null=True)
	address  = models.CharField(max_length=80, blank=True, null=True)
	city     = models.CharField(max_length=80, blank=True, null=True)
	state    = USStateField(choices=US_STATES, blank=True, null=True)
	zipcode  = models.CharField(max_length=10, blank=True, null=True)
	about    = models.TextField(blank=True, null=True)
	
	def __unicode__(self):
		return '%s: %s' % (self.wedding,self.name)

	def days_remaining(self):
		return (self.date-datetime.now()).days

	class Meta:
		ordering = ('date',)
