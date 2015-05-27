from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.loginView, name='login'),
	url(r'^/loggedIn/$', views.loggedIn, name='loggedIn')
]