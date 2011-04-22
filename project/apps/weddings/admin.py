from django.contrib import admin
from weddings.models import Wedding, Event

class WeddingAdmin(admin.ModelAdmin):
	list_display = ['bride','groom','contact_phone','contact_email',]

admin.site.register(Wedding,WeddingAdmin)

class EventAdmin(admin.ModelAdmin):
	list_display = ['wedding','name','date','venue',]
	prepopulated_fields = {"slug": ("name",)}

admin.site.register(Event,EventAdmin)
