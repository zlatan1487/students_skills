# иморт модуля json
import json

# список используется в функции "get_student_by_pk", в STUDENT_INFO сохраняеться информация о студенте
# список импортирован в main.py
STUDENT_INFO = []


def load_students():
    """
    :return: возвращает список студентов из файла students.json
    """
    with open('DATA/students.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def load_professions():
    """
    :return: возвращает список специальностей из файла professions.json
    """
    with open('DATA/professions.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def get_student_by_pk(search_student):
    """
        функция осуществляет поиск студента по номеру и формирует объект STUDENT_INFO
    :param search_student: номер студента
    :return: возвращает объект STUDENT_INFO
    """
    student_list = load_students()
    if search_student in [x['pk'] for x in student_list]:
        print(f'''Студент: {student_list[search_student - 1]['full_name']}''' '\n'f'''Знает:  {', '.join(student_list[search_student - 1]['skills'])}''')
        STUDENT_INFO.append([student_list[search_student - 1]['full_name'], student_list[search_student - 1]['skills']])
    else:
        print('У нас нет такого студента')
        quit()


def get_profession_by_title(search_profession):
    """
        функция осуществляет поиск специальностей по их названию  и формирует список из них
    :param search_profession:
    :return: возвращает список скиллов
    """
    profession_list = load_professions()
    if search_profession in [x['title'] for x in profession_list]:
        return [x['skills'] for x in profession_list if x['title'] == search_profession]
    else:
        print('У нас нет такой специальности')
        quit()


# вспамогательная функция "list_transformation" для распоковки объкта в один список типа "[]" из "[[]]"
# используеться в main.py
def list_transformation(list_):
    return [item for sublist in list_ for item in sublist]


def create_final_list(name, has, lacks, skills_list):
    """
        функция формирует конечный обьект с данными о возможнастях студента,
        запускает функцию "get_info" с параметром объекта для отображения данных в консоли
    :param name: имя студента
    :param has: список навыков которыми владеет студент
    :param lacks: список отсутствующих навыков
    :param skills_list: список всех навыков, перечисленных в professions.json
    :return: запускает функцию "get_info(calculated_list)"
    """
    calculated_list = {}

    percent = f'{int(len(has) / len(skills_list) * 100)}%'
    calculated_list["name"] = name
    calculated_list["has"] = list(has)
    calculated_list["lacks"] = list(lacks)
    calculated_list["fit_percent"] = percent

    get_info(calculated_list)


def get_info(info):
    """
        функция для отображения информации в консоли
    :param info: конечный обьект с данными о студенте и его навыках
    :return:
    """
    text = 'нет таких предметов'
    lacks = [', '.join([i for i in info['lacks']]) if info['lacks'] else text]
    has = [', '.join([i for i in info['has']]) if info['has'] else text]

    print(f'''Пригодность: {info['fit_percent']}''')
    print(f'''{info['name']} знает: {', '.join(has)}''')
    print(f'''{info['name']} не знает: {', '.join(lacks)}''')
