import requests
import json
import csv
import datetime
from time import sleep


def request_vacancies():
    """ Возвращает запрос c https://api.hh.ru
        Args:
            date_from(datetime): дата начала
            date_to(datetime): дата конца
            page(int): страница
        Returns:
            request: Ответ сервера

    hour_from = str(date_from.hour).zfill(2)
    hour_to = str(date_to.hour).zfill(2)
    day_from = str(date_from.day).zfill(2)
    day_to = str(date_to.day).zfill(2)
    minute_from = str(date_from.minute).zfill(2)
    minute_to = str(date_to.minute).zfill(2)
    second_from = str(date_from.second).zfill(2)
    second_to = str(date_to.second).zfill(2)"""
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


def input_datetime():
    """Получаем нужный день
        Returns:
            datetime: Нужный день
    """
    year = 2022
    month = 12
    day = 10
    day = 22 if day == "" else int(day)
    return datetime.datetime(year, month, day)


def get_day_range(date: datetime):
    """Получаем список нужных дат
        Args:
            date(datetime): Требуемый день
        Returns:
            [datetime, datetime]: Временной промежуток
    """
    day_range = []
    for hour in range(1, 25):
        if hour == 24:
            day_range.append([datetime.datetime(date.year, date.month, date.day, 23, 0, 0),
                              datetime.datetime(date.year, date.month, date.day, 23, 59, 59)])
            continue
        day_range.append([datetime.datetime(date.year, date.month, date.day, hour - 1, 0, 0),
                          datetime.datetime(date.year, date.month, date.day, hour, 0, 0)])
    return day_range


def make_requests(day_range):
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




def get():
    items = make_requests(get_day_range(input_datetime()))
    out = []
    for item in items:
        request = requests.get(f'https://api.hh.ru/vacancies/{item["id"]}')
        if request.status_code == 200:
            out.append(json.loads(request.text))
        if len(out) == 10:
            break
    return out