from django.contrib import admin
from guests.models import Guest

class GuestAdmin(admin.ModelAdmin):
	list_display = ['user','phone','meal','party','position',]

admin.site.register(Guest,GuestAdmin)
