from django.conf.urls import url
from . import views
app_name = 'main'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/', views.search, name="search"),
    url(r'^details/(?P<result_id>[0-9]+)', views.details, name="details")
]