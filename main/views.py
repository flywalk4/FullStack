from django.shortcuts import render

def main(request):
    return render(request, 'main/main.html', {"title" : "Главная страница"})

def area(request):
    return render(request, 'area/area.html', {"title" : "area страница"})

def demand(request):
    return render(request, 'demand/demand.html', {"title" : "demand страница"})

def skills(request):
    return render(request, 'skills/skills.html', {"title" : "skills страница"})

def last_vacancies(request):
    return render(request, 'last_vacancies/last_vacancies.html', {"title" : "last_vacancies страница"})