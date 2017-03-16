
from django.conf.urls import include, url
from . import views
from . import forms
app_name = 'common'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^edit_profile/', views.edit_profile, name='edit_profile'),


]