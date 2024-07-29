
from django.urls import path
from . import views
urlpatterns = [
    path('',views.signin,name=''),
    path('signin/',views.signin,name='signin'),
    path('signout/',views.singout,name='signout'),
    path('home/',views.home,name='home'),
]
