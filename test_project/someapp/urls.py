from django.conf.urls import url
from django.urls import path

from .views import SomeModelView, index

urlpatterns = [
    path('index/', index),
    path('', SomeModelView.as_view())
]
