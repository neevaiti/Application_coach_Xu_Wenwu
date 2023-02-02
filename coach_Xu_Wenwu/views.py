from django.shortcuts import render
from django.http import HttpResponse


# Premier test de page en code dégueulasse
def home(request):
    return HttpResponse("<h1>Bienvenue chez le coach Xu Wenwu.</h1>")