from django.contrib import admin
from weddings.models import Wedding

class WeddingAdmin(admin.ModelAdmin): pass

admin.site.register(Wedding,WeddingAdmin)
