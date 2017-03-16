from django.contrib import admin

# Register your models here.
from .models import Dues_Sandik,Dues_Dernek,Credit,Outcome,Profile

admin.site.register(Dues_Sandik)
admin.site.register(Dues_Dernek)
admin.site.register(Credit)
admin.site.register(Outcome)
admin.site.register(Profile)