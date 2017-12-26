from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from django.http import HttpResponseNotFound
from django.shortcuts import render

from .forms import UserForm, DuesForm ,TCrequestForm
from .models import Profile, Dues_Sandik, Dues_Dernek, Credit, User
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
            return_dict = {
                "error_val": "2"
            }
            return render(request, 'dues_sandik_form.html', {'ds_form': ds_form})
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
            return_dict = {
                "error_val": "2"
            }
            return render(request, 'dues_dernek_form.html', {'ds_form': ds_form}, {'ret_dict': return_dict})
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
            return_dict = {
                "error_val": "2"
            }
            return render(request, 'dues_credit_form.html', {'ds_form': ds_form}, {'ret_dict': return_dict})
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






class MultipleTables(MultiTableMixin, TemplateView):

    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'multiTable.html'
    table_pagination = {
        'per_page': 2
    }

    def get_table_pagination(self, table):
        return {'per_page': 2}

    def get(self, request, *args, **kwargs):
        qs = Dues_Sandik.objects.all()
        table = NameTable(qs)
        # table.paginate(page=request.GET.get('page', 1), per_page=2)
        table2 = NameTable(qs)
        # table2.paginate(page=request.GET.get('page', 1), per_page=2)
        tables = [
            table,
            table2
        ]
        return render(request, self.template_name, {'tables': tables})



def tc_sorgu_view(request):
    '''Demonstrate the use of the bootstrap template'''

    if request.user.is_superuser:
        if request.method == 'POST':
            tc = request.POST['tc']
            if tc == '000':
                result = Dues_Sandik.objects.all()
            else:
                result = Dues_Sandik.objects.filter(tc=tc)
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
            data.append({"tc": "Total", "value": total_value, "date": ""})
            table = NameTable(data)

            RequestConfig(request, paginate={'per_page': 50}).configure(table)

            return render(request, 'bootstrap_template.html', {
                'table': table
            })
        else:
            tc_form = TCrequestForm()
            return_dict = {
                "error_val": "2"
            }
            return render(request, 'tc_request_form.html', {'ds_form': tc_form}, {'ret_dict': return_dict})
