from datetime import datetime
from django.db import models

def get_google_maps_url(address):
    url = 'http://maps.google.com/maps?q='
    return url + '+'.join(address.split())

class Wedding(models.Model):

    featured          = models.BooleanField(default=True)
    contact_phone     = models.CharField(max_length=15,blank=True)
    contact_email     = models.EmailField(blank=True)

    bride             = models.CharField(max_length=80,blank=True)
    bride_parents     = models.CharField(max_length=80,blank=True)
    groom             = models.CharField(max_length=80,blank=True)
    groom_parents     = models.CharField(max_length=80,blank=True)

    story             = models.TextField(blank=True)

    def __unicode__(self):
        return '%s and %s Wedding' % (self.bride,self.groom)
    
    def save(self,*args,**kwargs):
        super(Wedding,self).save(*args,**kwargs)
        if self.featured:
            for wedding in Wedding.objects.exclude(id=self.id):
                wedding.featured=False,
                wedding.save()

class EventType(models.Model):

    name     = models.CharField(max_length=80)
    slug     = models.SlugField()

    def __unicode__(self):
        return self.name

class Event(models.Model):

    wedding  = models.ForeignKey(Wedding)
    type     = models.ForeignKey(EventType)
    date     = models.DateTimeField(blank=True, null=True)

    # Contact Information
    venue    = models.CharField(max_length=80, blank=True, null=True)
    email    = models.EmailField(blank=True, null=True)
    phone    = models.CharField(max_length=15, blank=True, null=True)
    url      = models.URLField(max_length=200, blank=True, null=True)
    address  = models.CharField(max_length=200, blank=True, null=True)
    about    = models.TextField(blank=True, null=True)
    
    def __unicode__(self):
        return '%s: %s' % (self.wedding,self.type.name)

    def days_remaining(self):
        return (self.date-datetime.now()).days

    def google_maps(self):
        return get_google_maps_url(self.address)

    class Meta:
        ordering = ('date',)

class Registry(models.Model):

    wedding  = models.ForeignKey(Wedding)
    name     = models.CharField(max_length=80)
    url      = models.URLField(verify_exists=True)
    image    = models.URLField(verify_exists=True)

    def __unicode__(self):
        return '%s: %s' % (self.wedding,self.name)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'registries'

class Lodging(models.Model):

    wedding  = models.ForeignKey(Wedding)
    name     = models.CharField(max_length=80)

    # Contact Information
    email    = models.EmailField(blank=True, null=True)
    phone    = models.CharField(max_length=15, blank=True, null=True)
    url      = models.URLField(max_length=200, blank=True, null=True)
    address  = models.CharField(max_length=200, blank=True, null=True)
    about    = models.TextField(blank=True, null=True)
    
    def __unicode__(self):
        return '%s: %s' % (self.wedding,self.name)

    def google_maps(self):
        return get_google_maps_url(self.address)

    class Meta:
        ordering = ('name',)
        verbose_name = 'lodge'
        verbose_name_plural = 'lodges'

