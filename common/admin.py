from django.contrib import admin

# Register your models here.
from .models import Dues_Sandik,Dues_Dernek,Credit,Outcome,Profile,Credit_Pays



class admin_Dues(admin.ModelAdmin):
    search_fields =  ['tc']
    list_display = ['tc','value','insert_date']

class admin_Profile(admin.ModelAdmin):
    search_fields =  ['tc']
    list_display = ['tc','tel','start_date']

admin.site.register(Dues_Sandik,admin_Dues)
admin.site.register(Dues_Dernek,admin_Dues)
admin.site.register(Credit,admin_Dues)
admin.site.register(Credit_Pays,admin_Dues)
admin.site.register(Outcome)
admin.site.register(Profile,admin_Profile)