"""bike_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from mainapp.views import main, parts, bicycles, accessories, single, send_message


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', main, name='index'),
    url(r'^bicycles/$', bicycles, name='bicycles'),
    url(r'^parts/$', parts, name='parts'),
    url(r'^accessories/$', accessories, name='accessories'),
    url(r'^cart/', include('cart.urls')),
    url(r'^single/(\d+)$', single, name='single'),
    url(r'^sendmessage/$', send_message),
    url(r'^user/', include('usermanage.urls')),
    url(r'^myadmin/', include('adminapp.urls')),
]

# handler404 = 'mysite.views.my_custom_404_view'

if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

