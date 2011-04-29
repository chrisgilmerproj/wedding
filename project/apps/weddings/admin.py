from django.contrib import admin
from django import forms
from easy_maps.widgets import AddressWithMapWidget
from weddings.models import Wedding, Event, Registry, Lodging

class EventInline(admin.StackedInline):
	extra = 0
	model = Event

class WeddingAdmin(admin.ModelAdmin):
	inlines = [EventInline,]
	list_display = ['bride','groom','contact_phone','contact_email','featured']

admin.site.register(Wedding,WeddingAdmin)

class EventAdmin(admin.ModelAdmin):
	list_display = ['wedding','name','date','venue',]
	
	class form(forms.ModelForm):
		class Meta:
			widgets = {
				'address': AddressWithMapWidget({'class': 'vTextField'})
			}

admin.site.register(Event,EventAdmin)

class RegistryAdmin(admin.ModelAdmin):
	list_display = ['wedding','name','url',]

admin.site.register(Registry,RegistryAdmin)

class LodgingAdmin(admin.ModelAdmin):
	list_display = ['wedding','name','email','phone']

	class form(forms.ModelForm):
		class Meta:
			widgets = {
				'address': AddressWithMapWidget({'class': 'vTextField'})
			}
	
admin.site.register(Lodging,LodgingAdmin)

