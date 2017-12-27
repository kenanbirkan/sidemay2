
from django.conf.urls import include, url
from . import views
from . import forms
from .views import FilteredProfileListView ,FilteredSandikListView , MultipleTables ,NormalUserMultipleTables
app_name = 'common'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^add_profile/', views.add_profile, name='add_profile'),
    url(r'^add_dues_sandik/', views.add_dues_sandik, name='add_dues_sandik'),
    url(r'^add_dues_dernek/', views.add_dues_dernek, name='add_dues_dernek'),
    url(r'^add_credit/', views.add_credit, name='add_credit'),
    url(r'^add_credit_pays/', views.add_credit_pays, name='add_credit_pays'),
    url(r'^user_list/$', FilteredProfileListView.as_view(), name='filtertableview'),
    url(r'^sandik_aidat/$', FilteredSandikListView.as_view(), name='bootstrap'),
    url(r'^tc_sorgu_view/$', MultipleTables.as_view(), name='tc_sorgu_view'),
    url(r'^normal_user_view/$', NormalUserMultipleTables.as_view(), name='normal_user_view'),

]