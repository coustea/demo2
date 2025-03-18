from django.urls import path
from .views import *
urlpatterns = [
    path('',UserView.as_view(),name='users'),
    path("test/",UsersViewTest.as_view(),name='usersTest'),
    path("<int:pk>/",UsersDetailView.as_view(),name='usersDetail'),
    path("login/",LoginView.as_view(),name='login'),
    path("register/",RegisterView.as_view(),name='register')
]