from customtkinter import *
from tkinter import *
from PIL import Image
from tkinter import messagebox
import sqlite3

import dashboard

class LoginClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1100x600+100+50')
        self.root.title('Login Page')
        self.root.config(bg='#F6F5F5')
        self.root.resizable(False,False)

        def open_dashboard():
            window = Toplevel()
            dashboard.DashboardClass(window)
            root.withdraw()
            window.deiconify()


        def login():
            con = sqlite3.connect('school.db')
            cur = con.cursor()
            find_user = 'SELECT * FROM Admin WHERE admin_username=? and admin_password=?'
            cur.execute(find_user, [(var_username.get()), (var_password.get())])
            result = cur.fetchall()

            if result:
                messagebox.showinfo("Success","login successfully,\n\nCLICK 'ok' to continue")
                open_dashboard()
            else:
                messagebox.showerror("error","you can't login beacuse you are not admin,\nenter admin account to login")    
        


        #======================= switch frame =====================
        login_frame = CTkFrame(root,width=1080,height=550,fg_color='#F6F5F5',bg_color='#F6F5F5')
        sign_up_frame = CTkFrame(root,width=1080,height=550,fg_color='#F6F5F5',bg_color='#F6F5F5')

        for frame in (login_frame,sign_up_frame):
            frame.place(x=10,y=20)

        def show_frame(frame):
            frame.tkraise()

        show_frame(login_frame)  

        #======================= logo image =================
        img = CTkImage(Image.open('images/login.png'), size=(490,400))
        img_lbl = CTkLabel(login_frame,text='',image=img,fg_color='#F6F5F5')
        img_lbl.place(x=10, y=70)
        #============================
        var_username = StringVar()
        var_password = StringVar()

        #======================= frame=======================
        frame = CTkFrame(login_frame,width=520,height=500,fg_color='#F6F5F5',bg_color='#F6F5F5',border_width=2,corner_radius=30,border_color='#DA7297')
        frame.place(x=520,y=20)

        up_text_lbl = CTkLabel(frame, text='Login Page',corner_radius=10,fg_color='#DA7297',width=200,height=30,text_color='white',font=('arial',20,'bold'))
        up_text_lbl.place(x=160,y=50)

        lbl = CTkLabel(frame,text='Login To Continue',width=200,height=25,text_color='#DA7297',font=('arial',18,'bold'))
        lbl.place(x=30,y=110)

        labl = CTkLabel(frame,text='Not A Member?',width=150,height=25,text_color='#DA7297',font=('arial',14,'bold'))
        labl.place(x=30,y=150)

        #=============================== labels + entrys ==================================
        lbl_user = CTkLabel(frame, text='Enter Your Username.',width=200,height=25,text_color='gray',font=('arial',14))
        lbl_user.place(x=25, y=200)

        user_en = CTkEntry(frame,textvariable=var_username,width=350,height=35,font=('corier',14),border_width=1,border_color='#DA7297',justify='center')
        user_en.place(x=50,y=230)

        lbl_password= CTkLabel(frame, text='Enter Your Password.',width=200,height=25,text_color='gray',font=('arial',14))
        lbl_password.place(x=25, y=280)

        password_en = CTkEntry(frame,textvariable=var_password,width=350,height=35,font=('corier',14),border_width=1,border_color='#DA7297',justify='center')
        password_en.place(x=50,y=310)

        #================================== buttons =======================
        forgot_pass_btn = CTkButton(frame,text='Forgot Password',width=150,height=20,fg_color='transparent',
                                    text_color='#DA7297',font=('arial',16,'bold'),bg_color='transparent',hover_color='#F6F5F5',command=lambda: forgot_password())
        forgot_pass_btn.place(x=150,y=360)

        sign_up_btn = CTkButton(frame,text='Sign Up Page',width=100,height=20,fg_color='transparent',
                                    text_color='gray',font=('arial',14,'bold'),bg_color='transparent',hover_color='#F6F5F5',command=lambda: show_frame(sign_up_frame))
        sign_up_btn.place(x=160,y=150)

        login_btn = CTkButton(frame,text='Login',width=150,height=20,border_spacing=20,
                              fg_color='#DA7297',text_color='white',bg_color='#F6F5F5',
                              font=('arial',16,'bold'),border_color='#DA7297',hover_color='#DA7297',
                              border_width=2,corner_radius=20,command=login)
        login_btn.place(x=155,y=400)

        #================================ forgot password page ======================
        def forgot_password():
            win = Toplevel()
            win.geometry('400x400+680+150')
            win.title('Forgot Password')
            win.config(bg='#F6F5F5')
            win.resizable(False,False)

            #========================== labels + entrys ========================
            lbl_up = CTkLabel(win,text='Update Your Password', width=200,height=25,text_color='#DA7297',font=('arial',16,'bold'))
            lbl_up.place(x=50,y=70)

            lbl_username = CTkLabel(win,text='Enter the username', height=25,text_color='gray',font=('arial',14))
            lbl_username.place(x=55,y=110)

            username_en = CTkEntry(win,width=300,height=35,font=('arial',14),border_width=1,border_color='#DA7297')
            username_en.place(x=50,y=140)

            lbl_pass = CTkLabel(win,text='Enter the New Password', height=25,text_color='gray',font=('arial',14))
            lbl_pass.place(x=55,y=180)

            pass_en = CTkEntry(win,width=300,height=35,font=('arial',14),border_width=1,border_color='#DA7297')
            pass_en.place(x=50,y=210)

            update_pass_btn = CTkButton(win,text='Update Password',width=180,height=10,border_spacing=15,
                              fg_color='#DA7297',text_color='white',bg_color='#F6F5F5',font=('arial',14,'bold'),border_color='#DA7297',hover_color='#DA7297',border_width=2,corner_radius=20)
            update_pass_btn.place(x=110,y=270)

        #=============================== sign up page ==================================
        #============ variables ===========
        name = StringVar()
        username = StringVar()
        password = StringVar()
        confirm_password = StringVar()

        
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
            
        def clear():
            name.set("")
            username.set("")
            password.set("")
            confirm_password.set("")
        #=========================
        def sign_up():
            if name.get()=="" or username.get()=="" or password.get()=="" or confirm_password.get()=="":
                messagebox.showerror('error','please enter all the data')
            elif password.get() != confirm_password.get():
                messagebox.showerror('error','password and confirm password not match')
            else:
                try:
                    con = sqlite3.connect('school.db')
                    cur = con.cursor()
                    cur.execute("INSERT INTO Account(name,username,password) VALUES(?,?,?)",
                                (name.get(),username.get(),password.get())) 
                    con.commit()  
                    con.close()  
                    rec_id()
                    messagebox.showinfo('success','new account create successfully')
                    clear()
                except Exception as es:
                    messagebox.showerror('error','something went wrong try agin')    

        #======================= logo image =================
        img = CTkImage(Image.open('images/login.png'), size=(490,400))
        img_lbl = CTkLabel(sign_up_frame,text='',image=img,fg_color='#F6F5F5')
        img_lbl.place(x=10, y=70)
        #========================== frame ===================
        signup_frame = CTkFrame(sign_up_frame,width=520,height=500,fg_color='#F6F5F5',bg_color='#F6F5F5',border_width=2,corner_radius=30,border_color='#DA7297')
        signup_frame.place(x=520,y=20)

        up_text_lbl = CTkLabel(signup_frame, text='Sign Up Page',corner_radius=10,fg_color='#DA7297',width=200,height=25,text_color='white',font=('arial',20,'bold'))
        up_text_lbl.place(x=150,y=20)

        lbl = CTkLabel(signup_frame,text='Create Account',width=200,height=25,text_color='#DA7297',font=('arial',16,'bold'))
        lbl.place(x=20,y=65)

        labl = CTkLabel(signup_frame,text='Already a Member?',width=150,height=25,text_color='#DA7297',font=('arial',14,'bold'))
        labl.place(x=70,y=90)

        #============================= labels + entrys =======================
        lbl_name = CTkLabel(signup_frame, text='Enter Your Name.',height=25,text_color='gray',font=('arial',14))
        lbl_name.place(x=75, y=120)

        name_en = CTkEntry(signup_frame,textvariable=name,width=350,height=35,font=('corier',14),border_width=1,border_color='#DA7297',justify='center')
        name_en.place(x=75,y=150)

        lbl_user = CTkLabel(signup_frame, text='Enter Your Username.',width=200,height=25,text_color='gray',font=('arial',14))
        lbl_user.place(x=50, y=190)

        user_en = CTkEntry(signup_frame,textvariable=username,width=350,height=35,font=('corier',14),border_width=1,border_color='#DA7297',justify='center')
        user_en.place(x=75,y=220)

        lbl_pass = CTkLabel(signup_frame, text='Enter Your Password.',width=200,height=25,text_color='gray',font=('arial',14))
        lbl_pass.place(x=50, y=260)

        pass_en = CTkEntry(signup_frame,textvariable=password,width=350,height=35,font=('corier',14),border_width=1,border_color='#DA7297',justify='center')
        pass_en.place(x=75,y=290)

        
        lbl_confirm_pass = CTkLabel(signup_frame, text='Enter the Confirm Password.',width=200,height=25,text_color='gray',font=('arial',14))
        lbl_confirm_pass.place(x=65, y=330)

        pass_en = CTkEntry(signup_frame,textvariable=confirm_password,width=350,height=35,font=('corier',14),border_width=1,border_color='#DA7297',justify='center')
        pass_en.place(x=75,y=360)

        #=========================== buttons =========================
        login_btn = CTkButton(signup_frame,text='Login Page',width=100,height=20,fg_color='transparent',
                                    text_color='gray',font=('arial',14,'bold'),bg_color='transparent',hover_color='#F6F5F5',command=lambda: show_frame(login_frame))
        login_btn.place(x=210,y=90)

        signup_btn = CTkButton(signup_frame,text='Sign Up',width=150,height=20,border_spacing=20,
                              fg_color='#DA7297',text_color='white',bg_color='#F6F5F5',font=('arial',16,'bold'),border_color='#DA7297',hover_color='#DA7297',border_width=2,corner_radius=20,
                              command=sign_up)
        signup_btn.place(x=155,y=410)








   


if __name__=="__main__":
    root = Tk()
    LoginClass(root)
    root.mainloop()        