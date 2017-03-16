from django.http import HttpResponse
from django.shortcuts import render
from .models import Profile
from .forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound


@login_required(login_url="login/")
def login(request):
    return render(request,"home.html")

@login_required(login_url="home/")
def home(request):
    return render(request,"home.html")


@login_required
def edit_profile(request):
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
            profile.grup = request.POST['grup']
            # profile.start_date = request.POST['start_date']
            profile.save()
            user_form = UserForm()
            return render(request, 'testform.html', {
                'user_form': user_form
            })
        else:
            user_form = UserForm()
        return render(request, 'testform.html', {
            'user_form': user_form
        })
    else:
        return  HttpResponseNotFound('<h1>No Page Here</h1>')