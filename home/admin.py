from django.contrib import admin
from .models import Contact
# Register your models here.


class Change(admin.ModelAdmin):
	list_display =('id','Name','Email','Phone','Message')
	search_fields =('Name',)

admin.site.register(Contact,Change)	
