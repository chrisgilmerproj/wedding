from django.contrib import admin
from weddings.models import Wedding

class WeddingAdmin(admin.ModelAdmin):
	list_display = ['bride','groom','contact_phone','contact_email',
			'rehearsal_dinner','wedding_ceremony','wedding_reception',]

admin.site.register(Wedding,WeddingAdmin)
