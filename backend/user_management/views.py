import logging
from . import forms
from django.http import HttpResponse
from django.contrib import messages
from user_management.models import User, Friend_Request, UserTwoFactorAuthData
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.models import AnonymousUser
from django.http import JsonResponse
from django.contrib.auth.views import LogoutView
from auth_2FA.jwt import set_all_cookies_jwt

logger = logging.getLogger(__name__)

def signin(request):
    form = forms.LoginForm()
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
                username=form.cleaned_data['username']
                password=form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    if user.log2fa is True:
                        if hasattr(user, 'two_factor_auth_data'):
                            request.session['user_id'] = user.id
                            return JsonResponse({'loginForm': True, 'OTPEnabled': True})
                    else:
                        login(request, user)
                        response = JsonResponse({'loginForm': True})
                        response = set_all_cookies_jwt(request, response, user)
                        return response
                else:
                    return JsonResponse({'loginForm': False})
    else:
        if request.GET.get('Valid') == "true":
            return render(request, 'views/signin.html', context={'form': form})
    return render(request, 'index.html', {'form': form})

def signup(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST) 
        if form.is_valid():
            form.save()
            return JsonResponse({'signupSuccess': True})
        else:
            return JsonResponse({'signupForm': True})
    if request.GET.get('Valid') == "true":
        form = forms.SignupForm() 
        return render(request, 'views/signup.html', context={'form': form})
    form = forms.SignupForm() 
    return render(request, 'index.html', {'form': form})

def send_friend_request(request, userID):
    from_user = request.user
    to_user = User.objects.get(id=userID)
    friend_request, created = Friend_Request.objects.get_or_create(from_user=from_user, to_user=to_user)
    return JsonResponse({'success': True})

def accept_friend_request(request, requestID):
    friend_request = Friend_Request.objects.get(id=requestID)
    friend_request.to_user.friends.add(friend_request.from_user)
    friend_request.from_user.friends.add(friend_request.to_user)
    friend_request.delete()
    return JsonResponse({'success': True })

def decline_friend_request(request, requestID):
    friend_request = Friend_Request.objects.get(id=requestID)
    friend_request.delete()
    return JsonResponse({'success': True})

class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        response.delete_cookie('jwt_access', path='/', domain='localhost')
        response.delete_cookie('jwt_refresh', path='/', domain='localhost')
        
        status = request.COOKIES.get('logout_status', '')
        if status:
            response.delete_cookie('logout_status')
        
        return response

def CheckLogoutView(request):
    status = request.COOKIES.get('logout_status', '')
    if status:
        return JsonResponse({'formuser': True})
    else:
        return JsonResponse({'formuser': False})

from django.core.serializers.json import DjangoJSONEncoder

@login_required
def display_user_profil(request, userID):
    userprofil = User.objects.get(id=userID)
    friends_json = list(userprofil.friends.values())
    response = JsonResponse({
        'name': userprofil.username,
        'is_online': userprofil.is_online,
        'avatar': userprofil.avatar.url,
        'friends': friends_json,
    }, encoder=DjangoJSONEncoder)
    return response
