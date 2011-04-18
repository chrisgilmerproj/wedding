from django.contrib.auth.models import User
from django.contrib.localflavor.us.models import USStateField, USPostalCodeField
from django.contrib.localflavor.us.us_states import US_STATES
from django.db import models
from django.db.models.signals import post_save

class Guest(models.Model):
	""" This keeps information about guests """

	MEAL_CHOICES = (
		('M','Meat'),
		('F','Fish'),
		('V','Vegetarian'),
	)
	PARTY_CHOICES = (
		('B','Bride'),
		('G','Groom'),
	)
	POSITION_CHOICES = (
		('bride','Bride'),
		('groom','Groom'),
		('officiant','Officiant'),
		('best man','Best Man'),
		('groomsman 1','Groomsman 1'),
		('groomsman 2','Groomsman 2'),
		('groomsman 3','Groomsman 3'),
		('maid of honor','Maid of Honor'),
		('bridesmaid 1','Bridesmaid 1'),
		('bridesmaid 2','Bridesmaid 2'),
		('bridesmaid 3','Bridesmaid 3'),
		('bride father','Father of the Bride'),
		('bride mother','Mother of the Bride'),
		('groom father','Father of the Groom'),
		('groom mother','Mother of the Groom'),
		('usher 1','Usher 1'),
		('usher 2','Usher 2'),
	)
	MAIL_CHOICES = (
		('required','Required'),
		('written','Written'),
		('sent','Sent'),
	)

	user     = models.ForeignKey(User, unique=True)
	phone    = models.CharField(max_length=15, blank=True, null=True)
	address  = models.CharField(max_length=80, blank=True, null=True)
	city     = models.CharField(max_length=80, blank=True, null=True)
	state    = USStateField(choices=US_STATES)
	zipcode  = USPostalCodeField()
	meal     = models.CharField(max_length=1, choices=MEAL_CHOICES, blank=True, null=True)
	party    = models.CharField(max_length=1, choices=PARTY_CHOICES, blank=True, null=True)
	message  = models.TextField(blank=True, null=True)

	# Admin use only
	position = models.CharField(max_length=20, choices=POSITION_CHOICES, unique=True, blank=True, null=True)
	
	announcment_required = models.BooleanField()
	announcment_sent     = models.DateField(blank=True,null=True)
	
	invitation_required  = models.BooleanField()
	invitation_sent      = models.DateField(blank=True,null=True)

	thankyou_required    = models.BooleanField()
	thankyou_sent        = models.DateField(blank=True,null=True)
	gift_received        = models.TextField(blank=True,null=True)

	gift_required        = models.BooleanField()
	gift_sent            = models.DateField(blank=True,null=True)
	gift_given           = models.TextField(blank=True,null=True)

	def __unicode__(self):
		return self.user.get_full_name()
	
def create_profile(sender, instance=None, **kwargs):
	if instance is None: return
	profile, created = Guest.objects.get_or_create(user=instance)

post_save.connect(create_profile, sender=User)
