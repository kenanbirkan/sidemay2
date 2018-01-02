from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from django.http import HttpResponseNotFound
from django.shortcuts import render

from .forms import UserForm, DuesForm ,TCrequestForm ,karPayirequestForm
from .models import Profile, Dues_Sandik, Dues_Dernek, Credit, User ,Credit_Pays ,Profit ,DEFAULT_TC
import traceback
from django.contrib import messages

from django_filters.views import FilterView
from django_tables2 import MultiTableMixin, RequestConfig, SingleTableMixin, SingleTableView
from .table_objects import ProfileFilter, ProfileTable, SandikFilter, SandikTable, NameTable ,ProfitFilter , ProfitTable
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.db.models import Sum
import os
import mimetypes

from django.conf import settings
from django.http import HttpResponse

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
                profile.ad = request.POST['first_name']
                profile.soyad = request.POST['last_name']
                profile.email = request.POST['email']
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
        print(traceback.format_exc())
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
                return render(request, 'dues_form.html', {'ds_form': ds_form, 'title_message': "Sandik Aidat Odeme Ekranı"})
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
                return render(request, 'dues_form.html', {'ds_form': ds_form, 'title_message': "Dernek Aidat Odeme Ekranı"})
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
                return render(request, 'dues_form.html', {'ds_form': ds_form, 'title_message': "Kredi Verme Ekranı"})
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
                return render(request, 'dues_form.html', {'ds_form': ds_form, 'title_message': "Kredi Odeme Ekranı"})
            except:
                print(traceback.format_exc())

        else:
            ds_form = DuesForm()
            return render(request, 'dues_form.html', {'ds_form': ds_form,'title_message':"Kredi Odeme Ekranı"})
    else:
        return HttpResponseNotFound('<h1>No Page Here</h1>')



@login_required
def download_sidemay_1(request):
    try:
        file_path = "doc/sidemay1.JPG"
        content_type = mimetypes.guess_type(file_path)[0]
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type=content_type)
                response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
                return response

        return HttpResponseNotFound('<h1>No Page Here</h1>')
    except:
        return HttpResponseNotFound('<h1>No Page Here</h1>')

@login_required
def download_sidemay_2(request):
    try:
        file_path = "doc/sidemay2.JPG"
        content_type = mimetypes.guess_type(file_path)[0]
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type=content_type)
                response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
                return response

        return HttpResponseNotFound('<h1>No Page Here</h1>')
    except:
        return HttpResponseNotFound('<h1>No Page Here</h1>')

class FilteredProfileListView(LoginRequiredMixin, SingleTableMixin, FilterView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    table_class = ProfileTable
    model = Profile
    template_name = 'user_template.html'
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



class NormalUserMultipleTables(LoginRequiredMixin,MultiTableMixin, TemplateView):

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

        return render(request, self.template_name, {'tables': tables,
                                                    'ds_form': '',"title_message":"Kullanıcı bilgileri tablosu"})







class MultipleTables(LoginRequiredMixin,MultiTableMixin, TemplateView):

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


class FilteredProfitListView(LoginRequiredMixin, SingleTableMixin, FilterView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'


    table_class = ProfitTable
    model = Profit
    template_name = 'bootstrap_template.html'
    filterset_class = ProfitFilter
    form_class = karPayirequestForm



    def get(self, request, *args, **kwargs):
        ds_form = karPayirequestForm()
        my_filter = ProfitFilter(request.GET)
        my_choice = my_filter.data.get('tc')
        kar_payi = request.session.get('kar_payi', 0)
        table = self.calculate_kar_payi(kar_payi, my_choice)
        return render(request, self.template_name, {"table":table,
                                                    'ds_form': ds_form,
                                                    "title_message": "KAR payi miktari girip sorgulayiniz..., yeni hesaplama icin tekrar miktar giriniz",
                                                    'filter': self.filterset_class})

    def post(self, request, *args, **kwargs):
        my_filter = ProfitFilter(request.GET)
        my_choice = my_filter.data.get('tc')
        kar_input = int(request.POST["kar_payi"])
        request.session['kar_payi'] = kar_input

        table = self.calculate_kar_payi(kar_input, my_choice)

        RequestConfig(request).configure(table)
        ds_form = karPayirequestForm()
        return render(request, self.template_name, {'table': table,
                                                    'ds_form': ds_form,
                                                    'filter': self.filterset_class,
                                                    "title_message": "KAR payi miktari girip sorgulayiniz..., yeni hesaplama icin tekrar miktar giriniz"})

    def calculate_kar_payi(self, kar_input, my_choice):
        all_members = Profile.objects.all()
        total_sandik = Dues_Sandik.objects.all().aggregate(Sum('value'))
        total_aidat = 0
        if total_sandik.get('value__sum'):
            total_aidat += total_sandik.get('value__sum')

        data = []
        total_value = 0
        total_kar = 0
        for member in all_members:
            tc = member.tc
            if tc != DEFAULT_TC:
                result_sandik = Dues_Sandik.objects.filter(tc=tc).aggregate(Sum('value'))
                member_aidat=0
                if result_sandik.get('value__sum'):
                    member_aidat += result_sandik.get('value__sum')

                member_profit = (kar_input / total_aidat) * member_aidat
                total_value += member_aidat
                total_kar += member_profit
                data.append({"tc": tc, "odenen_aidat": member_aidat, "kar_payi": member_profit})
        data.append({"tc": "TOTAL", "odenen_aidat": total_value, "kar_payi": total_kar})
        if my_choice:
            data = [x for x in data if x['tc'] == my_choice]
        table = ProfitTable(data, order_by='-kar_payi')
        return table
