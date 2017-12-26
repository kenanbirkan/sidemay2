import  django_tables2 as tables
from django_filters import FilterSet
from .models import Profile, Dues_Sandik, Dues_Dernek, Credit , User

class ProfileTable(tables.Table):
    class Meta:
        model = Profile
        attrs = {'class': 'table table-bordered table-striped table-hover'}

class ProfileFilter(FilterSet):
    class Meta:
        model = Profile
        fields = {
            'tc': ['exact', 'contains'],
            # 'tz': ['exact'],
        }

class SandikTable(tables.Table):
    class Meta:
        model = Dues_Sandik

class SandikFilter(FilterSet):
    class Meta:
        model = Dues_Sandik
        fields = {
            'tc': ['exact', 'contains'],
            # 'tz': ['exact'],
        }

class NameTable(tables.Table):
    class Meta:
        model = Dues_Sandik
        attrs = {'class': 'table table-bordered table-striped table-hover'}
        exclude = ('record_id',)