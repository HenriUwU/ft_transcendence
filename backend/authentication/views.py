import logging
from . import forms
from django.http import HttpResponse
from django.contrib import messages
from authentication.models import User, Friend_Request
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser

def signin(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
                username=form.cleaned_data['username']
                password=form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('batpong')
                else:
                    message = 'Identifiants invalides.'
                    return render(request, 'index.html', {'form': form})
    else:
        form = forms.LoginForm()
        return render(request, 'views/signin.html', context={'form': form})

def signup(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('batpong')
        else:
            return render(request, 'index.html')
    return render(request, 'views/signup.html', context={'form': form})

@login_required
def send_friend_request(request, userID):
    from_user = request.user
    to_user = User.objects.get(id=userID)
    friend_request, created = Friend_Request.objects.get_or_create(from_user=from_user, to_user=to_user)
    if created:
        return render (request, 'views/batprofile.html')
    else:
        return render (request, 'views/batprofile.html')

@login_required
def accept_friend_request(request, requestID):
    friend_request = Friend_Request.objects.get(id=requestID)
    if friend_request.to_user == request.user:
        friend_request.to_user.friends.add(friend_request.from_user)
        friend_request.from_user.friends.add(friend_request.to_user)
        friend_request.delete()
        return render (request, 'views/batprofile.html')
    else:
        return render (request, 'views/batprofile.html')
