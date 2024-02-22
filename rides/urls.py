from django.urls import path
from . import views

app_name = 'rides'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),  # Add this line for the about page
]
