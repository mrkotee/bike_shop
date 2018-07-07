from django.conf.urls import url
from .views import edit_bike

urlpatterns = [
    url(r'^bike/edit/(\d+)$', edit_bike),
]