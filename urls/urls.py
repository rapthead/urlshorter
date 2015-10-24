from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout
from forms import BootstrapAuthenticationForm

urlpatterns = [
    url(r'^$', views.index, name='urls-index'),
    url(r'^(?P<hash_param>[a-zA-Z0-9]+)/$', views.shortcut, name='urls-shortcut'),
    url(r'^accounts/login/$', login, name='login', kwargs={'authentication_form': BootstrapAuthenticationForm}),
    url(r'^accounts/logout/$', logout, name='logout', kwargs={'next_page': '/'}),
]
