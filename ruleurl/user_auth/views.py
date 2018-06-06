from django.shortcuts import render
from . import forms
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request,'index.html',{})

def register(request):
    form = forms.UserForm()
    registered = False
    if request.method == 'POST':
        form = forms.UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            registered = True
            print('Validation Success ..!')
            print(form.cleaned_data['email'])
        else:
            print(user_form.errors,profile_form.errors)
    else:
        form = forms.UserForm()    
    return render(request,'register.html',{'form':form,'registered':registered})



def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        print(username)
        print(password)
        print(user)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account is not active")
        else:
            print('Someone tried to login failes')
            print("Username {} and Password {}".format(username,password))
            return HttpResponse('Invalid Login details')
    else:
        return render(request,'login.html',{})


@login_required
def user_logout(request):
    print('logouting........')
    logout(request)
    return HttpResponseRedirect(reverse('index')) 