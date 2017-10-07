from __future__ import unicode_literals
from datetime import datetime
from django.db import models

class SearchString(models.Model):
	searchstring = models.CharField(max_length=250)
	searched_time = models.DateTimeField(default=datetime.now())
	amount_of_time_searched = models.CharField(max_length=100)

	def __str__(self):
		return self.searchstring + ' - ' + self.amount_of_time_searched

class Result(models.Model):
	searched_by = models.CharField(max_length=250)
	app_id = models.CharField(max_length=250)
	app_name = models.CharField(max_length=250)
	dev_name = models.CharField(max_length=250)
	app_icon = models.CharField(max_length=250)

	def __str__(self):
		return self.searched_by + ' - ' + self.app_id + ' - ' + self.app_name + ' - ' + self.dev_name + ' - ' + self.app_icon