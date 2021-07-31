from django.urls import path
from CSN import views

urlpatterns = [
    path("", views.login, name="login"),
     path('login_info',views.login_info),
     path('sign_up',views.sign_up),
     path('logout',views.logout),
     path('register',views.register),
     path('profile',views.profile),
]