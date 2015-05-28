from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from .models import myUsers

# Create your views here.
def loginView(request):
	if request.session['has_loggedin'] == True:
		request.session['has_loggedin'] = False
		request.session['user_id'] = 0

	return render(request, 'login/login.html')

def loggedIn(request):
	logout = "<br /><a href='/login'>logout</a>"
	if request.session['has_loggedin'] == True:
		requestedEmail = request.POST['email']
		currentUser = myUsers.objects.get(email=requestedEmail)
		request.session['user_id'] = currentUser.id
		myOutput = "You have already loggedIn as "+ currentUser.name + " - " + str(request.session['user_id']) + logout
	else:
		requestedEmail = request.POST['email']
		try:
			requestedUser = myUsers.objects.get(email=requestedEmail)
			if (requestedUser.password == hash(request.POST['password'])):
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