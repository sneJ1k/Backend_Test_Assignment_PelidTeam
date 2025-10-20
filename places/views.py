from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Добро пожаловать на API карты!</h1>")
