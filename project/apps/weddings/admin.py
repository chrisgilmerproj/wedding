from django.contrib import admin
from weddings.models import Wedding, Event

class EventInline(admin.StackedInline):
	extra = 0
	model = Event

class WeddingAdmin(admin.ModelAdmin):
	inlines = [EventInline,]
	list_display = ['bride','groom','contact_phone','contact_email','featured']

admin.site.register(Wedding,WeddingAdmin)

class EventAdmin(admin.ModelAdmin):
	list_display = ['wedding','name','date','venue',]
	prepopulated_fields = {"slug": ("name",)}

admin.site.register(Event,EventAdmin)
