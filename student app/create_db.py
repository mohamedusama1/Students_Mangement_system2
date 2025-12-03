import sqlite3 

def create_db():
    con = sqlite3.connect('school.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Account(ID INTEGER PRIMARY KEY, name TEXT, username TEXT, password TEXT)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS Admin(admin_ID INTEGER PRIMARY KEY, admin_name TEXT, admin_username TEXT, admin_password TEXT)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS first_student(s_ID INTEGER PRIMARY KEY AUTOINCREMENT,student_name TEXT, student_gender TEXT, student_age TEXT,address TEXT, contact TEXT, date TEXT, last_school TEXT,years_felid TEXT, health_problem TEXT, final_result TEXT)")
    con.commit()

    #cur.execute("DROP TABLE islamic_marks")
    cur.execute("CREATE TABLE IF NOT EXISTS islamic_marks(i_ID INTEGER PRIMARY KEY AUTOINCREMENT,student_name TEXT,st_month TEXT , nd_month TEXT, chapter1 TEXT, half_year TEXT, st_month1 TEXT, nd_month2 TEXT, chapter2 TEXT, chapter3 TEXT, final_exam TEXT, final_result TEXT)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS arabic_marks(a_ID INTEGER PRIMARY KEY AUTOINCREMENT,student_name TEXT,st_month TEXT , nd_month TEXT, chapter1 TEXT, half_year TEXT, st_month1 TEXT, nd_month2 TEXT, chapter2 TEXT, chapter3 TEXT, final_exam TEXT, final_result TEXT)")
    con.commit()
    

create_db()