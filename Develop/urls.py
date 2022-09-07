from django.urls import path
from Develop import views

urlpatterns = [
  
    path('',views.index, name = 'Home'),
    path('index',views.index, name = 'index'),
    path('about',views.about, name = 'About'),
    path('contact',views.contact, name = 'Contact'),
    path('courses', views.courses, name = 'Courses'),
    path("login", views.login_request, name="login"),
    path("register", views.register_request, name="register"),
    path("logout", views.logout_request, name= "logout"),
    path('search', views.search, name = 'search'),
]
