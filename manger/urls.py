from django.urls import path
from .views import *
urlpatterns = [
    path("",MangerView.as_view(),name='manger')
]