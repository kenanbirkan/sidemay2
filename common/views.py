from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from django.http import HttpResponseNotFound
from django.shortcuts import render

from .forms import UserForm, DuesForm ,TCrequestForm
from .models import Profile, Dues_Sandik, Dues_Dernek, Credit, User ,Credit_Pays
import traceback
from django.contrib import messages

from django_filters.views import FilterView
from django_tables2 import MultiTableMixin, RequestConfig, SingleTableMixin, SingleTableView
from .table_objects import ProfileFilter, ProfileTable, SandikFilter, SandikTable, NameTable
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView

@login_required(login_url="/login/")
def login(request):
    return render(request, "home.html")


@login_required(login_url="/login/")
def home(request):
    return render(request, "home.html")


@login_required
def add_profile(request):
    try:
        if request.user.is_superuser:
            if request.method == 'POST':
                new_user = User.objects.create_user(username=request.POST['username'],
                                                    email=request.POST['email'],
                                                    password=request.POST['username'])
                profile = new_user.profile
                profile.tc = request.POST['tc']
                profile.sandik = request.POST['sandik']
                profile.dernek = request.POST['dernek']
                profile.address = request.POST['address']
                profile.tel = request.POST['tel']
                # profile.start_date = request.POST['start_date']
                profile.save()
                messages.success(request, '%s tc li kullanici basari ile eklendi.' % request.POST['username'])
                user_form = UserForm()
                return render(request, 'user_form.html', {
                    'user_form': user_form
                })
            else:
                user_form = UserForm()
                return render(request, 'user_form.html', {
                    'user_form': user_form
                })
        else:
            return HttpResponseNotFound('<h1>No Page Here</h1>')
    except:
        messages.error(request, '%s tc li kullanici kayıt edilemedi.' % request.POST['username'])
        user_form = UserForm()
        return render(request, 'user_form.html', {
            'user_form': user_form
        })


