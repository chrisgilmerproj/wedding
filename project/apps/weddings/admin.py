from django.contrib import admin
from weddings.models import Wedding, Event, Registry, Lodging

class EventInline(admin.StackedInline):
	extra = 0
	model = Event
	prepopulated_fields = {"slug": ("name",)}

class RegistryInline(admin.TabularInline):
	extra = 0
	model = Registry

class WeddingAdmin(admin.ModelAdmin):
	inlines = [EventInline,RegistryInline]
	list_display = ['bride','groom','contact_phone','contact_email','featured']

admin.site.register(Wedding,WeddingAdmin)

class EventAdmin(admin.ModelAdmin):
	list_display = ['wedding','name','date','venue',]
	prepopulated_fields = {"slug": ("name",)}

admin.site.register(Event,EventAdmin)

class RegistryAdmin(admin.ModelAdmin):
	list_display = ['wedding','name','url',]

admin.site.register(Registry,RegistryAdmin)

class LodgingAdmin(admin.ModelAdmin):
	list_display = ['wedding','name','email','phone']

admin.site.register(Lodging,LodgingAdmin)

