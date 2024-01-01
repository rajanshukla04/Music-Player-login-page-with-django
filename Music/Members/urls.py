from django.urls import path,include
from .import views
from django.urls import path
from .views import your_django_signup_view

urlpatterns=[
    path('',views.home,name='home'),
     path('home',views.home,name='home'),
    path("login",views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('your_django_signup_view', your_django_signup_view, name='your_django_signup_view'),
    path('your_login_view',views.your_login_view,name='your_login_view'),
   
]