from django.shortcuts import render
from django.http import HttpResponse
from post.models import *
from django.core.urlresolvers import reverse

# Create your views here.
def hello(request):
	return HttpResponse('hello')

def list(request):
	posty = Post.objects.all()
	return render(request, "list.html", {'posty': posty})

def show(request, id):
	post = Post.objects.get(id=id)
	url = reverse ('lista')
	return render(request, "show.html", {'post':post, 'url': url})