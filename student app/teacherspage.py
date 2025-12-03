# teacherspage.py
from customtkinter import *
from tkinter import *
from PIL import Image
from time import strftime
from tkinter import ttk, messagebox
import sqlite3

import dashboard

class TeachersClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1200x690+100+5')
        self.root.title('Teachers Page')
        self.root.config(bg='white')
        self.root.resizable(False,False)

        def date():
            date_1 = strftime('%I:%M:%S %p \t %A \t %b/%d/%Y')
            date_lbl.config(text=date_1)
            date_lbl.after(1000,date)

        # ============================== head frame ==========================
        up_frame = CTkFrame(root, width=1199, height=70, bg_color='#F6F5F5', fg_color='#F6F5F5',
                            border_color='#DA7297', border_width=2)
        up_frame.place(x=1, y=1)

        text_lbl = Label(up_frame, text='Teachers Page', font=('corier',18,'bold'), bg='#F6F5F5', fg='#DA7297')
        text_lbl.place(x=150, y=5, width=200, height=60)

        date_lbl = Label(up_frame, font=('corier',18,'bold'), bg='#F6F5F5', fg='#DA7297')
        date_lbl.place(x=590, y=5, width=570, height=60)
        date()

        # =================== back button ================================
        def back():
            win = Toplevel()
            dashboard.DashboardClass(win)
            root.withdraw()
            win.deiconify()

        back_btn = CTkButton(up_frame, text='←', width=100, height=68,
                             fg_color='#DA7297', text_color='white', bg_color='#F6F5F5',
                             font=('arial',30,'bold'), hover_color='#DA7297', border_color='#DA7297',
                             corner_radius=0, command=back)
        back_btn.place(x=2, y=2)

        # ============================= main frame ========================
        head_frame = CTkFrame(root, width=1197, height=615, bg_color='white', fg_color='#F6F5F5',
                              border_color='#DA7297', border_width=2)
        head_frame.place(x=1, y=72)

        # -------- variables
        var_id = StringVar()
        var_name = StringVar()
        var_subject = StringVar()
        var_phone = StringVar()
        var_search = StringVar()

        # --------- functions: DB ops
        def rec_id():
            con = sqlite3.connect('school.db')
            cur = con.cursor()
            cur.execute("""
                WITH RECURSIVE cte AS (
                    SELECT ROW_NUMBER() OVER (ORDER BY t_id) AS new_id, t_id FROM teachers
                )
                UPDATE teachers SET t_id = (SELECT new_id FROM cte WHERE cte.t_id = teachers.t_id)
            """)
            con.commit()
            con.close()

        def add_teacher():
            if var_name.get()=="" or var_subject.get()=="" or var_phone.get()=="":
                messagebox.showerror("Error", "Enter all teacher data")
                return
            con = sqlite3.connect('school.db')
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS teachers(t_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, subject TEXT, phone TEXT)")
            cur.execute("INSERT INTO teachers(name, subject, phone) VALUES(?,?,?)",
                        (var_name.get(), var_subject.get(), var_phone.get()))
            con.commit()
            con.close()
            rec_id()
            show()
            clear()
            messagebox.showinfo("Success", "Teacher added successfully")

        def show():
            con = sqlite3.connect('school.db')
            cur = con.cursor()
            try:
                cur.execute("SELECT * FROM teachers")
                rows = cur.fetchall()
                teacher_tree.delete(*teacher_tree.get_children())
                i = 0
                for row in rows:
                    tag = 'evenrow' if i % 2 == 0 else 'oddrow'
                    teacher_tree.insert('', END, values=row, tags=(tag,))
                    i += 1
            except Exception as ex:
                messagebox.showerror("Error", f"Error: {str(ex)}")
            finally:
                con.close()

        def get_data(ev):
            item = teacher_tree.focus()
            row = teacher_tree.item(item)['values']
            if row:
                var_id.set(row[0])
                var_name.set(row[1])
                var_subject.set(row[2])
                var_phone.set(row[3])

        def update():
            con = sqlite3.connect('school.db')
            cur = con.cursor()
            cur.execute("UPDATE teachers SET name=?, subject=?, phone=? WHERE t_id=?",
                        (var_name.get(), var_subject.get(), var_phone.get(), var_id.get()))
            con.commit()
            con.close()
            rec_id()
            show()
            clear()
            messagebox.showinfo("Success", "Teacher updated successfully")

        def delete():
            if var_id.get()=="":
                messagebox.showerror("Error", "Select a teacher to delete")
                return
            con = sqlite3.connect('school.db')
            cur = con.cursor()
            op = messagebox.askyesno("Confirm", "Do you want to delete?")
            if op:
                cur.execute("DELETE FROM teachers WHERE t_id=?", (var_id.get(),))
                con.commit()
                con.close()
                rec_id()
                show()
                clear()
                messagebox.showinfo("Success", "Deleted successfully")

        def clear():
            var_id.set("")
            var_name.set("")
            var_subject.set("")
            var_phone.set("")
            var_search.set("")
            cmb_search.set("Select")

        def search():
            if cmb_search.get()=="Select" or var_search.get()=="":
                messagebox.showerror("Error", "Select search field and enter query")
                return
            con = sqlite3.connect('school.db')
            cur = con.cursor()
            try:
                cur.execute("SELECT * FROM teachers WHERE " + cmb_search.get() + " LIKE ?", ('%'+var_search.get()+'%',))
                rows = cur.fetchall()
                teacher_tree.delete(*teacher_tree.get_children())
                for row in rows:
                    teacher_tree.insert('', END, values=row)
            except Exception as ex:
                messagebox.showerror("Error", f"Error: {str(ex)}")
            finally:
                con.close()

        # ----------------- UI components -----------------
        lbl_name = CTkLabel(head_frame, text='Name', width=100, height=25, text_color='gray', font=('arial',14,'bold'))
        lbl_name.place(x=30, y=30)
        en_name = CTkEntry(head_frame, textvariable=var_name, width=220, height=35, justify=CENTER)
        en_name.place(x=120, y=30)

        lbl_subject = CTkLabel(head_frame, text='Subject', width=100, height=25, text_color='gray', font=('arial',14,'bold'))
        lbl_subject.place(x=30, y=80)
        en_subject = CTkEntry(head_frame, textvariable=var_subject, width=220, height=35, justify=CENTER)
        en_subject.place(x=120, y=80)

        lbl_phone = CTkLabel(head_frame, text='Phone', width=100, height=25, text_color='gray', font=('arial',14,'bold'))
        lbl_phone.place(x=30, y=130)
        en_phone = CTkEntry(head_frame, textvariable=var_phone, width=220, height=35, justify=CENTER)
        en_phone.place(x=120, y=130)

        add_btn = CTkButton(head_frame, text='ADD', width=120, height=35, fg_color='#DA7297', command=add_teacher)
        add_btn.place(x=30, y=180)

        update_btn = CTkButton(head_frame, text='UPDATE', width=120, height=35, fg_color='#DA7297', command=update)
        update_btn.place(x=160, y=180)

        delete_btn = CTkButton(head_frame, text='DELETE', width=120, height=35, fg_color='#DA7297', command=delete)
        delete_btn.place(x=290, y=180)

        clear_btn = CTkButton(head_frame, text='CLEAR', width=120, height=35, fg_color='#DA7297', command=clear)
        clear_btn.place(x=420, y=180)

        # search
        frame_search = CTkFrame(head_frame, width=600, height=60, fg_color='#F6F5F5', bg_color='white', border_color='#DA7297')
        frame_search.place(x=30, y=230)
        lbl_text = Label(frame_search, text='Search Teacher', font=('arial',14,'bold'), bg='white', fg='#DA7297')
        lbl_text.place(x=5, y=5, width=180, height=50)

        cmb_search = CTkComboBox(frame_search, values=("Select","name","subject","phone"),
                                 button_color='#DA7297', button_hover_color='#DA7297',
                                 justify=CENTER, font=('arial',12), width=180, height=35,
                                 fg_color='white', border_width=1, border_color='#DA7297',
                                 dropdown_fg_color='white', dropdown_text_color='#DA7297')
        cmb_search.place(x=180, y=12)

        search_en = CTkEntry(frame_search, textvariable=var_search, width=200, height=35, fg_color='white', justify='center', border_width=1, border_color='#DA7297')
        search_en.place(x=380, y=12)

        search_btn = CTkButton(frame_search, text='SEARCH', width=120, height=35, fg_color='#DA7297', command=search)
        search_btn.place(x=580, y=12)

        # Teacher treeview
        tree_f = Frame(head_frame, bg='gray')
        tree_f.place(x=30, y=310, width=1120, height=280)

        teacher_style = ttk.Style()
        teacher_style.theme_use('clam')
        teacher_style.configure('Treeview', bg='#D3D3D3', font=('arial',12), fg='black', rowheight=30, fieldbackground='white')
        teacher_style.configure('Treeview.Heading', background='#DA7297', foreground='white', font=('arial',12,'bold'))

        teacher_tree = ttk.Treeview(tree_f, columns=("t_id","name","subject","phone"), show='headings')
        teacher_tree.heading("t_id", text="ID")
        teacher_tree.heading("name", text="Name")
        teacher_tree.heading("subject", text="Subject")
        teacher_tree.heading("phone", text="Phone")

        teacher_tree.column("t_id", width=60)
        teacher_tree.column("name", width=300)
        teacher_tree.column("subject", width=200)
        teacher_tree.column("phone", width=200)

        vsb = Scrollbar(tree_f, orient=VERTICAL, command=teacher_tree.yview)
        vsb.pack(side=RIGHT, fill=Y)
        teacher_tree.configure(yscrollcommand=vsb.set)
        teacher_tree.place(x=0, y=0, width=1080, height=280)
        teacher_tree.bind("<ButtonRelease-1>", get_data)

        teacher_tree.tag_configure('oddrow', background='lightgray')
        teacher_tree.tag_configure('evenrow', background='#F6F5F5')

        show()
