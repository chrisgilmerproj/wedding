from django.db import models

class Wedding(models.Model):

	featured          = models.BooleanField(default=True)
	contact_phone     = models.CharField(max_length=15,blank=True)
	contact_email     = models.EmailField(blank=True)

	bride             = models.CharField(max_length=80,blank=True)
	bride_parents     = models.CharField(max_length=80,blank=True)
	groom             = models.CharField(max_length=80,blank=True)
	groom_parents     = models.CharField(max_length=80,blank=True)

	rehearsal_address = models.TextField(blank=True)
	rehearsal_dinner  = models.DateTimeField(blank=True,null=True)

	wedding_address   = models.TextField(blank=True)
	wedding_ceremony  = models.DateTimeField(blank=True,null=True)
	wedding_reception = models.DateTimeField(blank=True,null=True)

	def __unicode__(self):
		return '%s and %s Wedding' % (self.bride,self.groom)
	
	def save(self,*args,**kwargs):
		super(Wedding,self).save(*args,**kwargs)
		if self.featured:
			for wedding in Wedding.objects.exclude(id=self.id):
				wedding.featured=False,
				wedding.save()
		
