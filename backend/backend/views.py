from django.shortcuts import render, redirect
from authentication.forms import AvatarForm
from authentication.forms import UpdateUsername
from authentication.models import User, Friend_Request
from django.contrib.auth.decorators import login_required
from authentication.forms import CustomPasswordChangeForm
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import logging
import json

def home(request):
	user = request.user
	return render(request, "index.html", {'user': user})

logger = logging.getLogger(__name__)

@csrf_exempt
def lang(request):
	if request.method == 'POST':
		body = json.loads(request.body)
		key = body['key']
		request.session['user_language'] = key
		logger.info('Key: %s', key)
		logger.info('Hello World')
		return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def batcave(request):
	user = request.user
	return render(request, "views/batcave.html", {'user': user})

@login_required
def batprofile(request):
	user = request.user
	avatar_url = user.avatar.url if user.avatar else None
	if request.method == 'POST':
		formUsername = UpdateUsername(request.POST, instance=request.user)
		formPassword = CustomPasswordChangeForm(request.user, request.POST)
		formAvatar = AvatarForm(request.POST, request.FILES)
		if formUsername.is_valid():
			formUsername.save()
			return render(request, 'index.html')
		if formPassword.is_valid():
			formPassword.save()
			return render(request, 'index.html')
		if formAvatar.is_valid():
			user.avatar = formAvatar.cleaned_data['avatar']
			user.save()
			return render(request, 'index.html')
	else:
		formUsername = UpdateUsername()
		formPassword = CustomPasswordChangeForm(request.user)
		formAvatar = AvatarForm()
		all_users = User.objects.exclude(id=request.user.id).exclude(is_superuser=True)
		all_friend_request = Friend_Request.objects.filter(to_user=user)
		friends = user.friends.all()
		return render(request, "views/batprofile.html", {
			'formUsername':formUsername, 
			'user':user,
			'formPassword':formPassword,
			'formAvatar':formAvatar,
			'avatar_url':avatar_url,
			'all_users':all_users,
			'all_friend_request':all_friend_request,
			'friends':friends,
        })

def batpong(request):
	return render(request, "views/batpong.html")