@login_required
def add_dues_sandik(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            try:

                tc = request.POST['tc']
                value = request.POST['value']
                insert_date = request.POST['insert_date']
                p_obj = Profile.objects.filter(user__username=tc)  # check user exist else return exception

                if p_obj:
                    new_due = Dues_Sandik()
                    new_due.tc = tc
                    new_due.value = value
                    new_due.insert_date = insert_date
                    new_due.save()
                    messages.success(request, 'Sandik aidat %s tc li kullaniciya eklendi.' % tc)
                else:
                    messages.error(request, '%s tc li kullanici bulunamadi lutfen kontrol ediniz' % tc)

                ds_form = DuesForm()
                return render(request, 'dues_sandik_form.html', {'ds_form': ds_form})
            except:
                print(traceback.format_exc())

        else:
            ds_form = DuesForm()
            return render(request, 'dues_form.html', {'ds_form': ds_form, 'title_message': "Sandik Aidat Odeme Ekranı"})
    else:
        return HttpResponseNotFound('<h1>No Page Here</h1>')


@login_required
def add_dues_dernek(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            try:

                tc = request.POST['tc']
                value = request.POST['value']
                insert_date = request.POST['insert_date']
                p_obj = Profile.objects.filter(user__username=tc)  # check user exist else return exception

                if p_obj:
                    new_due = Dues_Dernek()
                    new_due.tc = tc
                    new_due.value = value
                    new_due.insert_date = insert_date
                    new_due.save()
                    messages.success(request, 'Dernek aidat %s tc li kullaniciya eklendi.' % tc)
                else:
                    messages.error(request, '%s tc li kullanici bulunamadi lutfen kontrol ediniz' % tc)

                ds_form = DuesForm()
                return render(request, 'dues_dernek_form.html', {
                    'ds_form': ds_form
                })
            except:
                print(traceback.format_exc())

        else:
            ds_form = DuesForm()
            return render(request, 'dues_form.html', {'ds_form': ds_form, 'title_message': "Dernek Aidat Odeme Ekranı"})
    else:
        return HttpResponseNotFound('<h1>No Page Here</h1>')


@login_required
def add_credit(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            try:

                tc = request.POST['tc']
                value = request.POST['value']
                insert_date = request.POST['insert_date']
                p_obj = Profile.objects.filter(user__username=tc)  # check user exist else return exception

                if p_obj:
                    new_due = Credit()
                    new_due.tc = tc
                    new_due.value = value
                    new_due.insert_date = insert_date
                    new_due.save()
                    messages.success(request, 'Kredi %s tc li kullaniciya eklendi.' % tc)
                else:
                    messages.error(request, '%s tc li kullanici bulunamadi lutfen kontrol ediniz' % tc)

                ds_form = DuesForm()
                return render(request, 'dues_credit_form.html', {
                    'ds_form': ds_form
                })
            except:
                print(traceback.format_exc())

        else:
            ds_form = DuesForm()
            return render(request, 'dues_form.html', {'ds_form': ds_form, 'title_message': "Kredi Verme Ekranı"})
    else:
        return HttpResponseNotFound('<h1>No Page Here</h1>')


@login_required
def add_credit_pays(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            try:

                tc = request.POST['tc']
                value = request.POST['value']
                insert_date = request.POST['insert_date']
                p_obj = Profile.objects.filter(user__username=tc)  # check user exist else return exception

                if p_obj:
                    new_due = Credit_Pays()
                    new_due.tc = tc
                    new_due.value = value
                    new_due.insert_date = insert_date
                    new_due.save()
                    messages.success(request, 'Kredi %s tc li kullaniciya eklendi.' % tc)
                else:
                    messages.error(request, '%s tc li kullanici bulunamadi lutfen kontrol ediniz' % tc)

                ds_form = DuesForm()
                return render(request, 'dues_credit_form.html', {
                    'ds_form': ds_form
                })
            except:
                print(traceback.format_exc())

        else:
            ds_form = DuesForm()
            return render(request, 'dues_form.html', {'ds_form': ds_form,'title_message':"Kredi Odeme Ekranı"})
    else:
        return HttpResponseNotFound('<h1>No Page Here</h1>')


class FilteredProfileListView(LoginRequiredMixin, SingleTableMixin, FilterView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    table_class = ProfileTable
    model = Profile
    template_name = 'bootstrap_template.html'
    filterset_class = ProfileFilter


class FilteredSandikListView(LoginRequiredMixin, SingleTableMixin, FilterView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    table_class = SandikTable
    model = Dues_Sandik
    template_name = 'bootstrap_template.html'
    filterset_class = SandikFilter


def get_table_from_data(result,label):
    data = []
    total_value = 0
    for item in result:
        item_dict = {
            "tc": item.tc,
            "value": item.value,
            "insert_date": item.insert_date
        }
        total_value += item.value
        data.append(item_dict)
    data.append({"tc": "Total " + label, "value": total_value, "insert_date": ""})
    table = NameTable(data,order_by='insert_date')
    return table



class NormalUserMultipleTables(MultiTableMixin, TemplateView):

    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'multiTable.html'
    table_pagination = {
        'per_page': 20
    }
    form_class = TCrequestForm
    initial = {'key': 'value'}

    def get_table_pagination(self, table):
        return {'per_page': 20}

    def get(self, request, *args, **kwargs):
        current_user = request.user
        tc = current_user.username
        result_sandik = Dues_Sandik.objects.filter(tc=tc)
        result_dernek = Dues_Dernek.objects.filter(tc=tc)
        result_credit = Credit.objects.filter(tc=tc)
        result_credit_pays = Credit_Pays.objects.filter(tc=tc)

        table_sandik = get_table_from_data(result_sandik, "Sandik aidat")
        table_dernek = get_table_from_data(result_dernek, "Dernek aidat")
        table_credit = get_table_from_data(result_credit, "Kredi Verilen")
        table_credit_pays = get_table_from_data(result_credit_pays, "Kredi Odenen")

        tables = [
            table_sandik,
            table_dernek,
            table_credit,
            table_credit_pays
        ]
        RequestConfig(request).configure(table_sandik)
        return render(request, self.template_name, {'tables': tables,
                                                    'ds_form': '',"title_message":"Kullanıcı bilgileri tablosu"})







class MultipleTables(MultiTableMixin, TemplateView):

    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'multiTable.html'
    table_pagination = {
        'per_page': 20
    }
    form_class = TCrequestForm
    initial = {'key': 'value'}

    def get_table_pagination(self, table):
        return {'per_page': 20}

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'ds_form': form,"title_message":"TC SORGU EKRANI , tum liste icin 000 giriniz"})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        tc = request.POST['tc']
        if tc == '000':
             result_sandik = Dues_Sandik.objects.all()
             result_dernek = Dues_Dernek.objects.all()
             result_credit = Credit.objects.all()
             result_credit_pays = Credit_Pays.objects.all()
        else:
            result_sandik = Dues_Sandik.objects.filter(tc=tc)
            result_dernek = Dues_Dernek.objects.filter(tc=tc)
            result_credit = Credit.objects.filter(tc=tc)
            result_credit_pays = Credit_Pays.objects.filter(tc=tc)

        table_sandik = get_table_from_data(result_sandik,"Sandik aidat")
        table_dernek = get_table_from_data(result_dernek,"Dernek aidat")
        table_credit = get_table_from_data(result_credit,"Kredi Verilen")
        table_credit_pays = get_table_from_data(result_credit_pays, "Kredi Odenen")

        tables = [
            table_sandik,
            table_dernek,
            table_credit,
            table_credit_pays
        ]
        return render(request, self.template_name, {'tables': tables,
                                                    'ds_form': form,"title_message":"TC SORGU EKRANI , tum liste icin 000 giriniz"})

