from django.urls import path
from . import views

app_name = 'rides'
urlpatterns = [
    path('', views.index, name='index'),  # Keep this for your homepage.
    path('about/', views.test, name='about'),
    path('create/', views.create, name='create'),
    path('ai_interaction/', views.ai_interaction, name='ai_interaction'), 
]
