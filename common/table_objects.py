import  django_tables2 as tables
from django_filters import FilterSet
from .models import Profile, Sorgu_model, Profit


class ProfileTable(tables.Table):
    class Meta:
        model = Profile
        attrs = {'class': 'table table-bordered table-striped table-hover'}
        exclude = ('user', 'id',)



class ProfileFilter(FilterSet):
    class Meta:
        model = Profile
        fields = {
            'tc': ['exact', 'contains'],
            # 'tz': ['exact'],
        }


class SorguTable(tables.Table):
    class Meta:
        model = Sorgu_model
        attrs = {'class': 'table table-bordered table-striped table-hover'}
        exclude = ('record_id',"id",)
        per_page = 30


class ProfitTable(tables.Table):
    class Meta:
        model = Profit
        attrs = {'class': 'table table-bordered table-striped table-hover'}
        exclude = ('record_id',)
        per_page = 30

class ProfitFilter(FilterSet):
    class Meta:
        model = Profit
        fields = {
            'tc': ['exact'],

        }