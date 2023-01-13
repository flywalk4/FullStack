import requests
import json
import csv
import datetime
from time import sleep


def request_vacancies():
    request = requests.get('https://api.hh.ru/vacancies',
                           params={'specialization': 1,
                                   "text" : "FullStack",
                                   "text": "fullstack",
                                   "text": "Full Stack",
                                   'date_from': f"2022-12-22T00:00:00",
                                    'date_to': f"2022-12-22T23:59:59"})
    return request


def form_vacancy(item):
    """ Возвращает вакансию в виде массива
        Args:
            item(dict): Вакансия
        Returns:
            list: Вакансия в обработанном виде
    """
    try:
        salary_from = item["salary"]["from"]
    except:
        salary_from = ""

    try:
        salary_to = item["salary"]["to"]
    except:
        salary_to = ""

    try:
        salary_currency = item["salary"]["currency"]
    except:
        salary_currency = ""

    try:
        area_name = item["address"]["city"]
    except:
        area_name = ""

    return [item["name"], salary_from, salary_to, salary_currency, area_name, item["published_at"]]


def make_requests():
    """Возвращает все вакансии за определенный день
        Args:
            day_range(list): Список параметров для запроса
        Return:
            list: Все вакансии
    """
    items = []
    request = request_vacancies()
    if "captcha_url" in request.text:
        print("Пройдите капчу чтобы продолжить: ")
        print(json.loads(request.text)["errors"][0]["captcha_url"])
        input("Нажмите после ввода капчи")
    if request.status_code == 200:
        items += json.loads(request.text)["items"]
    else:
        print("Request rejected, retrying")
        request = request_vacancies()
        if request.status_code == 200:
            items += json.loads(request.text)["items"]
        else:
            pass
    return items

def fix_date(vacancy):
    vacancy["published_at"] = " ".join(str(vacancy["published_at"]).split("T")).split("+")[0]
    return vacancy
def get():
    items = make_requests()
    out = []
    for item in items:
        request = requests.get(f'https://api.hh.ru/vacancies/{item["id"]}')
        if request.status_code == 200:
            out.append(json.loads(request.text))
        if len(out) == 10:
            break
    out = list(map(lambda x: fix_date(x), out))
    return sorted(out, key=lambda x: x["published_at"])