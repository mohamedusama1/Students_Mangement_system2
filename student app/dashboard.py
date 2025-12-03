from customtkinter import *
from tkinter import *
from PIL import Image
from time import strftime
import sqlite3
from tkinter import messagebox

import statisticspage
import adminpage
import studentspage
import teacherspage


class DashboardClass():
    def __init__(self, root):
        self.root = root
        self.root.geometry('1200x690+100+5')
        self.root.title('Dashboard Page')
        self.root.config(bg='white')
        self.root.resizable(False, False)

        def date():
            date_1 = strftime('%I:%M:%S %p \t %A \t %b/%d/%Y')
            date_lbl.config(text=date_1)
            date_lbl.after(1000, date)

        # ============================== head frame ==========================
        up_frame = CTkFrame(root, width=1199, height=70, bg_color='#F6F5F5', fg_color='#F6F5F5', border_color='#DA7297',
                            border_width=2)
        up_frame.place(x=1, y=1)

        text_lbl = Label(up_frame, text='Modern School', font=('corier', 18, 'bold'), bg='#F6F5F5', fg='#DA7297')
        text_lbl.place(x=30, y=5, width=200, height=60)

        date_lbl = Label(up_frame, font=('corier', 18, 'bold'), bg='#F6F5F5', fg='#DA7297')
        date_lbl.place(x=590, y=5, width=570, height=60)
        date()

        # ============================= up frame ==========================
        frame = CTkFrame(root, width=1197, height=615, bg_color='white', fg_color='#F6F5F5', border_color='#DA7297',
                         border_width=2)
        frame.place(x=1, y=72)

        menu_frame = CTkFrame(frame, width=200, height=608, fg_color='#DA7297', bg_color='#F6F5F5',
                              border_color='#DA7297')
        menu_frame.place(x=3, y=3)

        def hide_line():
            home_line.config(bg='#DA7297')
            note_line.config(bg='#DA7297')
            ser_line.config(bg='#DA7297')
            state_line.config(bg='#DA7297')

        def delete_pages():
            for frame in page_frame.winfo_children():
                frame.destroy()

        def line(lb, page):
            hide_line()
            lb.config(bg='white')
            delete_pages()
            page()

        def open_statistics_page():
            # kept for compatibility but STATISTICS works as internal page (sta_page)
            win = Toplevel()
            statisticspage.StatisticsClass(win)
            root.withdraw()
            win.deiconify()

        # ============================= buttons ===========================
        home_img = CTkImage(Image.open('images/home_icon.png'), size=(38, 38))

        self.home_btn = CTkButton(menu_frame, text='HOME', width=100, height=40, fg_color='#DA7297', text_color='white',
                                  bg_color='#DA7297', font=('arial', 20, 'bold'), hover_color='#DA7297',
                                  border_color='#DA7297', image=home_img, border_width=2,
                                  border_spacing=16, corner_radius=0,
                                  command=lambda: line(lb=home_line, page=home_page))
        self.home_btn.place(x=0, y=100)

        home_line = Label(menu_frame, text='', bg='white')
        home_line.place(x=3, y=120, width=5, height=40)

        note_img = CTkImage(Image.open('images/note.png'), size=(42, 42))

        self.note_btn = CTkButton(menu_frame, text='NOTE', width=100, height=40, fg_color='#DA7297', text_color='white',
                                  bg_color='#DA7297', font=('arial', 20, 'bold'), hover_color='#DA7297',
                                  border_color='#DA7297',
                                  image=note_img, border_width=2, border_spacing=16,
                                  corner_radius=0,
                                  command=lambda: line(lb=note_line, page=note_page))
        self.note_btn.place(x=0, y=180)

        note_line = Label(menu_frame, text='', bg='#DA7297')
        note_line.place(x=3, y=200, width=5, height=40)

        ser_img = CTkImage(Image.open('images/services_icon.png'), size=(38, 38))

        self.ser_btn = CTkButton(menu_frame, text='SERVIES', width=100, height=40, fg_color='#DA7297',
                                 text_color='white', bg_color='#DA7297', font=('arial', 20, 'bold'),
                                 hover_color='#DA7297',
                                 border_color='#DA7297', image=ser_img, border_width=2,
                                 border_spacing=16, corner_radius=0,
                                 command=lambda: line(lb=ser_line, page=ser_page))
        self.ser_btn.place(x=5, y=250)

        ser_line = Label(menu_frame, text='', bg='#DA7297')
        ser_line.place(x=3, y=270, width=5, height=40)

        state_img = CTkImage(Image.open('images/ll.png'), size=(40, 40))

        self.state_btn = CTkButton(menu_frame, text='STATISTICS', width=100, height=40, fg_color='#DA7297',
                                   text_color='white', bg_color='#DA7297', font=('arial', 20, 'bold'),
                                   hover_color='#DA7297',
                                   border_color='#DA7297', image=state_img,
                                   border_width=2, border_spacing=16, corner_radius=0,
                                   command=lambda: line(lb=state_line, page=sta_page)
                                   )
        self.state_btn.place(x=5, y=320)

        state_line = Label(menu_frame, text='', bg='#DA7297')
        state_line.place(x=3, y=340, width=5, height=40)

        close_img = CTkImage(Image.open('images/close.png'), size=(28, 28))

        self.ser_btn = CTkButton(menu_frame, text='CLOSE', width=100, height=40, fg_color='#DA7297',
                                 text_color='white', bg_color='#DA7297', font=('arial', 20, 'bold'),
                                 hover_color='#DA7297',
                                 border_color='#DA7297', image=close_img, border_width=2, border_spacing=16,
                                 corner_radius=0)
        self.ser_btn.place(x=3, y=390)

        # ============================ page frame ==========================
        def home_page():
            home_frame = CTkFrame(page_frame, width=975, height=600, bg_color='#F6F5F5', fg_color='#F6F5F5')
            home_frame.place(x=1, y=1)

            stu_img = CTkImage(Image.open('images/stu.png'), size=(100, 100))

            student_btn = CTkButton(home_frame, text='Students', width=250,
                                    height=200, fg_color='#DA7297', text_color='white',
                                    bg_color='#F6F5F5', font=('arial', 30, 'bold'),
                                    border_color='#D8D2C2', image=stu_img, compound='top',
                                    border_spacing=20, hover_color='#DA7297',
                                    border_width=5, corner_radius=30, command=open_students_page)
            student_btn.place(x=50, y=100)

            te_img = CTkImage(Image.open('images/tech.png'), size=(100, 100))

            techers_btn = CTkButton(home_frame, text='Techers', width=250,
                                    height=200, fg_color='#DA7297', text_color='white',
                                    bg_color='#F6F5F5', font=('arial', 30, 'bold'),
                                    border_color='#D8D2C2', image=te_img, compound='top',
                                    border_spacing=20, hover_color='#DA7297',
                                    border_width=5, corner_radius=30,
                                    command=open_teachers_page)
            techers_btn.place(x=350, y=100)

            emp_img = CTkImage(Image.open('images/emp.png'), size=(100, 100))

            emp_btn = CTkButton(home_frame, text='Employee', width=250,
                                height=200, fg_color='#DA7297', text_color='white',
                                bg_color='#F6F5F5', font=('arial', 30, 'bold'),
                                border_color='#D8D2C2', image=emp_img, compound='top',
                                border_spacing=20, hover_color='#DA7297',
                                border_width=5, corner_radius=30)
            emp_btn.place(x=650, y=100)

            acc_img = CTkImage(Image.open('images/cou.png'), size=(100, 100))

            accounting_btn = CTkButton(home_frame, text='Accounting', width=250,
                                       height=200, fg_color='#DA7297', text_color='white',
                                       bg_color='#F6F5F5', font=('arial', 30, 'bold'),
                                       border_color='#D8D2C2', image=acc_img, compound='top',
                                       border_spacing=20, hover_color='#DA7297',
                                       border_width=5, corner_radius=30)
            accounting_btn.place(x=50, y=350)

            e_img = CTkImage(Image.open('images/exam.png'), size=(100, 100))

            exam_btn = CTkButton(home_frame, text='Exam', width=250,
                                 height=200, fg_color='#DA7297', text_color='white',
                                 bg_color='#F6F5F5', font=('arial', 30, 'bold'),
                                 border_color='#D8D2C2', image=e_img, compound='top',
                                 border_spacing=20, hover_color='#DA7297',
                                 border_width=5, corner_radius=30)
            exam_btn.place(x=350, y=350)

            a_img = CTkImage(Image.open('images/adminl.png'), size=(100, 100))

            admin_btn = CTkButton(home_frame, text='Admin', width=250,
                                  height=200, fg_color='#DA7297', text_color='white',
                                  bg_color='#F6F5F5', font=('arial', 30, 'bold'),
                                  border_color='#D8D2C2', image=a_img, compound='top',
                                  border_spacing=20, hover_color='#DA7297',
                                  border_width=5, corner_radius=30, command=open_admin_page)
            admin_btn.place(x=650, y=350)

        def note_page():
            note_frame = CTkFrame(page_frame, width=975, height=600, bg_color='#F6F5F5', fg_color='#F6F5F5')
            note_frame.place(x=1, y=1)
            lbl = Label(note_frame, text='note page')
            lbl.pack()

        def ser_page():
            ser_frame = CTkFrame(page_frame, width=975, height=600, bg_color='#F6F5F5', fg_color='#F6F5F5')
            ser_frame.place(x=1, y=1)
            lbl = Label(ser_frame, text='ser page')
            lbl.pack()

        def sta_page():
            sta_frame = CTkFrame(page_frame, width=975, height=600, bg_color='#F6F5F5', fg_color='#F6F5F5')
            sta_frame.place(x=1, y=1)

            # ---------- helper functions ----------
            def safe_count(conn, table_name):
                try:
                    cur = conn.cursor()
                    cur.execute(f"SELECT COUNT(*) FROM {table_name}")
                    r = cur.fetchone()
                    return r[0] if r else 0
                except Exception:
                    return 0

            def detect_table(conn, candidates):
                cur = conn.cursor()
                cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
                existing = [r[0].lower() for r in cur.fetchall()]
                for c in candidates:
                    if c and c.lower() in existing:
                        return c
                return None

            def update_count():
                try:
                    con = sqlite3.connect('school.db')
                    cur = con.cursor()

                    # Students
                    student_table = detect_table(con, ['first_student', 'firststudent', 'students'])
                    students = safe_count(con, student_table) if student_table else 0

                    # Teachers
                    teacher_table = detect_table(con, ['teachers', 'teacher'])
                    teachers = safe_count(con, teacher_table) if teacher_table else 0

                    # Employees (if you have an employees table)
                    employee_table = detect_table(con, ['employee', 'employees'])
                    employees = safe_count(con, employee_table) if employee_table else 0

                    # Admins
                    admin_table = detect_table(con, ['admin', 'admins'])
                    admins = safe_count(con, admin_table) if admin_table else 0

                    # Accounts
                    account_table = detect_table(con, ['account', 'accounts'])
                    accounts = safe_count(con, account_table) if account_table else 0

                    # Marks - map per request: islamic -> physics, arabic -> english
                    islamic_table = detect_table(con, ['islamic_marks', 'islamic', 'physics_marks'])
                    islamic_count = safe_count(con, islamic_table) if islamic_table else 0

                    arabic_table = detect_table(con, ['arabic_marks', 'arabic', 'english_marks'])
                    arabic_count = safe_count(con, arabic_table) if arabic_table else 0

                    con.close()

                    # Update UI
                    lbl_students.config(text=f"Total Students\n[ {students} ]")
                    lbl_islamic.config(text=f"Islamic Marks\n[ {islamic_count} ]")
                    lbl_arabic.config(text=f"Arabic Marks\n[ {arabic_count} ]")
                    lbl_teachers.config(text=f"Total Teachers\n[ {teachers} ]")
                    lbl_employees.config(text=f"Total Employees\n[ {employees} ]")
                    lbl_admins.config(text=f"Total Admins\n[ {admins} ]")
                    lbl_accounts.config(text=f"Total Accounts\n[ {accounts} ]")
                except Exception as ex:
                    messagebox.showerror("Error", f"Failed to load statistics:\n{str(ex)}")

            # ---------- UI: organized grid (3 columns x 3 rows) ----------
            card_width = 300
            card_height = 140
            gap_x = 25
            gap_y = 20
            start_x = 30
            start_y = 40

            # Row 1
            lbl_students = Label(sta_frame, text="Total Students\n[ 0 ]", bd=5, relief=RIDGE,
                                 bg='#DA7297', fg='white', font=('goudy old style', 20, 'bold'))
            lbl_students.place(x=start_x, y=start_y, width=card_width, height=card_height)

            lbl_islamic = Label(sta_frame, text="Islamic Marks\n[ 0 ]", bd=5, relief=RIDGE,
                                bg='#DA7297', fg='white', font=('goudy old style', 20, 'bold'))
            lbl_islamic.place(x=start_x + (card_width + gap_x), y=start_y, width=card_width, height=card_height)

            lbl_arabic = Label(sta_frame, text="Arabic Marks\n[ 0 ]", bd=5, relief=RIDGE,
                               bg='#DA7297', fg='white', font=('goudy old style', 20, 'bold'))
            lbl_arabic.place(x=start_x + 2 * (card_width + gap_x), y=start_y, width=card_width, height=card_height)

            # Row 2
            lbl_teachers = Label(sta_frame, text="Total Teachers\n[ 0 ]", bd=5, relief=RIDGE,
                                 bg='#DA7297', fg='white', font=('goudy old style', 20, 'bold'))
            lbl_teachers.place(x=start_x, y=start_y + card_height + gap_y, width=card_width, height=card_height)

            lbl_employees = Label(sta_frame, text="Total Employees\n[ 0 ]", bd=5, relief=RIDGE,
                                  bg='#DA7297', fg='white', font=('goudy old style', 20, 'bold'))
            lbl_employees.place(x=start_x + (card_width + gap_x), y=start_y + card_height + gap_y,
                                width=card_width, height=card_height)

            lbl_admins = Label(sta_frame, text="Total Admins\n[ 0 ]", bd=5, relief=RIDGE,
                               bg='#DA7297', fg='white', font=('goudy old style', 20, 'bold'))
            lbl_admins.place(x=start_x + 2 * (card_width + gap_x), y=start_y + card_height + gap_y,
                             width=card_width, height=card_height)

            # Row 3 (smaller cards for summary)
            small_h = 100
            lbl_accounts = Label(sta_frame, text="Total Accounts\n[ 0 ]", bd=5, relief=RIDGE,
                                 bg='#DA7297', fg='white', font=('goudy old style', 16, 'bold'))
            lbl_accounts.place(x=start_x, y=start_y + 2 * (card_height + gap_y), width=card_width, height=small_h)

            lbl_islamic_small = Label(sta_frame, text="Islamic Marks\n[ 0 ]", bd=5, relief=RIDGE,
                                      bg='#DA7297', fg='white', font=('goudy old style', 16, 'bold'))
            lbl_islamic_small.place(x=start_x + (card_width + gap_x), y=start_y + 2 * (card_height + gap_y),
                                    width=card_width, height=small_h)

            lbl_arabic_small = Label(sta_frame, text="Arabic Marks\n[ 0 ]", bd=5, relief=RIDGE,
                                     bg='#DA7297', fg='white', font=('goudy old style', 16, 'bold'))
            lbl_arabic_small.place(x=start_x + 2 * (card_width + gap_x), y=start_y + 2 * (card_height + gap_y),
                                   width=card_width, height=small_h)

            # ---------- Refresh button (centered under the grid) ----------
            refresh_btn = CTkButton(sta_frame, text="REFRESH", fg_color="#DA7297", width=160, height=42,
                                    text_color="white", font=("Arial", 14, "bold"), command=update_count)
            refresh_btn.place(x=(975 - 160) // 2, y=start_y + 2 * (card_height + gap_y) + small_h + 15)

            # initial load
            update_count()

        # =================== import pages =================
        def open_admin_page():
            win = Toplevel()
            adminpage.AdminClass(win)
            root.withdraw()
            win.deiconify()

        def open_students_page():
            win = Toplevel()
            studentspage.StudentsClass(win)
            root.withdraw()
            win.deiconify()

        def open_teachers_page():
            win = Toplevel()
            teacherspage.TeachersClass(win)
            root.withdraw()
            win.deiconify()

        page_frame = CTkFrame(frame, width=980, height=605, bg_color='#F6F5F5', fg_color='#F6F5F5')
        page_frame.place(x=210, y=5)
        home_page()


if __name__ == "__main__":
    root = Tk()
    DashboardClass(root)
    root.mainloop()
