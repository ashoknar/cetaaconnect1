from django.shortcuts import render
from django.template import RequestContext

def about_index(request):
	return render(request, 'about.html')