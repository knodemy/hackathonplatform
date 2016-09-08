"""djangotest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import login
from django.contrib.auth import views as auth_views
from hackathons import views
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', auth_views.login, name='my_login'),
    url(r'^login/$', login),
    url(r'^index/', views.index ),
#    url(r'^flyer/(?P<event_id>[0-9]+)/$', views.dynpages, name='Flyer'),
    url(r'^dynpages/', views.dynpages ),

    url(r'^password/reset/$',auth_views.password_reset,{'post_reset_redirect' : '/password/reset/done/'},name="password_reset"),
    url(r'^password/reset/done/$',auth_views.password_reset_done),
    url(r'^password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',auth_views.password_reset_confirm,{'post_reset_redirect' : '/password/done/'}),
    url(r'^password/done/$',auth_views.password_reset_complete),

    url(r'^eventpagetest', views.eventpagetest),
    url(r'^accounts/profile/', include(admin.site.urls)),
    url(r'^howThisWorks', views.howThisWorks),
    url(r'^registrationComplete', views.registrationComplete),
    url(r'^adminSignUp/$', views.adminSignUp, name='adminSignUp'),
    
    #url(r'^Event/', include('knohack.urls')),
    url(r'^(?P<event_id>[0-9]+)/$', views.test_Flyer, name='Flyer'),

    #url(r'^login/', 'django.contrib.auth.views.login', name='my_login'),    
    #django.contrib.auth.views.password_reset, 
    #'django.contrib.auth.views.password_reset_done'),
    #'django.contrib.auth.views.password_reset_confirm', 
    #'django.contrib.auth.views.password_reset_complete'),
    #url(r'^forgotPassword/', views.forgotPassword),
    #url(r'^reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
    #       'views.reset_confirm', name='reset_confirm'),
    #url(r'^reset/', views.reset),
    #url(r'^password_reset_form', views.reset),
    #url(r'^adminSignUp/', views.adminSignUp),
    #url(r'^adminSignUp/', views.adminSignUp),
    #url('^adminSignUp/', CreateView.as_view(template_name='registration/adminSignUp.html',form_class=UserCreationForm,success_url='/registrationComplete.html')),
    #url('^accounts/', include('django.contrib.auth.urls')),
]
