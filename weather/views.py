from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.db import IntegrityError


def index(request):
    return render(request, 'weather/index.html')


def signupuser(request):
    """
    Создание нового пользователя, проверка на совпадение паролей, проверка на уникальность пользователя, запрет на
    посещение пользователем админ панели, перенаправление пользователя на страницу с текущими задачами
    """
    return render(request, 'weather/signupuser.html')
