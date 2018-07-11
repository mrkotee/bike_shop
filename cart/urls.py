from django.conf.urls import url, include
from mainapp.views import cart

urlpatterns = [
    url(r'^$', cart, name='cart'),
    url('', include('easycart.urls'))
]