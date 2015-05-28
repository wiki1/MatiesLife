from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^article/(?P<article_id>[0-9]+)/$', views.article, name = 'article'),
    url(r'^user/(?P<user_id>[0-9]+)/create/$', views.Create, name = 'Create'),
    url(r'^disambiguation/$', views.disambiguation, name = 'disambiguation'),
    url(r'^search/$', views.Search, name = 'Search'),
    url(r'^profile/(?P<user_id>[0-9]+)/$', views.profile, name = 'profile'),
    url(r'^login/$', views.loginView, name = 'login'),
    url(r'^loggedIn/$', views.loggedIn, name='loggedIn'),
]
