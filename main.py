
# импорт функций из модуля UTILS
from UTILS.utils import get_student_by_pk, get_profession_by_title, STUDENT_INFO, create_final_list, list_transformation

# начало/запуск программы
if __name__ == '__main__':

    # поиск студента по номеру
    search_student_by_pk = input('Введите номер студента ')

    # проверка на тип данных возвращаемой переменной "search_student_num"
    # если возвращает строку, программа завершает свою работу
    try:
        search_student = get_student_by_pk(int(search_student_by_pk))
    except ValueError:
        print(f"{search_student_by_pk} не являеться номером студента, введите номер.")
        quit()

    # поиск специальности
    search_profession = input(f'''Выберите специальность для оценки студента {(STUDENT_INFO[0][0])} ''')


    def check_fitness(people, skills):
        """
        функция множества, сопоставляет список навыков студента и предоставленных специальностей
        :param people:
        :param skills:
        :return: функция передает параметры в функцию "create_final_list" для формирования итогового списка
        """
        print()

        # вспамогательная функция "list_transformation" для распоковки объкта в один список, для удобства при дальнейшем использовании,
        # сохраняет в переменные "people_list" & "skills_list" соответственно.
        people_list = list_transformation(people)
        skills_list = list_transformation(skills)

        # вычисления разницы список навыков студента и специальностей из файла professions.json с помощью множеств - "intersection" & "difference".
        # результаты записуються в переменные intersection_ & difference_ соответственно.
        people_, skills_ = set(people_list[1]), set(skills_list)
        intersection_, difference_ = people_.intersection(skills_), skills_.difference(people_)

        # функцию "create_final_list" для формирования итогового списка находится в папке UTILS, файла utils.py
        # в функцию передаються следующие параметры: people_list[0] - имя студента,
        # intersection_ - названия навыков студента перечисленные в professions.json,
        # difference_ - специальности которыми студент не владеет.
        create_final_list(people_list[0], intersection_, difference_, skills_list)

    # STUDENT_INFO объект импортирован из папки UTILS, файла utils.py, объект представляет результат поиска по "pk", искомому номеру студента
    # и возвращает информацию о нем
    student = STUDENT_INFO

    # функция "get_profession_by_title" возвращает объект со специальностями, сохраняеться в переменную "profession"
    profession = get_profession_by_title(search_profession.title())

    # запуск функии "check_fitness" с известными параметрами
    check_fitness(student, profession)

