
from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.index, name='index'),
    path('impressum/', views.impressum_view, name='impressum'),
    path('information/', views.information, name='information'),

    # Other URL patterns for the events app
]

