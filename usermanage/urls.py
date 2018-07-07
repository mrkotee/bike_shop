from django.conf.urls import url
from .views import login, logout, registration, userpage, delete, edit

urlpatterns = [
    url(r'^(\d+)$', userpage),
    url(r'^login/$', login),
    url(r'^logout/$', logout),
    url(r'^registration/$', registration),
    url(r'^delete/(\d+)/$', delete),
    url(r'^edit/(\d+)/$', edit),
]