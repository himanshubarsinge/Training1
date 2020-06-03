from django.conf.urls import url, include
from . import views

#We need to set a global name called app_name, django looks for this automatically
app_name = 'basic_app'

urlpatterns = [
    url(r'^relative/$', views.relative, name='relative'),
    url(r'^other/$', views.other, name='other'),
]
