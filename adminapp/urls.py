from django.conf.urls import url, include
from .views import admin_page, contact_messages, user_manage, bikes_manage

urlpatterns = [
    url(r'^$', admin_page, name='myadmin'),
    url(r'^messages/$', contact_messages),
    url(r'^users/$', user_manage),
    url(r'^bikes/$', bikes_manage),
    url(r'^product/', include('productmanage.urls')),
]