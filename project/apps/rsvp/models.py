import random
import sys

from django.contrib.localflavor.us.models import USStateField
from django.contrib.localflavor.us.us_states import US_STATES
from django.db import models
from django.core.mail import send_mass_mail


class Group(models.Model):
    """ Guests are invited in groups """

    RESPONSE_CHOICES = (
        (0, 'No Response'),
        (1, 'Attending'),
        (2, 'Not Attending'),
        (3, 'Ceremony Only'),
    )
    PARTY_CHOICES = (
        (0, 'Bride'),
        (1, 'Groom'),
    )

    name = models.CharField(max_length=80)
    response = models.IntegerField(choices=RESPONSE_CHOICES, default=0)
    party = models.IntegerField(choices=PARTY_CHOICES, default=0)
    code = models.CharField(max_length=6, editable=False)

    # Contact Information
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    address = models.CharField(max_length=80, blank=True, null=True)
    city = models.CharField(max_length=80, blank=True, null=True)
    state = USStateField(choices=US_STATES, blank=True, null=True)
    zipcode = models.CharField(max_length=10, blank=True, null=True)

    # Admin Only
    number_guests = models.PositiveSmallIntegerField(default=1)
    rehearsal_dinner = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)

    announcement_required = models.BooleanField()
    announcement_sent = models.DateField(blank=True, null=True)

    invitation_required = models.BooleanField()
    invitation_sent = models.DateField(blank=True, null=True)

    thank_you_required = models.BooleanField()
    thank_you_sent = models.DateField(blank=True, null=True)

    gift_received = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('apps.rsvp.views.rsvp_detail', (), {
            'code': self.code,
        })

    def save(self, *args, **kwargs):
        if self.invitation_required:
            self.announcement_required = True
        if self.gift_received:
            self.thank_you_required = True
        if not self.code:
            self.code = ''.join(random.sample('ABCDEFGHJKLMNPQRSTUVWXYZ23456789', 6))
        super(Group, self).save(*args, **kwargs)

    def full_address(self):
        return "%s %s, %s %s" % (self.address, self.city, self.state, self.zipcode)

    class Meta:
        ordering = ('name', )

    @classmethod
    def rsvp_reminder(cls):
        question = raw_input('Are you sure you want to send emails? ')
        if question.lower() not in ['y', 'yes']:
            sys.exit()

        mail_list = []
        subject = 'Chris and Megan RSVP Reminder'
        from_email = 'chris.gilmer@gmail.com'
        message_txt = """
Dear %(name)s,

You're getting this email because you haven't RSVPed to our
wedding yet.  That's okay; the deadline for us getting info
to the vendors isn't for a couple of weeks, but we really
would like to hear from you sooner rather than later so that
we can start planning accordingly.

You don't need your invitation to RSVP.  Instead you can
click the following link and RSVP on our website:

http://celebratechrisandmegan.com/rsvp/%(code)s/

Once there you can RSVP for each person in your group
individually and choose your meal option (red meat, fish, or
vegetarian).

The rest of the website holds useful info about the location
of the venue, etc, and will be updated as we get more
information ourselves

If you haven't responded because you couldn't figure out the
website, have lost your invitation, or any other reason,
please call us directly.

Megan at (415) 328-9245 or Chris at (303) 907-5277

Please get back to us by the end of April... If you don't,
we're going to pester you by phone until you respond.

Thanks,
Megan and Chris
"""

        for group in cls.objects.filter(response=0):
            recipient_list = [group.email]
            message = message_txt % ({'name': group.name,
                                      'code': group.code,
                                     })
            if group.invitation_sent:
                mail_list.append((subject, message, from_email, recipient_list))

        send_mass_mail(mail_list, fail_silently=False)


class Guest(models.Model):
    """ Capture information about each guest """

    MEAL_CHOICES = (
        (0, 'Meat'),
        (1, 'Fish'),
        (2, 'Veggie'),
    )

    group = models.ForeignKey(Group)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    child = models.BooleanField(default=False)
    meal = models.IntegerField(choices=MEAL_CHOICES, default=0)

    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)

    class Meta:
        ordering = ('last_name', 'first_name', )
