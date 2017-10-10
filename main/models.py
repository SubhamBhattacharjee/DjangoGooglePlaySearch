from __future__ import unicode_literals
from datetime import datetime
from django.db import models

class SearchString(models.Model):
	searchstring = models.CharField(max_length=250)
	searched_time = models.DateTimeField(default=datetime.now())
	amount_of_time_searched = models.IntegerField(default='0')

	def __str__(self):
		return "%s - %s" % (self.searchstring, self.amount_of_time_searched)

class Result(models.Model):
	app_id = models.CharField(max_length=250)
	app_name = models.CharField(max_length=250)
	dev_name = models.CharField(max_length=250)
	app_icon = models.CharField(max_length=250)
	searched_by = models.ForeignKey(SearchString)

	def __str__(self):
		return "%s - %s" % (self.app_name, self.app_id)