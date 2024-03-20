"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views as mainViews
from authentication import views as authenticationViews
from django.conf import settings
from django.conf.urls.static import static
from auth_API42 import views as API42Views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainViews.home, name='batpong'),
    path('batcave', mainViews.batcave, name='batcave'),
    path('batpong/', mainViews.batpong),
    path('batprofile', mainViews.batprofile),
    path('signin', authenticationViews.signin, name='signin'),
    path('signup', authenticationViews.signup, name='signup'),
  #  path('accounts/', include('allauth.urls')),
    path('cursus-and-users', API42Views.get_cursus_and_users, name='cursus_and_users'),
    path('callback', API42Views.callback, name='callback'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
