from django.shortcuts import render, get_object_or_404, redirect
from .models import Main
from news.models import News
# Create your views here.


def home(request):
    # sitename = "My Site | Home"
    # site = Main.objects.all()
    # site = Main.objects.filter(pk=1)
    site = Main.objects.get(pk=1)
    news = News.objects.all()

    return render(request, 'front/home.html', {'site':site ,'news':news}) #{'sitename':sitename}

def about(request):
    # sitename = "My Site | About"
    site = Main.objects.get(pk=1)

    return render(request, 'front/about.html', {'site':site}) #{'sitename':sitename}

def panel(request):


    return render(request, 'back/home.html')


