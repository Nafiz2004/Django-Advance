from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from basic_app.forms import UserModelForm,UserModelExtraForm


def index(request):
    return render(request,'basic_app/index.html')

def UserModelView(request):

    registered = False

    if request.method == 'POST':
        usermodelform = UserModelForm(request.POST)
        usermodelextraform = UserModelExtraForm(request.POST)

        if usermodelform.is_valid() and usermodelextraform.is_valid():

            user = usermodelform.save()
            user.set_password(user.password)
            user.save()

            profile = usermodelextraform.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True
    else:
        usermodelform = UserModelForm()
        usermodelextraform = UserModelExtraForm()

    context = {
        'usermodelform' : usermodelform,
        'usermodelextaform' : usermodelextraform,
        'registered' : registered,
    }

    return render(request,'basic_app/registration.html',context)


def UserLogin(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return redirect('../../')
            else:
                return HttpResponse('Not active')
        else:
            return HttpResponse('Invalid Username or Password')

    else:
        return render(request,'basic_app/login.html')


@login_required
def UserLogout(request):
    logout(request)
    return redirect('../')
