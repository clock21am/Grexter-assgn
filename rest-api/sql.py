import sqlite3

with sqlite3.connect('students.db') as connection:
    c = connection.cursor()
    c.execute("""create table students ( NAME TEXT, AGE INTEGER,MAJOR TEXT, SPORT TEXT,RANK INTEGER)""")
    c.execute('INSERT INTO students VALUES("TOM",24,"MATHS","Cricket",3)')
    c.execute('INSERT INTO students VALUES("JERRY",26,"SCIENCE","Football",1)')
    c.execute('INSERT INTO students VALUES("Cacy",28,"ARTS","Baseball",2)')