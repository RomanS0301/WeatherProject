from django.shortcuts import render
import requests


def index(request):
    appid = '90d9088ba4add0f831fd2f3904a20649'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    city = 'Brest'
    res = requests.get(url.format(city))
    print(res.text)
    return render(request, 'weather/index.html')



