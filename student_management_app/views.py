from django.contrib import messages
from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .EmailBackend import EmailBackend


# Create your views here.


def showPage(request):
    return render(request, 'hod_template/home_content.html')


def showLoginPage(request):
    return render(request, 'login.html')


def doLogin(request):
    if request.method == 'POST':
        user = EmailBackend.authenticate(request, request.POST['email'], request.POST['password'])
        if user is None:
            messages.error(request, "Please check again!")
            return render(request, 'login.html', {})
        else:
            login(request, user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('admin_page')
            elif user_type == '2':
                return HttpResponse('Staff login')
            elif user_type == '3':
                return HttpResponse('Student login')
    return render(request, 'login.html', {})


def userDetail(request):
    if request.user is not None:
        return HttpResponse('Username: ' + request.user.username + ' Email: ' + request.user.email +
                            ' Type: ' + request.user.user_type)
    else:
        return HttpResponse('You are not login')


def doLogout(request):
    logout(request)
    return HttpResponse('You are logout')
