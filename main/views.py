from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader
from bs4 import BeautifulSoup
import requests
from .models import Result, SearchString

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))

def search(request):
	if request.method == 'POST':
		if SearchString.objects.filter(searchstring = request.POST.get('qry')).exists():
			return HttpResponse('Hoshwalo kya khabar bekhudi kya cheese he!')
		else:
			url  = 'https://play.google.com/store/search?q='+request.POST.get('qry')+'&c=apps'
			raw  = requests.get(url)
			soup = BeautifulSoup(raw.text, 'html.parser')
			apps = soup.find_all(class_="card-content")
			for ids in apps:
				app_id = ids.find("span", {"class": "preview-overlay-container"})['data-docid']
				app_name = ids.find("img", {"class": "cover-image"})['alt']
				cover_image = ids.find("img", {"class": "cover-image"})['src']
				dev_name = ids.find(class_="subtitle").get_text()
				res = Result(searched_by=request.POST.get('qry'), app_id=app_id, app_name=app_name, dev_name=dev_name, app_icon=cover_image)
				res.save()

		return HttpResponse("<pre>lool</pre>")