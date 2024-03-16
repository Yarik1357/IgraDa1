import sqlite3

conn = sqlite3.connect("students.db")

cursor = conn.cursor()

# cursor.execute(""" DROP TABLE students""")
cursor.execute("""CREATE TABLE IF NOT EXISTS students (
               student_name TEXT,
               class TEXT,
               avr_score INT,
               parents_name TEXT
)""")

# cursor.execute("""INSERT INTO students VALUES (
#                'Панасюк Євгенія',
#                '7А',
#                10,
#                'Панасюк Катеріна'
# )""")

# cursor.execute("""INSERT INTO students VALUES (
#                'Аркадій Паравозік',
#                '9А',
#                8,
#                'Дімон Паравозік'
# )""")

# cursor.execute("""INSERT INTO students VALUES (
#                'Нікіта Гітлеренко',
#                '6А',
#                5,
#                'Анна Гітлеренко'
# )""")

# cursor.execute("""INSERT INTO students VALUES (
#                'Иосив Стас',
#                '10А',
#                8,
#                'Иосив Александер'
# )""")



cursor.execute("""SELECT * FROM students """)
stud =(cursor.fetchall())
for s in stud:
    print(s)

conn.commit()