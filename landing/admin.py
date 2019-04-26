from django.contrib import admin
from .models import Partners
# Register your models here.


class PartnersAdmin(admin.ModelAdmin):
	model = Partners
	extra = 10 
	fieldsets = [
		('Name information', {'fields': ['name']}),
		('Email information', {'fields':['email']})
	]

	list_display = ('name', 'email', 'date_pub')
	list_filter = ['date_pub', 'email']
	search_fields = ['email', 'name']
admin.site.register(Partners, PartnersAdmin)