# Golubovich Igor for Python Course | homework №8 | task №1


from sqlalchemy import create_engine
from sqlalchemy.sql.expression import select
from sqlalchemy.sql.schema import Column, MetaData, Table
from sqlalchemy.sql.sqltypes import Integer, String
 
engine = create_engine('sqlite:///Homework/lesson_8_db/hm_db.db', echo=True)
conn = engine.connect()
meta = MetaData()

universities = Table(
    'universities', meta,
    Column('id', Integer, primary_key=True),
    Column('name_university', String),
)

faculties = Table(
    'faculties', meta,
    Column('id', Integer, primary_key=True),
    Column('name_faculties', String),
    Column('id_university', Integer),
)

specialities = Table(
    'specialities', meta,
    Column('id', Integer, primary_key=True),
    Column('name_specialities', String),
    Column('id_faculty', Integer),
)

subjects = Table(
    'subjects', meta,
    Column('id', Integer, primary_key=True),
    Column('name_subjects', String),
    Column('id_speciality', Integer),
)

students = Table(
    'students', meta,
    Column('id', Integer, primary_key=True),
    Column('first_name', String),
    Column('last_name', String),
    Column('id_speciality', Integer),
)

meta.create_all(engine)



# conn.execute(
#     universities.insert(),
#     [
#         {'name_university': 'БНТУ'},
#         {'name_university': 'БГУ'},
#         {'name_university': 'БГУИР'},
#     ]
# )



# conn.execute(
#     faculties.insert(),
#     [
#         {'name_faculties': 'АТФ', 'id_university': '1'},
#         {'name_faculties': 'МСФ', 'id_university': '1'},
#         {'name_faculties': 'ФПМИ', 'id_university': '2'},
#         {'name_faculties': 'ЮФ', 'id_university': '2'},
#         {'name_faculties': 'КСИС', 'id_university': '3'},
#         {'name_faculties': 'ФИТУ', 'id_university': '3'},
#     ]
# )


# conn.execute(
#     specialities.insert(),
#     [
#         {'name_specialities': 'Автомобилестроение', 'id_faculty': '1'},
#         {'name_specialities': 'Технология машиностроения', 'id_faculty': '2'},
#         {'name_specialities': 'Компьютерная безопасность', 'id_faculty': '3'},
#         {'name_specialities': 'Адвокатура и нотариат', 'id_faculty': '4'},
#         {'name_specialities': 'Электронные вычислительные средства', 'id_faculty': '5'},
#         {'name_specialities': 'Искусственный интеллект', 'id_faculty': '6'},
#     ]
# )


# conn.execute(
#     subjects.insert(),
#     [
#         {'name_subjects': 'Транспорт', 'id_speciality': '1'},
#         {'name_subjects': 'Материаловедение и технология материалов', 'id_speciality': '2'},
#         {'name_subjects': 'Компьютерные сети', 'id_speciality': '3'},
#         {'name_subjects': 'Правоведение', 'id_speciality': '4'},
#         {'name_subjects': 'Администрирование компьютерных систем и сетей', 'id_speciality': '5'},
#         {'name_subjects': 'Дискретная математика', 'id_speciality': '6'},
#     ]
# )



# conn.execute(
#     students.insert(),
#     [
#         {'first_name': 'Чук', 'last_name': 'Петров','id_speciality': '1'},
#         {'first_name': 'Гек', 'last_name': 'Баширов','id_speciality': '1'},
#         {'first_name': 'Лайза', 'last_name': 'Путина','id_speciality': '2'},
#         {'first_name': 'Гуф', 'last_name': 'Петрович','id_speciality': '2'},
#         {'first_name': 'Джони', 'last_name': 'Иванов','id_speciality': '3'},
#         {'first_name': 'Сара', 'last_name': 'Конор','id_speciality': '3'},
#         {'first_name': 'Коля', 'last_name': 'Гагарин','id_speciality': '4'},
#         {'first_name': 'Брэд', 'last_name': 'Грусный','id_speciality': '4'},
#         {'first_name': 'Петя', 'last_name': 'Козловский','id_speciality': '5'},
#         {'first_name': 'Оля', 'last_name': 'Куценко','id_speciality': '5'},
#         {'first_name': 'Жан', 'last_name': 'Жак','id_speciality': '6'},
#         {'first_name': 'Оливье', 'last_name': 'Буру','id_speciality': '6'},
#     ]
# )


# st = universities.insert().values(name_university='БГЭУ')

# st = faculties.insert().values(name_faculties='Экономики и менеджмента', id_university='4')

# st = specialities.insert().values(name_specialities='Государственное управление', id_faculty='7')

# st = students.insert().values(first_name='Иван', last_name='Матроскин', id_speciality='7')

# print(st)
 
# conn = engine.connect()
# result = conn.execute(st)
# print(result)


# j = students.join(specialities, students.c.id_speciality == specialities.c.id)
# stmt = select([students.c.first_name ,students.c.last_name , specialities.c.name_specialities]).select_from(j).where(students.c.id_speciality == 4)
# print(stmt)
# result = conn.execute(stmt)
# print([row for row in result])


j = students.join(specialities, students.c.id_speciality == specialities.c.id)
stmt = select([students.c.first_name ,students.c.last_name , specialities.c.name_specialities]).select_from(j).where(specialities.c.name_specialities == 'Компьютерная безопасность')
print(stmt)
result = conn.execute(stmt)
print([row for row in result])


# s = students.select()
# print(s)
 
# result = conn.execute(s)
# print(result.fetchall())