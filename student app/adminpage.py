from customtkinter import *
from tkinter import *
from PIL import Image
from time import strftime
from tkinter import ttk, messagebox
import sqlite3

import dashboard

class AdminClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1200x690+100+5')
        self.root.title('Admin Page')
        self.root.config(bg='white')
        self.root.resizable(False,False)


        def date():
            date_1 = strftime('%I:%M:%S %p \t %A \t %b/%d/%Y')
            date_lbl.config(text=date_1)
            date_lbl.after(1000,date)
        #============================== head frame ==========================
        up_frame = CTkFrame(root,width=1199,height=70,bg_color='#F6F5F5',fg_color='#F6F5F5',border_color='#DA7297',border_width=2)
        up_frame.place(x=1,y=1)

        text_lbl = Label(up_frame, text='Admin Page',font=('corier',18,'bold'),bg='#F6F5F5',fg='#DA7297')
        text_lbl.place(x=150,y=5,width=200,height=60)

        date_lbl = Label(up_frame,font=('corier',18,'bold'),bg='#F6F5F5',fg='#DA7297')
        date_lbl.place(x=590,y=5,width=570,height=60)
        date()

        #=================== back button ================
        def back():
            win = Toplevel()
            dashboard.DashboardClass(win)
            root.withdraw()
            win.deiconify()

        back_btn = CTkButton(up_frame,text='←', width=100,height=68,
                             fg_color='#DA7297',text_color='white',bg_color='#F6F5F5',
                             font=('arial',30,'bold'),hover_color='#DA7297',border_color='#DA7297',
                             corner_radius=0,command=back)
        back_btn.place(x=2,y=2)

        #============================= up frame ==========================
        head_frame = CTkFrame(root,width=1197,height=615,bg_color='white',fg_color='#F6F5F5',border_color='#DA7297',border_width=2)
        head_frame.place(x=1,y=72)

        text_lbl = Label(head_frame, text='WELCOME ADMIN \n PAGE',font=('corier',25,'bold'),bg='#F6F5F5',fg='#DA7297')
        text_lbl.place(x=20,y=50,width=300,height=100)

        #================== logo image =================
        logo_img = CTkImage(Image.open('images/admin.png'),size=(250,250))
        img_lbl = CTkLabel(head_frame, text='',image=logo_img, fg_color='#F6F5F5')
        img_lbl.place(x=350,y=20)
        #==================
        id = StringVar()
        name = StringVar()
        username = StringVar()
        password = StringVar()
        #======================= labels + entrys ============================
        lbl_id = CTkLabel(head_frame,text='Id',width=200,height=25, text_color='gray',
                          font=('arial',14,'bold'),fg_color='#F6F5F5',bg_color='#F6F5F5')
        lbl_id.place(x=80,y=300)

        en_id = CTkEntry(head_frame,textvariable=id,justify='center',width=50,height=35,font=('arial',14,'bold'),
                         border_color='gray',border_width=1,bg_color='#F6F5F5',fg_color='#F6F5F5')
        en_id.place(x=200,y=300)

        lbl_name = CTkLabel(head_frame,text='New Account Name',width=200,height=25, text_color='gray',
                          font=('arial',14,'bold'),fg_color='#F6F5F5',bg_color='#F6F5F5')
        lbl_name.place(x=20,y=340)

        en_name = CTkEntry(head_frame,textvariable=name,justify='center',width=230,height=35,font=('arial',14,'bold'),
                         border_color='gray',border_width=1,bg_color='#F6F5F5',fg_color='#F6F5F5')
        en_name.place(x=20,y=370)

        lbl_username = CTkLabel(head_frame,text='New Account userame',width=200,height=25, text_color='gray',
                          font=('arial',14,'bold'),fg_color='#F6F5F5',bg_color='#F6F5F5')
        lbl_username.place(x=20,y=410)

        en_username = CTkEntry(head_frame,textvariable=username,justify='center',width=230,height=35,font=('arial',14,'bold'),
                         border_color='gray',border_width=1,bg_color='#F6F5F5',fg_color='#F6F5F5')
        en_username.place(x=20,y=440)

        lbl_pass = CTkLabel(head_frame,text='New Account Password',width=200,height=25, text_color='gray',
                          font=('arial',14,'bold'),fg_color='#F6F5F5',bg_color='#F6F5F5')
        lbl_pass.place(x=20,y=480)

        en_pass = CTkEntry(head_frame,textvariable=password,justify='center',width=230,height=35,font=('arial',14,'bold'),
                         border_color='gray',border_width=1,bg_color='#F6F5F5',fg_color='#F6F5F5')
        en_pass.place(x=20,y=510)
        #====================== buttons ====================
        def clear():
            id.set("")
            name.set("")
            username.set("")
            password.set("")
        
        def delete():
            con = sqlite3.connect('school.db')
            cur = con.cursor()
            op = messagebox.askyesno("confirm","do you really want to delete")

            if op:
                cur.execute("DELETE FROM Account WHERE ID=?", (id.get(),))
                con.commit()
                rec_id()
                messagebox.showinfo("delete","delete successfully")
                show()
                clear()
            else:
                messagebox.showerror("cancel","delete cancel")
            con.close()      

        clear_brn = CTkButton(head_frame,text='clear',width=100,height=40,
                              fg_color='#DA7297',text_color='white',bg_color='white',
                              font=('arial',16,'bold'),hover_color='#DA7297',
                              border_color='#DA7297',corner_radius=5,command=clear)
        clear_brn.place(x=20,y=560)

        delete_brn = CTkButton(head_frame,text='delete',width=100,height=40,
                              fg_color='#DA7297',text_color='white',bg_color='white',
                              font=('arial',16,'bold'),hover_color='#DA7297',
                              border_color='#DA7297',corner_radius=5,command=delete)
        delete_brn.place(x=150,y=560)
        #======================= new account treeview =======================
        def rec_id():
            con = sqlite3.connect('school.db')
            cur = con.cursor()
            cur.execute("""
            WITH RECURSIVE cte AS (
                        SELECT ROW_NUMBER() OVER (ORDER BY ID) AS new_id, ID
                        FROM Account)
            UPDATE Account
                        SET ID = (SELECT new_id FROM cte WHERE cte.ID =Account.ID)            
                """)
            
        def show():
            con = sqlite3.connect('school.db')
            cur = con.cursor()
            try:
                cur.execute("select * from Account")
                rows = cur.fetchall()
                new_account_tree.delete(*new_account_tree.get_children())
                global count
                count = 0
                for row in rows:
                    #new_account_tree.insert('',END,values=row)
                    if count % 2 == 0:
                        new_account_tree.insert(parent='', index='end', iid=count, text='', values=(row[0],row[1],row[2],row[3]),tags=('evenrow'))
                    else:
                        new_account_tree.insert(parent='', index='end', iid=count, text='', values=(row[0],row[1],row[2],row[3]),tags=('oddrow'))
                    
                    count += 1
            except Exception as ex:
                messagebox.showerror('error',f"errot {str(ex)}")

        def get_data(ev):
            n = new_account_tree.focus()
            f = (new_account_tree.item(n))
            row = f['values']

            id.set(row[0])
            name.set(row[1])
            username.set(row[2])
            password.set(row[3])

            var_id_admin.set(row[0])
            var_name_admin.set(row[1])
            var_username_admin.set(row[2])
            var_password_admin.set(row[3])
        

        
        new_account_tree_f = Frame(head_frame,bg='gray')
        new_account_tree_f.place(x=280,y=330,width=420,height=250)

        new_account_style = ttk.Style()
        new_account_style.theme_use('clam')

        new_account_style.configure('Treeview',bg='#D3D3D3',font=('arial',12),fg='black',
                                    rowheight=30,fieldbackground='white')
        new_account_style.configure('Treeview.Heading',background='#DA7297',foreground='white',
                                    font=('arial',12,'bold'),height=100)
        
        scroll_new_account_tree = Scrollbar(new_account_tree_f)
        scroll_new_account_tree.pack(side=RIGHT, fill=Y)

        new_account_tree = ttk.Treeview(new_account_tree_f,yscrollcommand=scroll_new_account_tree.set)
        new_account_tree.place(x=0,y=0,width=403,height=250)

        scroll_new_account_tree.config(command=new_account_tree.yview)

        new_account_tree['columns'] = ("ID", "name", "username", "password")

        new_account_tree.column('#0',width=0, stretch=NO)
        new_account_tree.column('ID', anchor=W, width=40)
        new_account_tree.column('name', anchor=W, width=50)
        new_account_tree.column('username', anchor=W, width=100)
        new_account_tree.column('password', anchor=W, width=100)

        new_account_tree.heading('#0', text='', anchor=W)
        new_account_tree.heading('ID', text='ID', anchor='center')
        new_account_tree.heading('name', text='NAME', anchor='center')
        new_account_tree.heading('username', text='USERNAME', anchor='center')
        new_account_tree.heading('password', text='Password', anchor='center')
        new_account_tree.bind("<ButtonRelease-1>",get_data)
        show()

        new_account_tree.tag_configure('oddrow', background='lightgray')
        new_account_tree.tag_configure('evenrow', background='#F6F5F5')
        
        #============================== admin ============================
        def rec_id_admin():
            con = sqlite3.connect('school.db')
            cur = con.cursor()
            cur.execute("""
            WITH RECURSIVE cte AS (
                        SELECT ROW_NUMBER() OVER (ORDER BY admin_ID) AS new_id, admin_ID
                        FROM Admin)
            UPDATE Admin
                        SET admin_ID = (SELECT new_id FROM cte WHERE cte.admin_ID =Admin.admin_ID)            
                """)
            
        def add():
            con = sqlite3.connect('school.db')
            cur = con.cursor()
            if (var_name_admin.get()=="" or var_username_admin.get()=="" or var_password_admin.get()==""):
                messagebox.showerror("error","please enter all data")
            else:
                cur.execute("INSERT INTO Admin(admin_name,admin_username,admin_password) values(?,?,?)",(
                    var_name_admin.get(),
                    var_username_admin.get(),
                    var_password_admin.get(),
                ))  
                messagebox.showinfo("success","add successfully") 
            con.commit()  
            con.close() 
            rec_id_admin() 
            show_admin()
            clear_admin()

        def show_admin():
            con = sqlite3.connect('school.db')
            cur = con.cursor()
            try:
                cur.execute("select * from Admin")
                rows = cur.fetchall()
                admin_tree.delete(*admin_tree.get_children())
                global count
                count = 0
                for row in rows:
                    #new_account_tree.insert('',END,values=row)
                    if count % 2 == 0:
                        admin_tree.insert(parent='', index='end', iid=count, text='', values=(row[0],row[1],row[2],row[3]),tags=('evenrow'))
                    else:
                        admin_tree.insert(parent='', index='end', iid=count, text='', values=(row[0],row[1],row[2],row[3]),tags=('oddrow'))
                    
                    count += 1
            except Exception as ex:
                messagebox.showerror('error',f"errot {str(ex)}")

        def clear_admin():
            var_id_admin.set("")
            var_name_admin.set("")
            var_username_admin.set("")
            var_password_admin.set("")

        def get_admin_data(ev):
            n = admin_tree.focus() 
            f = (admin_tree.item(n)) 
            row = f['values']  

            var_id_admin.set(row[0])
            var_name_admin.set(row[1])
            var_username_admin.set(row[2])
            var_password_admin.set(row[3])

        def update_admin():
            con = sqlite3.connect('school.db')
            cur = con.cursor()   
            cur.execute("UPDATE Admin set admin_name=?, admin_username=?, admin_password=? where admin_ID=?",(
                var_name_admin.get(),
                var_username_admin.get(),
                var_password_admin.get(),
                var_id_admin.get(),
            )) 
            con.commit()
            con.close()
            rec_id_admin()
            messagebox.showinfo("success","update successfully")
            show_admin()
            clear_admin()

        def delete_admin():
            con = sqlite3.connect('school.db')
            cur= con.cursor()
            op = messagebox.askyesno("confirm","do you really want to delete") 
            if op:
                cur.execute("DELETE FROM Admin WHERE admin_ID=?",(var_id_admin.get(),))
                con.commit()
                rec_id_admin()
                messagebox.showinfo("success","delete successfully")
                show_admin() 
                clear_admin()
                
            else:
                messagebox.showinfo("cancle","delete cancel")
            con.close() 

        def upgrade_to_admin():
            con =sqlite3.connect('school.db')
            cur = con.cursor()

            if id.get() =="":
                messagebox.showerror("error","please select a new account to upgrade")
                return
            cur.execute("SELECT * FROM Account WHERE ID=?",(id.get(),)) 
            data = cur.fetchone()    

            if data:
                cur.execute("INSERT INTO Admin(admin_name,admin_username,admin_password) VALUES (?,?,?)",(
                    data[1],
                    data[2],
                    data[3]

                ))
                cur.execute("DELETE FROM Account WHERE ID=?",(id.get(),))
                con.commit()
                rec_id()
                messagebox.showinfo("success","upgrade successfully") 
                show()
                clear()   
            else:
                messagebox.showerror("error","no new account")
            con.close()
            rec_id_admin()
            show_admin()
            clear_admin()        
        #=======================
        var_id_admin = StringVar()
        var_name_admin = StringVar()
        var_username_admin = StringVar()
        var_password_admin = StringVar()
        
        #======================= labels + entrys ============================
        lbl_admin_id = CTkLabel(head_frame,text='Id',width=200,height=25, text_color='gray',
                          font=('arial',14,'bold'),fg_color='#F6F5F5',bg_color='#F6F5F5')
        lbl_admin_id.place(x=790,y=50)

        en_admin_id = CTkEntry(head_frame,textvariable=var_id_admin,justify='center',width=50,height=35,font=('arial',14,'bold'),
                         border_color='gray',border_width=1,bg_color='#F6F5F5',fg_color='#F6F5F5')
        en_admin_id.place(x=910,y=50)

        lbl_admin_name = CTkLabel(head_frame,text='Admin Name',width=200,height=25, text_color='gray',
                          font=('arial',14,'bold'),fg_color='#F6F5F5',bg_color='#F6F5F5')
        lbl_admin_name.place(x=750,y=90)

        en_admin_name = CTkEntry(head_frame,textvariable=var_name_admin,justify='center',width=230,height=35,font=('arial',14,'bold'),
                         border_color='gray',border_width=1,bg_color='#F6F5F5',fg_color='#F6F5F5')
        en_admin_name.place(x=730,y=120)

        lbl_admin_username = CTkLabel(head_frame,text='Admin userame',width=200,height=25, text_color='gray',
                          font=('arial',14,'bold'),fg_color='#F6F5F5',bg_color='#F6F5F5')
        lbl_admin_username.place(x=750,y=170)

        en_admin_username = CTkEntry(head_frame,textvariable=var_username_admin,justify='center',width=230,height=35,font=('arial',14,'bold'),
                         border_color='gray',border_width=1,bg_color='#F6F5F5',fg_color='#F6F5F5')
        en_admin_username.place(x=730,y=200)

        lbl_admin_pass = CTkLabel(head_frame,text='Admin Password',width=200,height=25, text_color='gray',
                          font=('arial',14,'bold'),fg_color='#F6F5F5',bg_color='#F6F5F5')
        lbl_admin_pass.place(x=750,y=240)

        en_admin_pass = CTkEntry(head_frame,textvariable=var_password_admin,justify='center',width=230,height=35,font=('arial',14,'bold'),
                         border_color='gray',border_width=1,bg_color='#F6F5F5',fg_color='#F6F5F5')
        en_admin_pass.place(x=730,y=270)
        #====================== buttons =====================
        add_brn = CTkButton(head_frame,text='Add',width=100,height=40,
                              fg_color='#DA7297',text_color='white',bg_color='white',
                              font=('arial',16,'bold'),hover_color='#DA7297',
                              border_color='#DA7297',corner_radius=5,command=add)
        add_brn.place(x=1020,y=50)
        
        clear_brn = CTkButton(head_frame,text='Clear',width=100,height=40,
                              fg_color='#DA7297',text_color='white',bg_color='white',
                              font=('arial',16,'bold'),hover_color='#DA7297',
                              border_color='#DA7297',corner_radius=5,command=clear_admin)
        clear_brn.place(x=1020,y=100)
        
        update_brn = CTkButton(head_frame,text='Update',width=100,height=40,
                              fg_color='#DA7297',text_color='white',bg_color='white',
                              font=('arial',16,'bold'),hover_color='#DA7297',
                              border_color='#DA7297',corner_radius=5,command=update_admin)
        update_brn.place(x=1020,y=150)

        delete_brn = CTkButton(head_frame,text='Delete',width=100,height=40,
                              fg_color='#DA7297',text_color='white',bg_color='white',
                              font=('arial',16,'bold'),hover_color='#DA7297',
                              border_color='#DA7297',corner_radius=5,command=delete_admin)
        delete_brn.place(x=1020,y=200)

        upgrade_brn = CTkButton(head_frame,text='Upgrade to admin',width=100,height=40,
                              fg_color='#DA7297',text_color='white',bg_color='white',
                              font=('arial',16,'bold'),hover_color='#DA7297',
                              border_color='#DA7297',corner_radius=5,command=upgrade_to_admin)
        upgrade_brn.place(x=1000,y=250)

        #================================= admin treeview =============================
        admin_tree_f = Frame(head_frame,bg='gray')
        admin_tree_f.place(x=730,y=330,width=420,height=250)

        admin_style = ttk.Style()
        admin_style.theme_use('clam')

        admin_style.configure('Treeview',bg='#D3D3D3',font=('arial',12),fg='black',
                                    rowheight=30,fieldbackground='white')
        admin_style.configure('Treeview.Heading',background='#DA7297',foreground='white',
                                    font=('arial',12,'bold'),height=100)
        
        scroll_admin_tree = Scrollbar(admin_tree_f)
        scroll_admin_tree.pack(side=RIGHT, fill=Y)

        admin_tree = ttk.Treeview(admin_tree_f,yscrollcommand=scroll_admin_tree.set)
        admin_tree.place(x=0,y=0,width=403,height=250)

        scroll_admin_tree.config(command=admin_tree.yview)

        admin_tree['columns'] = ("admin_ID", "admin_name", "admin_username", "admin_password")

        admin_tree.column('#0',width=0, stretch=NO)
        admin_tree.column('admin_ID', anchor=W, width=40)
        admin_tree.column('admin_name', anchor=W, width=100)
        admin_tree.column('admin_username', anchor=W, width=70)
        admin_tree.column('admin_password', anchor=W, width=70)

        admin_tree.heading('#0', text='', anchor=W)
        admin_tree.heading('admin_ID', text='ID', anchor='center')
        admin_tree.heading('admin_name', text='admin NAME', anchor='center')
        admin_tree.heading('admin_username', text='USERNAME', anchor='center')
        admin_tree.heading('admin_password', text='Password', anchor='center')
        admin_tree.bind("<ButtonRelease-1>",get_admin_data)
        show_admin()
        

        admin_tree.tag_configure('oddrow', background='lightgray')
        admin_tree.tag_configure('evenrow', background='#F6F5F5')
        
        
        
        
        




if __name__=="__main__":
    root = Tk()
    AdminClass(root)
    root.mainloop()