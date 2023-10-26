from django.urls import path
from . import views

app_name = 'soccers'
urlpatterns = [
    path('teams/',views.matchup_info,name='matchup_info'),
]
