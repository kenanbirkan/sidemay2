from django.contrib import admin

# Register your models here.
from .models import Dues_Sandik,Dues_Dernek,Credit,Outcome,Profile,Credit_Pays,User
admin.site.disable_action('delete_selected')


def delete_all_records(modeladmin, request, queryset):
    profile_list = queryset.all()
    for item in profile_list:
        if not item.user.is_superuser:
            tc = item.tc
            Dues_Sandik.objects.filter(tc=tc).delete()
            Dues_Dernek.objects.filter(tc=tc).delete()
            Credit.objects.filter(tc=tc).delete()
            Credit_Pays.objects.filter(tc=tc).delete()
            Profile.objects.filter(tc=tc).delete()
            User.objects.filter(username=tc).delete()
delete_all_records.short_description = "!!! UYE VE TUM KAYITLARI SIL !!! "



class admin_Dues(admin.ModelAdmin):
    actions = ['delete_selected']
    search_fields =  ['tc']
    list_display = ['tc','value','insert_date']

class admin_Profile(admin.ModelAdmin):
    search_fields =  ['tc']
    list_display = ['tc','ad','soyad','tel','start_date']
    actions = [delete_all_records]

admin.site.register(Profile,admin_Profile)
admin.site.register(Dues_Sandik,admin_Dues)
admin.site.register(Dues_Dernek,admin_Dues)
admin.site.register(Credit,admin_Dues)
admin.site.register(Credit_Pays,admin_Dues)
