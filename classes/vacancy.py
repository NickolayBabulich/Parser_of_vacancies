from datetime import datetime


class Vacancy:
    """Класс для работы с вакансиями"""

    all_vacancies = []

    def __init__(self, vacancy_name, salary_from, salary_to, city, responsibility, requirement, url, published):
        self.vacancy_name = vacancy_name
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.city = city
        self.responsibility = responsibility
        self.requirement = requirement
        self.url = url
        self.published = published

    @classmethod
    def vacancies_from_hh(cls, data):
        """Метод для создания экземпляров классов вакансий с данными из HeadHunter"""

        for vacancy in data:
            cls.all_vacancies.append(Vacancy
                                     (vacancy_name=vacancy["name"],
                                      salary_from=vacancy["salary"]["from"],
                                      salary_to=vacancy["salary"]["to"],
                                      city=vacancy["area"]["name"],
                                      responsibility=vacancy["snippet"]["responsibility"],
                                      requirement=vacancy["snippet"]["requirement"],
                                      url=vacancy["alternate_url"],
                                      published=datetime.fromisoformat(vacancy['published_at']).strftime(
                                          "%d.%m.%Y %H:%M")))

    @classmethod
    def vacancies_from_sj(cls, data):
        """Метод для создания экземпляров классов вакансий с данными из SuperJob"""

        for vacancy in data:
            cls.all_vacancies.append(Vacancy
                                     (vacancy_name=vacancy['profession'],
                                      salary_from=vacancy['payment_from'],
                                      salary_to=vacancy['payment_to'],
                                      city=vacancy['town']['title'],
                                      responsibility=vacancy['vacancyRichText'],
                                      requirement=vacancy['candidat'],
                                      url=vacancy['link'],
                                      published=datetime.fromtimestamp(vacancy['date_published']).strftime(
                                          "%d.%m.%Y %H:%M")))

