from django.conf.urls import url
from .views import saluda

urlpatterns = [
    url(r'^saluda/', saluda),
]
