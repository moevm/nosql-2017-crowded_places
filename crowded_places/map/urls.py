from django.urls import path
#from django.conf.urls import url
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', views.index, name='index'),
    path('index', TemplateView.as_view(template_name='/home/nick1/mygit/nosql-2017-crowded_places/crowded_places/map/templates/map_page.html'), name='index'),
    #url(r'^students', students, name='students'),
]