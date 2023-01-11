from . import views
from django.urls import path

urlpatterns = [
    path('', views.main, name="main"),
    path('area', views.area, name="area"),
    path('demand', views.demand, name="demand"),
    path('skills', views.skills, name="skills"),
    path('last_vacancies', views.last_vacancies, name="last_vacancies"),
]
