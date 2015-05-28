from django.conf.urls import url

from . import views

urlpatterns = [
	#/postArticles
	url(r'^$', views.preliminary, name='preliminary'),
	#/postArticles/1
	url(r'^(?P<article_id>[0-9]+)/$', views.postedArticle, name='postedArticle'),
	#/preliminary/1/addItems
	url(r'^(?P<articles_id>[0-9]+)/addItems/$', views.addItems, name='addItems'),
]