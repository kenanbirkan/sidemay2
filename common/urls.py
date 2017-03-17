
from django.conf.urls import include, url
from . import views
from . import forms
app_name = 'common'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^add_profile/', views.add_profile, name='add_profile'),
    url(r'^add_dues_sandik/', views.add_dues_sandik, name='add_dues_sandik'),


]