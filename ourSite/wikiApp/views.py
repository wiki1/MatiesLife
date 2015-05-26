from django.shortcuts import render
from django.template import RequestContext, loader
from .models import Users, Requests, Articles, Content
from django.http import HttpResponse

# Create your views here.

def home(request):
	template = loader.get_template('home.html')
	return HttpResponse(template.render())

def article(request, article_id):
	template = loader.get_template('article.html')  
	return HttpResponse(template.render())

def Create(request, user_id):
	template = loader.get_template('create.html')
	return HttpResponse(template.render())

def disambiguation(request):
	template = loader.get_template('disambiguation.html')	
	return HttpResponse(template.render())
	
def profile(request, user_id):
	template = loader.get_template('profile.html')
	return HttpResponse(template.render())

def signup_login(request):
	template = loader.get_template('signup_login.html')
	return HttpResponse(template.render())
