from django.shortcuts import render
from django.template import RequestContext, loader, Template
from .models import Users, Requests, Articles, Content
from .utils import generic_search
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts  import render_to_response,redirect
from django.template.context_processors import csrf
from django.template import Context
from django.views.decorators.csrf import csrf_exempt
from .models import Users, Requests, Articles, Content

QUERY = "search-query"

MODEL_MAP = { Articles: ["title"],

}

def home(request):
	template = loader.get_template('home.html')
	return HttpResponse(template.render())

def article(request, article_id):
	template = loader.get_template('article.html')  
	return HttpResponse(template.render())

@csrf_exempt
def Search(request):
	if request.GET:
		search_list = {}
		search_articles = []
		resuilt_list = {}

		search_string = request.GET['term']
		search_list = search_string.split()

		for title in Articles.objects.all():
			for word in search_list:
				if word in title.title:
					search_articles.append(title.title)		
			


			
		context_dic = Context({"search_string" : request.GET['term'],
								"search_list" : search_list,
								"search_articles" : search_articles,
								"Articles" : Articles.objects.all(),
								"resuilt_list" : resuilt_list,
								})
		return render (request, 'search_results.html', context_dic)


	return render (request, 'search.html')

	
def Create(request, user_id):
	template = loader.get_template('create.html')
	return HttpResponse(template.render())

def disambiguation(request):
	template = loader.get_template('disambiguation.html')	
	return HttpResponse(template.render())
	
def profile(request, user_id):
	template = loader.get_template('profile.html')
	return HttpResponse(template.render())

#def signup_login(request):
#	template = loader.get_template('signup_login.html')
#	return HttpResponse(template.render())

#login

def loginView(request):
	request.session['has_loggedin'] = False
	request.session['user_id'] = 0

	return render(request, 'login.html')

def loggedIn(request):
	logout = "<br /><a href='/wikiApp/login'>Click here to logout</a>"
	if request.session['has_loggedin'] == True:
		requestedEmail = request.POST['email']
		currentUser = Users.objects.get(email=requestedEmail)
		request.session['user_id'] = currentUser.id
		myOutput = "You have already loggedIn as "+ currentUser.name + " - " + str(request.session['user_id']) + logout
	else:
		requestedEmail = request.POST['email']
		try:
			requestedUser = Users.objects.get(email=requestedEmail)
			if (requestedUser.password == str(hash(request.POST['password']))):
				email = request.POST['email']
				password = request.POST['password']
				myOutput = "your email is: " + email+ "<br />" + "Your password is: " + password + logout
				request.session['has_loggedin'] = True
				request.session['user_id'] = requestedUser.id
			else:
				myOutput = "Correct email, wrong password" + logout
		except:
			myOutput = 'login failed' + logout
			request.session['has_loggedin'] = False
			request.session['user_id'] = 0
	
	return HttpResponse(myOutput)