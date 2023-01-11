from django.shortcuts import render
from .models import  Main
import asyncio
from . import apihh
def main(request):
    return render(request, 'main/main.html', {"title" : "Главная страница", "content": Main.objects.all()})

def area(request):
    return render(request, 'area/area.html', {"title" : "География"})

def demand(request):
    return render(request, 'demand/demand.html', {"title" : "Востребованность"})

def skills(request):
    return render(request, 'skills/skills.html', {"title" : "Навыки"})

def last_vacancies(request):
    vacancies = apihh.get()
    return render(request, 'last_vacancies/last_vacancies.html', {"title" : "Последние вакансии", "vacancies": vacancies})