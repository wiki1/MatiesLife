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
from ipware.ip import get_ip
from django.utils import timezone

QUERY = "search-query"

MODEL_MAP = { Articles: ["title"],

}

from django.template import RequestContext, loader
from .models import Users, Requests, Articles, Content
from django.http import HttpResponse

# Create your views here.


def home(request):
	template = loader.get_template('home.html')
	return HttpResponse(template.render())

def article(request, article_id):
	article = Articles.objects.filter(id=article_id)  
	context_dic = ({"article" : article,

					})
	return render(request, "article.html", context_dic)

@csrf_exempt
def Search(request):  #this search is still case sensitive and needs fixing
	if request.GET.get('term'):
		search_list = []
		search_articles = []

		search_string = request.GET.get('term')
		search_list = search_string.split()

		for article in Articles.objects.all():
			for word in search_list:
				if word in article.title:
					search_articles.append(article.title)		
						
		context_dic = Context({"search_string" : request.GET.get('term'),
								"search_list" : search_list,
								"search_articles" : search_articles,
								"Articles" : Articles.objects.all(),
								})
		return render (request, 'disambiguation.html', context_dic)


	return render (request, 'disambiguation.html')

	

def Create(request, user_id):
	template = loader.get_template('create.html')
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

@csrf_exempt
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


@csrf_exempt
def anonymousLogin(request):
	logout = "<br /><a href='/wikiApp/login'>logout</a>"

	if(request.session['has_loggedin'] == True):
		currentUser = request.session['user_id']
		myOutput = "You are already logged in as: " + str(Users.objects.get(pk=currentUser).name) + logout
	else:
		try:
			ip = get_ip(request)
			ip = str(ip)
			
			myOutput = "You are now logged in with your IP address: " + ip
			myOutput += logout
			userAlreadyExists = None
			try:
				userAlreadyExists = Users.objects.get(name=ip)
			except:
				userAlreadyExists = None 
			
			if userAlreadyExists == None:
				newUser = Users(name=ip, surname=ip, user_type=0, password="0", email=ip, date_of_birth=timezone.now())
				newUser.save()
				request.session['has_loggedin'] = True
				request.session['user_id'] = newUser.id
			else:
				request.session['has_loggedin'] = True
				request.session['user_id'] = userAlreadyExists.id
		except:
			myOutput = "We don't have an IP address for user"

	return HttpResponse(myOutput)