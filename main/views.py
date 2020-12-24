from django.shortcuts import render, get_object_or_404, redirect
from .models import Main
# Create your views here.


def home(request):
    # sitename = "My Site | Home"
    # site = Main.objects.all()
    # site = Main.objects.filter(pk=1)
    site = Main.objects.get(pk=1)

    return render(request, 'front/home.html', {'site':site}) #{'sitename':sitename}

def about(request):
    # sitename = "My Site | About"
    site = Main.objects.get(pk=1)

    return render(request, 'front/about.html', {'site':site}) #{'sitename':sitename}