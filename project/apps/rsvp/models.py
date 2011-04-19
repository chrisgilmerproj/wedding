from django.contrib.auth.models import User
from django.contrib.localflavor.us.models import USStateField
from django.contrib.localflavor.us.us_states import US_STATES
from django.db import models
from django.db.models.signals import post_save

class Group(models.Model):
	""" Guests are invited in groups """

	RESPONSE_CHOICES = (
		(0,'No Response'),
		(1,'Attending'),
		(2,'Not Attending'),
	)
	PARTY_CHOICES = (
		('B','Bride'),
		('G','Groom'),
	)

	name     = models.CharField(max_length=80)
	response = models.IntegerField(choices=RESPONSE_CHOICES, default=0)
	party    = models.CharField(max_length=1, choices=PARTY_CHOICES, blank=True, null=True)
	
	# Contact Information
	email    = models.EmailField(blank=True, null=True)
	phone    = models.CharField(max_length=15, blank=True, null=True)
	address  = models.CharField(max_length=80, blank=True, null=True)
	city     = models.CharField(max_length=80, blank=True, null=True)
	state    = USStateField(choices=US_STATES, blank=True, null=True)
	zipcode  = models.CharField(max_length=10, blank=True, null=True)

	# Admin Only
	number_guests        = models.PositiveSmallIntegerField(default=1)
	updated              = models.DateTimeField(auto_now=True)

	announcement_required = models.BooleanField()
	announcement_sent     = models.DateField(blank=True,null=True)
	
	invitation_required  = models.BooleanField()
	invitation_sent      = models.DateField(blank=True,null=True)

	thank_you_required   = models.BooleanField()
	thank_you_sent       = models.DateField(blank=True,null=True)
	gift_received        = models.TextField(blank=True,null=True)

	def __unicode__(self):
		return self.name

	def save(self,*args,**kwargs):
		if self.invitation_required:
			self.announcement_required = True
		if self.gift_received:
			self.thank_you_required = True
		super(Group,self).save(*args,**kwargs)

class Guest(models.Model):
	""" Capture information about each guest """

	MEAL_CHOICES = (
		('M','Meat'),
		('F','Fish'),
		('V','Vegetarian'),
	)

	group      = models.ForeignKey(Group)
	first_name = models.CharField(max_length=30)
	last_name  = models.CharField(max_length=30)
	meal       = models.CharField(max_length=1, choices=MEAL_CHOICES, blank=True, null=True)

	def __unicode__(self):
		return u"%s %s" % (self.first_name,self.last_name)

	class Meta:
		ordering = ('last_name','first_name',)

