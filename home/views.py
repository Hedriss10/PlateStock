from django.shortcuts import render

# Create your views here.

#home
def request_home(request):
    return render(request, 'home.html')

