import sqlite3
import csv


# database stored in the memory
conn = sqlite3.connect('school.db')
try:
    c = conn.cursor()
    c.execute("""
        CREATE TABLE students(
            SIS_ID integer,
            School_SIS_ID integer,
            First_Name message_text ,
            Last_Name message_text ,
            Username message_text,
            Password character,
            State_ID message_text,
            Secondary_Email null,
            Student_Number integer,
            Middle_Name message_text,
            Grade integer,
            Status message_text,
            Birthdate date,
            Graduation_Year date
            )""")

    c.execute("""CREATE TABLE teachers (
            SIS_ID	integer,
            School_SIS_ID	integer,
            First_Name	message_text,
            Last_Name	message_text,
            Username	message_text,
            Password	message_text,
            State_ID	integer,
            Teacher_Number	integer,
            Status	message_text,
            Middle_Name	message_text,
            Secondary_Email	null ,
            Title	null ,
            Qualification null 
            )""")

    c.execute("""CREATE TABLE schools (
            SIS_ID	integer,
            Name	message_text,
            School_Number	integer,
            School_NCES_ID	integer ,
            State_ID	message_text ,
            Grade_Low	integer ,
            Grade_High	integer ,
            Principal_SIS_ID	integer ,
            Principal_Name	message_text ,
            Principal_Secondary_Email null ,
            Address	message_text ,
            City	message_text ,
            State	message_text ,
            Country	message_text ,
            Zip	integer ,
            Phone message_text ,
            Zone null
                )""")

    conn.commit()
    with open('Student.csv', 'r') as student:
        no_students=0
        for row in student:
            c.execute("INSERT INTO students VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)", row.split(","))
            conn.commit()
            no_students +=1

    #c.execute("SELECT * FROM students")
    #print(c.fetchall())
    print("\n {} Records transferred".format(no_students))

    with open('Teacher.csv', 'r') as teacher:
        no_teacher=0
        for row in teacher:
            c.execute("INSERT INTO teachers VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", row.split(","))
            conn.commit()
            no_teacher +=1

    #c.execute("SELECT * FROM students")
    #print(c.fetchall())
    print("\n {} Records transferred".format(no_teacher))

    with open('School.csv', 'r') as school:
        no_school=0
        for row in school:
            c.execute("INSERT INTO schools VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", row.split(","))
            conn.commit()
            no_school +=1

    #c.execute("SELECT * FROM students")
    #print(c.fetchall())
    print("\n {} Records transferred".format(no_school))
except sqlite3.Error as e:
    print(e, "Sorry something went wrong")
finally:
    conn.close()










"""def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp.first, 'last': emp.last, 'pay': emp.pay})


def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
    return c.fetchall()


def update_pay(emp, pay):
    with conn:
        c.execute(""""UPDATE employees SET pay = :pay"""
"""""WHERE first = :first AND last = :last
                  {'first': emp.first, 'last': emp.last, 'pay': pay})


def remove_emp(emp):
    with conn:
        c.execute("DELETE from employees WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last})

emp_1 = Students('John', 'Doe', 80000)
emp_2 = Students('Jane', 'Doe', 90000)

insert_emp(emp_1)
insert_emp(emp_2)

emps = get_emps_by_name('Doe')
print(emps)

update_pay(emp_2, 95000)
remove_emp(emp_1)

emps = get_emps_by_name('Doe')
print(emps)
"""
#conn.close()