from django.urls import path


#importando as views
from .views import request_home


#patterns
urlpatterns = [
    path('', request_home),
]

