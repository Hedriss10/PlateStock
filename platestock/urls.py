from django.contrib import admin
from django.urls import path, include



#adicionando a urls do home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
]
