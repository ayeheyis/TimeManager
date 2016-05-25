from django.conf.urls import url
from TimeManager.views import *

urlpatterns = [
    url(r'^register$', register, name="register"),
    url(r'^login$', 'django.contrib.auth.views.login', {'template_name':'login.html'}, name="login"),
    url(r'^logout$', 'django.contrib.auth.views.logout_then_login', name='logout'),
    url(r'^home$', home, name="home"),
    url(r'^task$', task, name="task"),
    url(r'^task_form$', task_form, name="task_form"),
    url(r'^$', home, name="home")
]