from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader
from bs4 import BeautifulSoup
import requests
import pandas as pd

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))

def search(request):
	if request.method == 'POST':
		url  = 'https://play.google.com/store/search?q='+request.POST.get('qry')+'&c=apps'
		raw  = requests.get(url)
		soup = BeautifulSoup(raw.text, 'html.parser')
		# apps = soup.find("div", {"class": "card-list"})
		apps = soup.find_all(class_="card-content")
		# print(apps[0].prettify())
		for ids in apps:
			app_id = ids.find("span", {"class": "preview-overlay-container"})['data-docid']
			app_name = ids.find("img", {"class": "cover-image"})['alt']
			cover_image = ids.find("img", {"class": "cover-image"})['src']
			dev_name = ids.find(class_="subtitle").get_text()
			app_details = pd.DataFrame({
		        "app_id": [app_id], 
		        "app_name": [app_name], 
		        "cover_image": [cover_image], 
		        "dev_name":[dev_name]
		    })
			print (app_details)

		return HttpResponse("<pre>"+app_details+"</pre>")