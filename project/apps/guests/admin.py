from django.contrib import admin
from guests.models import Group,Guest

class GuestInline(admin.TabularInline):
	model = Guest

class GuestAdmin(admin.ModelAdmin):
	list_display  = ['group','first_name','last_name',]
	raw_id_fields = ['group',]
	search_fields = ['first_name','last_name',]
admin.site.register(Guest,GuestAdmin)

class GroupAdmin(admin.ModelAdmin):
	fieldsets = (
		(None, {
			'fields': ('name','response','party',)
			}),
		('Contact Information', {
			'fields': ('email','phone','address',
				'city','state','zipcode',)
			}),
		('Admin Use Only', {
			'fields': ('number_guests',
				'announcement_required','announcement_sent',
				'invitation_required','invitation_sent',
				'thank_you_required','thank_you_sent',
				'gift_received',)
			}),
		)
	inlines       = [GuestInline,]
	list_display  = ['name','response','party','email',]
	search_fields = ['name','gift_received',]

admin.site.register(Group,GroupAdmin)

