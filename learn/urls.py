from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^(?P<w>[\w-]+)/$', views.word, name='word'),
]