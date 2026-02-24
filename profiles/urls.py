
from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_profile, name='add_profile'),
    path('',views.profile_home, name='profile_home'),
]
