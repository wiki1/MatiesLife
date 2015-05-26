from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
	return HttpResponse("Hello guys. This is our home page.")

def article(request, article_id):
	response = "Hello guys. This is the page for article %s"
	return HttpResponse(response % article_id)

def Create(request, user_id):
	return HttpResponse("Hello guys. This is where we create actual articles for our wiki")

def disambiguation(request):
	return HttpResponse("Hello guys. If you see this, it means your search was unsuccesfull")

def profile(request, user_id):
	response = "Hello guys. This is the profile page for user number %s"
	return HttpResponse(response % user_id)

def signup_login(request):
	return HttpResponse("Hello guys. This is our home page.")