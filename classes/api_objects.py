import os
import requests
from abc import ABC, abstractmethod

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())
SUPERJOB_API_KEY = os.getenv('SUPERJOB_API_KEY')


class APIObjects(ABC):
    """Абстрактный класс для работы с API сайтов."""

    @abstractmethod
    def get_vacancies(self, query: str):
        pass


class HeadHunterAPI(APIObjects):
    """Класс для получения вакансий с HeadHunter"""

    def get_vacancies(self, query: str):
        url = "https://api.hh.ru/vacancies"
        params = {"text": f"name:{query}",
                  "page": 0,
                  "per_page": 50,
                  "area": 113,
                  'only_with_salary': True}
        response = requests.get(url, params)
        response_data = response.json()
        vacancies = response_data["items"]
        while response_data["page"] != 2:
            params["page"] += 1
            response = requests.get(url, params)
            response_data = response.json()
            vacancies.extend(response_data["items"])

        return vacancies


class SuperJobAPI(APIObjects):
    """Класс для получения вакансий с SuperJob"""
    
    def get_vacancies(self, query: str):
        url = "https://api.superjob.ru/2.0/vacancies/"
        params = {"keywords": query,
                  "page": 0,
                  "count": 100,
                  'no_agreement': 1}
        headers = {"X-Api-App-Id": SUPERJOB_API_KEY}
        response = requests.get(url, params, headers=headers)
        response_data = response.json()
        vacancies = response_data["objects"]
        while params["page"] != 2:
            params["page"] += 1
            response = requests.get(url, params, headers=headers)
            response_data = response.json()
            vacancies.extend(response_data["objects"])

        return vacancies
