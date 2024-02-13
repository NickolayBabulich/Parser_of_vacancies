# Parser of vacancies

## Описание:

Программа парсит вакансии с сайта HH.ru и SuperJob.
В программе реализованны принципы ООП

## Технологии:

[![Python](https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
  [![JSON](https://img.shields.io/badge/-JSON-000000?style=flat&logo=json&logoColor=white)](https://www.json.org/)
  [![PyTest](https://img.shields.io/badge/-PyTest-0A9EDC?style=flat&logo=python&logoColor=white)](https://docs.pytest.org/) [![OOP](https://img.shields.io/badge/-OOP-FF5733?style=flat)](https://en.wikipedia.org/wiki/Object-oriented_programming)

## Реализовано:

- ввод конкретного слова для поиска по базе вакансий
- вывод найденных вакансий
- опциональный вывод определенного количества найденного
- фильтрация по городу
- сортировка топ-10 вакансий по зарплатам
- сохранение полученных результатов в JSON

## Дополнительно:

- для работы с API SuperJob необходимо зарегистрироваться на сайте и получить API ключ
- отредактировать .env.sample вставив полученный API ключ и переименовать файд в .env
- после запустить программу из файла main.py