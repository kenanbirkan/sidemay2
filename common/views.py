from django.http import HttpResponse
from django.shortcuts import render
from .models import Profile,Dues_Sandik,Dues_Dernek,Credit
from .forms import UserForm,DuesForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
import traceback

@login_required(login_url="login/")
def login(request):
    return render(request,"home.html")

@login_required(login_url="home/")
def home(request):
    return render(request,"home.html")


@login_required
def add_profile(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            new_user = User.objects.create_user(username=request.POST['username'],
                                     email=request.POST['email'],
                                     password=request.POST['username'])
            profile = new_user.profile
            profile.sandik=request.POST['sandik']
            profile.dernek = request.POST['dernek']
            profile.address = request.POST['address']
            profile.tel = request.POST['tel']
            # profile.start_date = request.POST['start_date']
            profile.save()
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
        return  HttpResponseNotFound('<h1>No Page Here</h1>')

@login_required
def add_dues_sandik(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            try:

                tc=request.POST['tc']
                value = request.POST['value']
                insert_date = request.POST['insert_date']
                p_obj = Profile.objects.filter(user__username=tc) # check user exist else return exception

                new_due = Dues_Sandik()
                new_due.tc=tc
                new_due.value=value
                new_due.insert_date=insert_date
                new_due.save()

                ds_form = DuesForm()
                return render(request, 'dues_sandik_form.html', {
                    'ds_form': ds_form
                })
            except:
                print traceback.format_exc()

        else:
            ds_form = DuesForm()
        return render(request, 'dues_sandik_form.html', {
            'ds_form': ds_form
        })
    else:
        return  HttpResponseNotFound('<h1>No Page Here</h1>')

@login_required
def add_dues_dernek(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            try:

                tc=request.POST['tc']
                value = request.POST['value']
                insert_date = request.POST['insert_date']
                p_obj = Profile.objects.filter(user__username=tc) # check user exist else return exception

                new_due = Dues_Dernek()
                new_due.tc=tc
                new_due.value=value
                new_due.insert_date=insert_date
                new_due.save()

                ds_form = DuesForm()
                return render(request, 'dues_sandik_form.html', {
                    'ds_form': ds_form
                })
            except:
                print traceback.format_exc()

        else:
            ds_form = DuesForm()
        return render(request, 'dues_sandik_form.html', {
            'ds_form': ds_form
        })
    else:
        return  HttpResponseNotFound('<h1>No Page Here</h1>')

@login_required
def add_credit(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            try:

                tc=request.POST['tc']
                value = request.POST['value']
                insert_date = request.POST['insert_date']
                p_obj = Profile.objects.filter(user__username=tc) # check user exist else return exception

                new_due = Credit()
                new_due.tc=tc
                new_due.value=value
                new_due.insert_date=insert_date
                new_due.save()

                ds_form = DuesForm()
                return render(request, 'dues_sandik_form.html', {
                    'ds_form': ds_form
                })
            except:
                print traceback.format_exc()

        else:
            ds_form = DuesForm()
        return render(request, 'dues_sandik_form.html', {
            'ds_form': ds_form
        })
    else:
        return  HttpResponseNotFound('<h1>No Page Here</h1>')