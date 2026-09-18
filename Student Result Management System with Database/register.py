from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk #pip install pillow
import sqlite3
import os

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0")
        #self.root.config(bg="white")

#=======BG Image=================================================

        self.bg=ImageTk.PhotoImage(file="images/bgr.jpg")
        bg=Label(self.root,image=self.bg)
        bg.place(x=250,y=0,relwidth=1,relheight=1)

#=======LEFT Image===============================================

        self.left=ImageTk.PhotoImage(file="images/bgr2.jpg")
        left=Label(self.root,image=self.left)
        left.place(x=30,y=100,width=650,height=490)

#====================================================================================Registration Frame==================================

        frame1=Frame(self.root,bg="white")
        frame1.place(x=680,y=100,width=635,height=490)

        title=Label(frame1,
                    text="REGISTER HERE",
                    font=("times new roman",20,"bold"),
                    bg="white",
                    fg="green")
        title.place(x=50,y=30)

#=======First Name===============================================

        f_name=Label(frame1,
                     text="First Name",
                     font=("times new roman",12,"bold"),
                     bg="white",
                     fg="black")
        f_name.place(x=50,y=100)

        self.txt_fname=Entry(frame1,
                             font=("times new roman",12),
                             bg="lightgray")
        self.txt_fname.place(x=50,y=130,width=250)

#=======Last Name================================================

        l_name=Label(frame1,
                     text="Last Name",
                     font=("times new roman",12,"bold"),
                     bg="white",
                     fg="black")
        l_name.place(x=340,y=100)

        self.txt_lname=Entry(frame1,
                             font=("times new roman",12),
                             bg="lightgray")
        self.txt_lname.place(x=340,y=130,width=250)

#=======Contact Number===========================================

        contact=Label(frame1,
                      text="Contact No.",
                      font=("times new roman",12,"bold"),
                      bg="white",
                      fg="black")
        contact.place(x=50,y=170)

        self.txt_contact=Entry(frame1,
                               font=("times new roman",12),
                               bg="lightgray")
        self.txt_contact.place(x=50,y=200,width=250)

#=======Email=====================================================

        email=Label(frame1,
                    text="Email",
                    font=("times new roman",12,"bold"),
                    bg="white",
                    fg="black")
        email.place(x=340,y=170)

        self.txt_email=Entry(frame1,
                             font=("times new roman",12),
                             bg="lightgray")
        self.txt_email.place(x=340,y=200,width=250)

#=======Question==================================================

        question=Label(frame1,
                       text="Security Question",
                       font=("times new roman",12,"bold"),
                       bg="white",
                       fg="black")
        question.place(x=50,y=240)

                                                                                    #drop down choices

        self.cmb_quest=ttk.Combobox(frame1,
                                    font=("times new roman",12),
                                    state='readonly',
                                    justify=CENTER)
        self.cmb_quest.place(x=50,y=270,width=250)

        self.cmb_quest['values']=("Select",
                                  "Your First Pet Name?",
                                  "Your Birth Place?",
                                  "Your Best Friend Name?")
        self.cmb_quest.current(0)                                                   #Standand display

#=======Answer=====================================================

        answer=Label(frame1,
                     text="Answer",
                     font=("times new roman",12,"bold"),
                     bg="white",
                     fg="black")
        answer.place(x=340,y=240)

        self.txt_answer=Entry(frame1,
                              font=("times new roman",12),
                              bg="lightgray")
        self.txt_answer.place(x=340,y=270,width=250)

#=======Password===================================================

        password=Label(frame1,
                       text="Password",
                       font=("times new roman",12,"bold"),
                       bg="white",
                       fg="black")
        password.place(x=50,y=310)

        self.txt_password=Entry(frame1,
                                font=("times new roman",12),
                                bg="lightgray")
        self.txt_password.place(x=50,y=340,width=250)

#=======Confirmation Password=======================================

        cpassword=Label(frame1,
                        text="Confirm Password",
                        font=("times new roman",12,"bold"),
                        bg="white",
                        fg="black")
        cpassword.place(x=340,y=310)

        self.txt_cpassword=Entry(frame1,
                                 font=("times new roman",12),
                                 bg="lightgray")
        self.txt_cpassword.place(x=340,y=340,width=250)

#===================================================================================TERMS========================================================

        self.var_chk=IntVar()
        chk=Checkbutton(frame1,
                        text="I Agree The Terms & Conditions",
                        variable=self.var_chk,
                        onvalue=1,
                        offvalue=0,
                        bg="white",
                        font=("times new roman",12,"bold"))
        chk.place(x=50,y=380)

#===================================================================================BUTTONS===============================================

#=======REGISTER NOW BUTTON=============================================

        btn_register=Button(frame1,
                            text="REGISTER NOW...",
                            bg="green",
                            fg="white",
                            font=("times new roman",17,"bold"),
                            bd=5,
                            relief=RAISED,
                            cursor="hand2",
                            command=self.register_data)
        btn_register.place(x=50,y=420,width=250)

#=======LOGIN============================================================

        btn_login=Button(self.root,
                         text="SIGN IN",
                         bg="white",
                         fg="green",
                         font=("times new roman",17,"bold"),
                         bd=5,
                         relief=RAISED,
                         cursor="hand2",
                         command=self.login_window)
        btn_login.place(x=310,y=480)

#====================================================================================lOGIN WINDOW CONDITIONS=================================

    def login_window(self):
        self.root.destroy()
        #import login
        os.system("python login.py")

#====================================================================================Clearing everything when done register==============

    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.cmb_quest.set("Select")
        self.txt_answer.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_cpassword.delete(0,END)
        self.txt_fname.delete(0,END)
        self.var_chk.set(0)

#===================================================================================Condition to Register=================================

    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_lname.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.cmb_quest.get()=="Select" or self.txt_answer.get()=="":
            messagebox.showerror("Error","All Fields Are Required!",parent=self.root)
        elif self.txt_password.get()!=self.txt_cpassword.get():
            messagebox.showerror("Error","Password & Confirm Password should be the same!",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please Agree our terms & condition.",parent=self.root)
        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=?",(self.txt_email.get(),))
                row=cur.fetchone()
                #print(row)
                if row!=None:
                    messagebox.showerror("Error","User already Exist, Please try with another email",parent=self.root)
                else:    
                    cur.execute("insert into employee (f_name,l_name,contact,email,question,answer,password) values(?,?,?,?,?,?,?)",
                                    (self.txt_fname.get(),
                                    self.txt_lname.get(),
                                    self.txt_contact.get(),
                                    self.txt_email.get(),
                                    self.cmb_quest.get(),
                                    self.txt_answer.get(),
                                    self.txt_password.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Register Successfully",parent=self.root)
                    self.clear()
                    self.login_window()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)





root=Tk()
obj=Register(root)
root.mainloop()