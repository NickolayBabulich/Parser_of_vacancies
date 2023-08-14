from abc import ABC, abstractmethod

import json
import os

FILENAME = os.path.join("database", "database.json")


class Engine(ABC):
    """Абстрактный класс для работы с методами добавления вакансий в файл"""

    @abstractmethod
    def save_vacancies(self, data):
        pass


class JSONSaver(Engine):
    """Класс для сохранения данных в JSON"""

    def save_vacancies(self, data):
        if not os.path.isdir("database"):
            os.mkdir("database")
        with open(FILENAME, "w") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
