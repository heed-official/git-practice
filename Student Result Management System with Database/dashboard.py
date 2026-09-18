from tkinter import*
from PIL import Image,ImageTk,ImageDraw #pip install pillow
from course import CourseClass
from student import studentClass
from result import resultClass
from report import reportClass
from tkinter import messagebox,ttk
import os
from datetime import*
from math import*
import time
import sqlite3

class RMS:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1360x700+0+0")
        self.root.config(bg="white")

#=========icons===========================================

        logo_image=Image.open("images/apple.png")
        logo_image=logo_image.resize((50,50))
        self.logo_dash=ImageTk.PhotoImage(logo_image)
        
#=========title===========================================

        title=Label(
            self.root,
            text="Student Result Management System",
            padx=10,
            compound=LEFT,
            image=self.logo_dash,
            font=("goudy old style",20,"bold"),
            bg="#033054",
            fg="white"
            )
        title.place(x=0,y=0,relwidth=1,height=50)

#=======Menu Frame==========================================

        M_Frame=LabelFrame(
            self.root,
            text="Menus",
            font=("times new roman", 15),
            bg="white"
            )
        M_Frame.place(x=10,y=70,width=1340,height=80)

#==================================================================================Buttons in Menu==============================

#=======Course Button======================================

        btn_course=Button(
            M_Frame,
            text="Course",
            font=("goudy old style",15,"bold"),
            bg="#0b5377",
            fg="white",
            cursor="hand2",
            command=self.add_course
            )
        btn_course.place(x=20,y=5,width=200,height=40)

#=======Student Button=======================================

        btn_student=Button(
            M_Frame,
            text="Students",
            font=("goudy old style",15,"bold"),
            bg="#0b5377",
            fg="white",
            cursor="hand2",
            command=self.add_student
            )
        btn_student.place(x=240,y=5,width=200,height=40)

#=======Result Button==========================================

        btn_result=Button(
            M_Frame,
            text="Result",
            font=("goudy old style",15,"bold"),
            bg="#0b5377",
            fg="white",
            cursor="hand2",
            command=self.add_result
            )
        btn_result.place(x=460,y=5,width=200,height=40)

#=======View Button==============================================

        btn_view=Button(
            M_Frame,
            text="View Student Result",
            font=("goudy old style",15,"bold"),
            bg="#0b5377",
            fg="white",
            cursor="hand2",
            command=self.add_report
            )
        btn_view.place(x=680,y=5,width=200,height=40)

#=======Logout Button=============================================

        btn_logout=Button(
            M_Frame,
            text="Logout",
            font=("goudy old style",15,"bold"),
            bg="#0b5377",
            fg="white",
            cursor="hand2",
            command=self.logout
            )
        btn_logout.place(x=900,y=5,width=200,height=40)

#=======Exit Button================================================

        btn_exit=Button(
            M_Frame,
            text="Exit",
            font=("goudy old style",15,"bold"),
            bg="#0b5377",
            fg="white",
            cursor="hand2",
            command=self.exit
            )
        btn_exit.place(x=1120,y=5,width=200,height=40)

#===================================================================================Content Window======================

        self.bg_img=Image.open("images/partial.png")
        self.bg_img=self.bg_img.resize((920,350),Image.Resampling.LANCZOS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg=Label(self.root,image=self.bg_img)
        self.lbl_bg.place(x=400,y=180,width=920,height=350)

#===================================================================================Update Details======================

#=======Course_Update============================================

        self.lbl_course=Label(
            self.root,
            text="Total Courses\n[ 0 ]",
            font=("goudy old style",20),
            bd=10,
            relief=RIDGE,
            bg="#e43b06",
            fg="white"
            )
        self.lbl_course.place(x=400,y=530,width=300,height=100)

#=======Students_Update===========================================

        self.lbl_student=Label(
            self.root,
            text="Total Students\n[ 0 ]",
            font=("goudy old style",20),
            bd=10,
            relief=RIDGE,
            bg="#e43b06",
            fg="white"
            )
        self.lbl_student.place(x=710,y=530,width=300,height=100)

#=======Results_Update=============================================

        self.lbl_result=Label(
            self.root,
            text="Total Results\n[ 0 ]",
            font=("goudy old style",20),
            bd=10,
            relief=RIDGE,
            bg="#e43b06",
            fg="white"
            )
        self.lbl_result.place(x=1020,y=530,width=300,height=100)

#===================================================================================CLOCK====================================

        self.lbl=Label(self.root,
            text="\nLocal\nTime",
            font=("Book Antiqua",25,"bold"),
            fg="black",
            compound=BOTTOM,
            bg="white",bd=0)
        self.lbl.place(x=40,y=180,height=450,width=350)

        self.working()                                                              #clock arrow rotation hours/minutes/seconds

#=======footer====================================================

        footer=Label(
            self.root,
            text="SRMS - Student Result Management System\nContact Us for any Technical Issue: 9052312394",
            font=("goudy old style",12),
            bg="#262626",
            fg="white"
            )
        footer.pack(side=BOTTOM,fill=X)

        self.update_details()                                                       #calling the update_details to work the updates

#===================================================================================Updating Number of Course, Students, and Result=====================

    def update_details(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select * from course")
            cr=cur.fetchall()
            self.lbl_course.config(text=f"Total Courses\n[{str(len(cr))}]")

            cur.execute("select * from student")
            cr=cur.fetchall()
            self.lbl_student.config(text=f"Total Students\n[{str(len(cr))}]")

            cur.execute("select * from result")
            cr=cur.fetchall()
            self.lbl_result.config(text=f"Total Result\n[{str(len(cr))}]")

            self.lbl_course.after(200,self.update_details)
            self.lbl_student.after(200,self.update_details)
            self.lbl_result.after(200,self.update_details)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

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

#===================================================================================#putting image in the window without arrow================

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

#=======Hour Line Image=========================================================================

        draw.line((origin,200+60*sin(radians(hr)),200-60*cos(radians(hr))),fill="black",width=3)

#=======Minute Line Image=======================================================================

        draw.line((origin,200+80*sin(radians(min)),200-80*cos(radians(min))),fill="red",width=3)

#=======Second Line Image=======================================================================

        draw.line((origin,200+100*sin(radians(sec)),200-100*cos(radians(sec))),fill="blue",width=3)

        draw.ellipse((195,195,210,210),fill="black")                                #drawing black circle/ellipse

        clock.save("images/clock_new.png")                                          #when done drawing then it will save as Clock_new.png

#===================================================================================Adding Course=====================================

    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CourseClass(self.new_win)
    
#===================================================================================Adding Students====================================

    def add_student(self):
            self.new_win=Toplevel(self.root)
            self.new_obj=studentClass(self.new_win)

#===================================================================================Adding Result======================================

    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=resultClass(self.new_win)

#===================================================================================Adding Report=======================================

    def add_report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=reportClass(self.new_win)    

#===================================================================================Logout Condition====================================

    def logout(self):
            op=messagebox.askyesno("Confirm","Do you really want to logout?")
            if op==True:
                self.root.destroy()                                                 #destroy's dashboard window
                os.system("python login.py")                                        #redirect to login window

#===================================================================================Exit Condition======================================

    def exit(self):
            op=messagebox.askyesno("Confirm","Do you really want to Exit?")
            if op==True:
                self.root.destroy()                                                 #destroy's dashboard to completely exit

                 
    


if __name__=="__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()