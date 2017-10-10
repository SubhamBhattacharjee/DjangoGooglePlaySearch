from __future__ import unicode_literals
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from .models import Result, SearchString
import sys

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))

def search(request):
	if request.method == 'POST':
		if SearchString.objects.filter(searchstring = request.POST.get('qry')).exists():

			searchstr = SearchString.objects.filter(searchstring = request.POST.get('qry')).get()
			searchstr.amount_of_time_searched += 1
			searchstr.save()
			result_list = Result.objects.filter(searched_by__searchstring__exact = request.POST.get('qry'))

			return render(request, 'result_list.html', {
				'result_list': result_list
			})

		else:
			url  = 'https://play.google.com/store/search?q='+request.POST.get('qry')+'&c=apps'

			try:
				raw  = requests.get(url)
				soup = BeautifulSoup(raw.text, 'html.parser')
				apps = soup.find_all(class_="card-content")
				searchstr = SearchString(searchstring=request.POST.get('qry').lower(), amount_of_time_searched=1)
				searchstr.save()
			except requests.exceptions.RequestException as e:
				print(e)
				sys.exit(1)

			ids = []
			for app in apps[:10]:
				app_id = app.find("span", {"class": "preview-overlay-container"})['data-docid']
				app_name = app.find("img", {"class": "cover-image"})['alt']
				cover_image = app.find("img", {"class": "cover-image"})['src']
				dev_name = app.find(class_="subtitle").get_text()

				if Result.objects.filter(app_id = app_id).exists():
					toAppend = Result.objects.filter(app_id = app_id).get()
					ids.append(toAppend.id)
				else:
					res = Result(searched_by=searchstr, app_id=app_id, app_name=app_name, dev_name=dev_name, app_icon=cover_image)
					res.save()
					ids.append(res.id)

			result_list = Result.objects.filter(pk__in=ids)
			return render(request, 'result_list.html', {
				'result_list': result_list
			})

	
	return HttpResponseRedirect("/")

def details(request, result_id):
	if Result.objects.filter(pk = result_id).exists():

		result_list = Result.objects.filter(pk = result_id).get()
		return render(request, 'details.html', {
			'result_list': result_list
		})

	else:
		return render(request, 'details.html', {'error_message': 'Nothing Found!'})