from classes.json_saver import JSONSaver
from utils import search_by_name, view_vacancies, sorted_by_city, value_for_show, sorted_by_salary

json_saver = JSONSaver()


def user_interaction():
    search_query = input("Введите название вакансии для поиска: ")

    searched_vacancies = search_by_name(search_query)

    print(
        f"По заданному параметру найдено {len(searched_vacancies)} вакансий, повторите ваш запрос или введите цифру "
        f"exit для завершения программы")
    while len(searched_vacancies) == 0:
        search_query = input("Введите название вакансии для поиска: ")
        if search_query == "exit":
            print("Программа завершена...")
            exit()

        searched_vacancies = search_by_name(search_query)
        print(f"По заданному параметру найдено {len(searched_vacancies)} вакансий")

    while True:
        user_answer = input(f"Выберите действие (введите номер):\n"
                            f"1 - показать найденные вакансии:\n"
                            f"2 - ввести количество вакансий для отображения:\n"
                            f"3 - отфильтровать по городу: \n"
                            f"4 - показать топ-10 вакансий по зарплатам: \n")
        if user_answer == "1":
            view_vacancies(searched_vacancies)
            user_answer = input(f"Выберите действие (введите номер):\n"
                                f"1 - отсортировать по зарплате:\n"
                                f"2 - сохранить \n")
            if user_answer == "1":
                view_vacancies(sorted_by_salary(searched_vacancies))
                user_answer = input(f"Выберите действие (введите номер):\n"
                                    f"1 - сохранить \n")
                if user_answer == "1":
                    json_saver.save_vacancies(sorted_by_salary(searched_vacancies))
                    print(f"Данные сохранены! Программа завершена...")
                    break
            elif user_answer == "2":
                json_saver.save_vacancies(searched_vacancies)
                print(f"Данные сохранены! Программа завершена...")
                break

        elif user_answer == "2":
            user_answer = int(
                input(f'Сколько вакансий отобразить (введите значение от 1 до {len(searched_vacancies)}): '))
            vacancies = value_for_show(searched_vacancies, user_answer)
            view_vacancies(vacancies)

            user_answer = input(f"Выберите действие (введите номер):\n"
                                f"1 - отсортировать по зарплате:\n"
                                f"2 - сохранить \n")
            if user_answer == "1":
                view_vacancies(sorted_by_salary(vacancies))
                user_answer = input(f"Выберите действие (введите номер):\n"
                                    f"1 - сохранить \n")
                if user_answer == "1":
                    json_saver.save_vacancies(sorted_by_salary(vacancies))
                    print(f"Данные сохранены! Программа завершена...")
                    break
            elif user_answer == "2":
                json_saver.save_vacancies(vacancies)
                print(f"Данные сохранены! Программа завершена...")
                break

        elif user_answer == "3":
            user_input = input(f"Введите название города: ")
            sort_result = sorted_by_city(searched_vacancies, user_input)
            user_input = int(input(f"Выберите действие: \n"
                                   f"1 - отобразить найденное\n"))
            if user_input == 1:
                view_vacancies(sort_result)
                user_answer = input(f"Выберите действие (введите номер):\n"
                                    f"1 - отсортировать по зарплате:\n"
                                    f"2 - сохранить \n")
                if user_answer == "1":
                    view_vacancies(sorted_by_salary(sort_result))
                    user_answer = input(f"Выберите действие (введите номер):\n"
                                        f"1 - сохранить \n")
                    if user_answer == "1":
                        json_saver.save_vacancies(sorted_by_salary(sort_result))
                        print(f"Данные сохранены! Программа завершена...")
                        break
                elif user_answer == "2":
                    json_saver.save_vacancies(sort_result)
                    print(f"Данные сохранены! Программа завершена...")
                    break

        elif user_answer == "4":
            sort_result = sorted_by_salary(searched_vacancies)
            view_vacancies(sort_result[-10:])
            user_answer = input(f"Выберите действие (введите номер):\n"
                                f"1 - сохранить\n")
            if user_answer == "1":
                json_saver.save_vacancies(sort_result[-10:])
                print(f"Данные сохранены! Программа завершена...")
                break
        else:
            print('Выбрано недопустимое действие, введите правильный номер действия\n')


if __name__ == "__main__":
    user_interaction()
