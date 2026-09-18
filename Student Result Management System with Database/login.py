from tkinter import*
from PIL import Image,ImageTk,ImageDraw #pip install Pillow
from datetime import*
import time
from math import*
import sqlite3
from tkinter import messagebox
import os

class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("GUI Analog Clock")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")

#=======Background Colors====================================

        left_lbl=Label(self.root,
                       bg="#08A3D2",
                       bd=0)
        left_lbl.place(x=0,y=0,relheight=1,width=600)

        right_lbl=Label(self.root,
                        bg="#031F3C",
                        bd=0)
        right_lbl.place(x=600,y=0,relheight=1,relwidth=1)

#====================================================================================Login Frames================================================

        login_frame=Frame(self.root,
                          bg="#002B32",
                          bd=5,
                          relief=RAISED)
        login_frame.place(x=250,y=100,width=800,height=500)

#=======Login Label=======================================

        title=Label(login_frame,
                    text="LOGIN HERE",
                    font=("times new roman",30,"bold"),
                    bg="#002B32",
                    fg="#08A3D2")
        title.place(x=250,y=50)

#=======Email Label=======================================

        email=Label(login_frame,
                    text="EMAIL ADDRESS",
                    font=("times new roman",18,"bold"),
                    bg="#002B32",
                    fg="white")
        email.place(x=250,y=150)

                                                                                    #Email/Username Input
        self.txt_email=Entry(login_frame,
                             font=("times new roman",15,"bold"),
                             bg="white",
                             fg="black")
        self.txt_email.place(x=250,y=180,width=350,height=35)

#=======Password Label=====================================

        pass_=Label(login_frame,
                    text="PASSWORD",
                    font=("times new roman",18,"bold"),
                    bg="#002B32",
                    fg="white")
        pass_.place(x=250,y=250)

                                                                                    #Password Input
        self.txt_pass=Entry(login_frame,
                            font=("times new roman",15,"bold"),
                            bg="white",
                            fg="black")
        self.txt_pass.place(x=250,y=280,width=350,height=35)

#===================================================================================Buttons================================================

#=======Registration Button==============================================

        btn_reg=Button(login_frame,
                       text="Register new Account?",
                       font=("times new roman",14),
                       bg="#002B32",
                       bd=0,
                       fg="#B00857",
                       cursor="hand2",
                       command=self.register_window)
        btn_reg.place(x=250,y=320)

#=======Login Button=====================================================

        btn_login=Button(login_frame,
                         text="Login",
                         font=("times new roman",14,"bold"),
                         fg="white",
                         bg="#B00857",
                         cursor="hand2",
                         command=self.login)
        btn_login.place(x=250,y=360,width=180,height=40)

#===================================================================================CLOCK==================================================

        self.lbl=Label(self.root,
                       text="\nWebCode Clock",
                       font=("Book Antiqua",25,"bold"),
                       fg="black",
                       compound=BOTTOM,
                       bg="white",bd=0)
        self.lbl.place(x=90,y=120,height=450,width=350)

        self.working()                                                              #clock arrow rotation hours/minutes/seconds

#======================================================================Registration Condition when done clicking the registration here...============

    def register_window(self):
        self.root.destroy()
        import register

#===================================================================================Login Condition==================================================

    def login(self):
        if self.txt_email.get()=="" or self.txt_pass.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=? and password=?",(self.txt_email.get(),self.txt_pass.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid USERNAME & PASSWORD",parent=self.root)
                else:
                    messagebox.showinfo("Success",f"Welcome: {self.txt_email.get()}",parent=self.root)
                    self.root.destroy()
                    os.system("python dashboard.py")
                con.close()
            except Exception as es:
                messagebox.showerror("Error",f"Error Due to: {str(es)}",parent=self.root)

#====================================================================================#putting image in the window without arrow================

    def clock_image(self,hr,min,sec):
        clock=Image.new("RGB",(400,400),(255,255,255))
        draw=ImageDraw.Draw(clock)

        bg=Image.open("images/cn.jpg")
        bg=bg.resize((300,300),Image.Resampling.LANCZOS)
        clock.paste(bg,(50,50))
                                                                                    #Formula To Rotate the AntiClock
                                                                                    #angle_in_radioans = angle_in_degrees * math.pi / 180
                                                                                    #line_length = 250
                                                                                    #center_x = 250
                                                                                    #center_y = 250
                                                                                    #end_x = center_x + line_length * math.cos(angle_in_radious)
                                                                                    #end_y = center_y + line_length * math.cos(angle_in_radious)

#===================================================================================Clock arrow rotation formula==================================

        origin=200,200

#=======Hour Line Image=========================================

        draw.line((origin,200+60*sin(radians(hr)),200-60*cos(radians(hr))),fill="black",width=3)

#=======Minute Line Image=======================================

        draw.line((origin,200+80*sin(radians(min)),200-80*cos(radians(min))),fill="red",width=3)

#=======Second Line Image=======================================

        draw.line((origin,200+100*sin(radians(sec)),200-100*cos(radians(sec))),fill="blue",width=3)

        draw.ellipse((195,195,210,210),fill="black")                                #drawing black circle/ellipse

        clock.save("images/clock_new.png")                                          #when done drawing then it will save as Clock_new.png

#====================================================================================Clock arrow radious formula===============================

    def working(self):
        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second
        
        hr=(h/12)*360                                                               #Hour rotation radious
        min=(m/60)*360                                                              #Minutes rotation radious
        sec=(s/60)*360                                                              #Seconds rotation radious
        
        self.clock_image(hr,min,sec)
        self.img=ImageTk.PhotoImage(file="images/clock_new.png")                    #saving the clock with arrow every 0.2 seconds
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.working)                                            #command for saving every 0.2 seconds





root=Tk()
obj=Login(root)
root.mainloop()