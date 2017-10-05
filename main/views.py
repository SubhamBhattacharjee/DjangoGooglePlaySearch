from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader
from bs4 import BeautifulSoup
import requests

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))

def search(request):
	return HttpResponse('Hi There!')