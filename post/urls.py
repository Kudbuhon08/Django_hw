from django.urls import path
from .views import *

urlpatterns = [
    path('hi/', hello),
    path('goodbye/', goodbye),
    path('time/', time),
    path('home/', home_page),
    path('about/', about),
]
