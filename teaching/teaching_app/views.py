from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# relative import
from .forms import UserModelForm,UserModelExtraForm


def index(request):
    return render(request,'teaching_app/index.html')

def UserInfoView(request):

    registered = False

    if request.method == 'POST':

        usermodel = UserModelForm(request.POST)
        usermodelextra = UserModelExtraForm(request.POST)

        if usermodel.is_valid() and usermodelextra.is_valid():

            user = usermodel.save()
            user.set_password(user.password)
            user.save()

            profile = usermodelextra.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True

    else:
        usermodel = UserModelForm()
        usermodelextra = UserModelExtraForm()

    context = {
        'usermodel' : usermodel,
        'usermodelextra' : usermodelextra,
        'registered' : registered,
    }

    return render(request,'teaching_app/register.html',context)



def UserLogin(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return redirect('../')

            else:
                return HttpResponse('Not active')

        else:
            return HttpResponse('Invalid Username or Password')

    else:
        return render(request,'teaching_app/login.html')


@login_required
def UserLogout(request):
    logout(request)
    return redirect('../')
