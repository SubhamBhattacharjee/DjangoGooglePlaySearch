from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader
from bs4 import BeautifulSoup
import requests

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))

def search(request):
	if request.method == 'POST':
		url  = 'https://play.google.com/store/search?q='+request.POST.get('qry')+'&c=apps'
		raw  = requests.get(url)
		soup = BeautifulSoup(raw.text, 'html.parser')
		apps = soup.find_all(class_="card-content")
		for ids in apps:
			app_id = ids.find("span", {"class": "preview-overlay-container"})['data-docid']
			app_name = ids.find("img", {"class": "cover-image"})['alt']
			cover_image = ids.find("img", {"class": "cover-image"})['src']
			dev_name = ids.find(class_="subtitle").get_text()

		return HttpResponse("<pre>lool</pre>")