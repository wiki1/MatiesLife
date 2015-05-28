from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader, Context
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.db.models import Sum, Avg
from .models import Article, Content
from django.http import QueryDict
# Create your views here.

a = Article(title = 'syllables')
a.save()

def preliminary(request):
	
	c = Content(article=Article(pk=a.id), heading='verse 1', paragraph='dum dum')
	c.save()
	#articles = Article.objects.get(pk=a.id)
	#contents = Content.objects.get(pk=c.id)

	try:
		articles = Article.objects.get(pk=a.id)
		contents = Content.objects.get(pk=c.id)
	except Article.DoesNotExist:
		raise Http404("Article does not exist")
	#return HttpResponse(render(request, 'postingArticles/postArticles.html', {'articles': articles, 'contents':contents}))


	return render(request, 'postingArticles/postArticles.html', {'articles': articles, 'contents':contents})

def postedArticle(request):
	#value1 = request.POST['title']
	#value2 = request.POST['paragraph']
	#return HttpResponse(value1 + "<br /> " + value2)
	pass


def addItems(request, articles_id):
	title = request.POST['title']
	heading = request.POST['heading']
	paragraph = request.POST['paragraph']

	myArticle = Article.objects.get(pk=articles_id)
	myArticle.title = title

	myArticle.save()
	contents = Content.objects.get(pk=indexPk)

	contents.heading = heading
	contents.paragraph = paragraph

	contents.save()
	++indexPk
	return HttpResponseRedirect(reverse('postingArticles:preliminary'))