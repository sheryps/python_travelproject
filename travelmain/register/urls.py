from django.urls import path
from . import views
urlpatterns = [
    path('register',views.register,name='register'),
    path('login',views.loginn,name='loginn'),
    path('logout',views.logout,name='logout')
]