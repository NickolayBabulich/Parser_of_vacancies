from datetime import datetime
from classes.api_objects import SuperJobAPI
from classes.api_objects import HeadHunterAPI
from classes.vacancy import Vacancy

# Создаем экземпляры классов для работы с методами API
hh_api = HeadHunterAPI()
sj_api = SuperJobAPI()


def search_by_name(search_query):
    """
    Функция для поиска и парсинга данных с сайтов
    :param search_query: Название вакансии для поиска
    :return: Возвращаем отсортированные по дате вакансии с сайтов
    """
    # Передаем поисковое слово для парсинга
    hh_vacancies = hh_api.get_vacancies(search_query)
    # Создаем экземпляры класса найденных вакансий с HH
    Vacancy.vacancies_from_hh(hh_vacancies)

    # Передаем поисковое слово для парсинга
    sj_vacancies = sj_api.get_vacancies(search_query)
    # Создаем экземпляры класса найденных вакансий с SJ
    Vacancy.vacancies_from_sj(sj_vacancies)

    # Получаем массив со всеми отпарсенными данными
    load_vacancies = Vacancy.all_vacancies
    vacancies_data = []

    # Преобразуем найденные экземпляры классов в словарь для хранения и работы с данными
    for vacancy in load_vacancies:
        vacancies_data.append(vacancy.__dict__)

    # Преобразуем дату для сортировки
    for vacancy in vacancies_data:
        vacancy['published'] = datetime.strptime(vacancy['published'], "%d.%m.%Y %H:%M")

    # Сортируем по дате размещения вакансий
    sort_vacancies_data = sorted(vacancies_data,
                                 key=lambda x: x.get('published'),
                                 reverse=False)

    # Преобразуем дату к привычному виду
    for vacancy in vacancies_data:
        vacancy['published'] = datetime.strftime(vacancy['published'], "%d.%m.%Y %H:%M")

    return sort_vacancies_data


def format_salary(data):
    """
    Функция для форматирования зарплаты
    :param data: Данные вакансий с зарплатами
    :return:
    """
    for vacancy in data:
        if vacancy.get("salary_from") is None:
            vacancy["salary_from"] = 0
        elif vacancy.get("salary_to") is None:
            vacancy["salary_to"] = ''


def view_vacancies(data):
    """
    Функция для отображения полученных данных в форматированном виде
    :param data: Данные вакансий
    :return:
    """
    for vacancy in data:
        format_salary(data)
        print(f"Дата публикации: {vacancy['published']}\n"
              f"Вакансия: {vacancy['vacancy_name']}\n"
              f"Зарплата: {vacancy['salary_from']} - {vacancy['salary_to']}\n"
              f"Город: {vacancy['city']}\n"
              f"Обязанности: {vacancy['responsibility']}\n"
              f"Требования: {vacancy['requirement']}\n"
              f"Ссылка на вакансию: {vacancy['url']}\n"
              f"--------------------------------------\n")


def value_for_show(data, value):
    """
    Функция для отображения определенного количества вакансий
    :param data: Данные вакансий
    :param value: Количество вакансий для отображения
    :return: Возвращает результат с данными
    """
    result = []
    for vacancy in range(0, len(data)):
        result.append(data[vacancy])
    return result[-value:]


def sorted_by_city(data, city):
    """
    Функция фильтрации вакансий в соответствии с заданным городом
    :param data: Данные вакансий
    :param city: Город для фильтрации
    :return: Возвращает результат с вакансиями в заданном городе
    """
    sort_result = []
    for vacancy in data:
        if city == vacancy['city']:
            sort_result.append(vacancy)
    print(f"В городе {city} найдены {len(sort_result)} вакансии")

    return sort_result


def sorted_by_salary(data):
    """
    Функция сортировки вакансий по заработной плате от самой наивысшей
    :param data: Данные вакансий
    :return: Возвращает отсортированные данные
    """
    format_salary(data)
    sort_vacancies_data = sorted(
        data,
        key=lambda x: x["salary_from"],
        reverse=False
    )
    return sort_vacancies_data
