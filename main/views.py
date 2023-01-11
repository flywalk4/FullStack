from django.shortcuts import render
from .models import  Main, Demand, Area, Skills
from . import apihh

def main(request):
    return render(request, 'main/main.html', {"title" : "Главная страница", "content": Main.objects.all()})

def area(request):
    return render(request, 'area/area.html', {"title" : "География", "content": Area.objects.all()})

def demand(request):
    return render(request, 'demand/demand.html', {"title" : "Востребованность", "content": Demand.objects.all()})

def skills(request):
    return render(request, 'skills/skills.html', {"title" : "Навыки", "content": Skills.objects.all()})

def last_vacancies(request):
    vacancies = apihh.get()
    return render(request, 'last_vacancies/last_vacancies.html', {"title" : "Последние вакансии", "vacancies": vacancies})