from django.shortcuts import render
import requests

from weather.models import City
from .forms import CityForm


def index(request):
    appid = '90d9088ba4add0f831fd2f3904a20649'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()
    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'feels_like': res['main']['feels_like'],
            'humidity': res['main']['humidity'],
            'speed': res['wind']['speed'],
            'all': res['clouds']['all'],
            'pressure': res['main']['pressure'],
            'icon': res['weather'][0]['icon'],
        }

        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}

    return render(request, 'weather/index.html', context)
