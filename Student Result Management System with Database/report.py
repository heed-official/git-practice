from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk,messagebox
import sqlite3

class reportClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")#window_title
        self.root.geometry("1200x480+80+170")#window size
        self.root.config(bg="white")
        self.root.focus_force()

#=======Title==========================================================

        title=Label(
            self.root,
            text="View Student Results",#main header
            font=("goudy old style",20,"bold"),
            bg="orange",
            fg="#262626"
            )
        title.place(x=10,y=15,width=1170,height=50)       

#=======VARIABLES======================================================

        self.var_search=StringVar()
        self.var_id=""



#===================================================================================Search=========================================================

        lbl_search=Label(
            self.root,
            text="Search By Roll No.",
            font=("goud old style", 20, "bold"),
            bg="white"
            )
        lbl_search.place(x=260,y=100)

        txt_search=Entry(
            self.root,
            textvariable=self.var_search,
            font=("goud old style", 20),
            bg="lightyellow"
            )
        txt_search.place(x=520,y=100, width=150)

#====================================================================================BUTTONS============================================

#=======Search Button====================================================

        btn_search=Button(
            self.root,
            text='Search',
            font=("goudy old style",15,"bold"),
            bg="#03a9f4",
            fg="white",
            cursor="hand2",
            command=self.search
            )
        btn_search.place(x=680,y=100,width=100,height=35)

#=======Clear Button======================================================

        btn_clear=Button(
            self.root,
            text='Clear',
            font=("goudy old style",15,"bold"),
            bg="gray",
            fg="white",
            cursor="hand2",
            command=self.clear
            )
        btn_clear.place(x=800,y=100,width=100,height=35)

#=======Delete Button==========================================================

        btn_delete=Button(
            self.root,
            text='Delete',
            font=("goudy old style",15,"bold"),
            bg="red",
            fg="white",
            cursor="hand2",
            command=self.delete
            )
        btn_delete.place(x=500,y=350,width=150,height=35)


#=======LABEL==============================================================

#=======Roll===============================================================

        lbl_roll=Label(
            self.root,
            text="Roll No.",
            font=("goud old style", 15, "bold"),
            bg="white",
            bd=2,
            relief=GROOVE
            )
        lbl_roll.place(x=150,y=230, width=150, height=50)  

#=======Name================================================================

        lbl_name=Label(
            self.root,
            text="Name",
            font=("goud old style", 15, "bold"),
            bg="white",
            bd=2,
            relief=GROOVE
            )
        lbl_name.place(x=300,y=230, width=150, height=50)  

#=======Course===============================================================

        lbl_course=Label(
            self.root,
            text="Course",
            font=("goud old style", 15, "bold"),
            bg="white",
            bd=2,
            relief=GROOVE
            )
        lbl_course.place(x=450,y=230, width=150, height=50)

#=======Marks Obtained=======================================================

        lbl_marks=Label(
            self.root,
            text="Marks Obtained",
            font=("goud old style", 15, "bold"),
            bg="white",
            bd=2,
            relief=GROOVE
            )
        lbl_marks.place(x=600,y=230, width=150, height=50)

#=======Full Marks============================================================

        lbl_full=Label(
            self.root,
            text="Total Marks",
            font=("goud old style", 15, "bold"),
            bg="white",
            bd=2,
            relief=GROOVE
            )
        lbl_full.place(x=750,y=230, width=150, height=50)

#=======Percentage===========================================================

        lbl_per=Label(
            self.root,
            text="Percentage",
            font=("goud old style", 15, "bold"),
            bg="white",
            bd=2,
            relief=GROOVE
            )
        lbl_per.place(x=900,y=230, width=150, height=50)  

#=======Label the result=====================================================

#=======Roll=================================================================

        self.roll=Label(
            self.root,
            #text="Roll No.",
            font=("goud old style", 15, "bold"),
            bg="white",
            bd=2,
            relief=GROOVE
            )
        self.roll.place(x=150,y=280, width=150, height=50)  

#=======Name=================================================================

        self.name=Label(
            self.root,
            #text="Name",
            font=("goud old style", 15, "bold"),
            bg="white",
            bd=2,
            relief=GROOVE
            )
        self.name.place(x=300,y=280, width=150, height=50)  

#=======Course===============================================================

        self.course=Label(
            self.root,
            #text="Course",
            font=("goud old style", 15, "bold"),
            bg="white",
            bd=2,
            relief=GROOVE
            )
        self.course.place(x=450,y=280, width=150, height=50)
        
#=======Marks Obtained=======================================================

        self.marks=Label(
            self.root,
            #text="Marks Obtained",
            font=("goud old style", 15, "bold"),
            bg="white",
            bd=2,
            relief=GROOVE
            )
        self.marks.place(x=600,y=280, width=150, height=50)

#=======Full Marks============================================================

        self.full=Label(
            self.root,
            #text="Total Marks",
            font=("goud old style", 15, "bold"),
            bg="white",
            bd=2,
            relief=GROOVE
            )
        self.full.place(x=750,y=280, width=150, height=50)

#=======Percentage=============================================================

        self.per=Label(
            self.root,
            #text="Percentage",
            font=("goud old style", 15, "bold"),
            bg="white",
            bd=2,
            relief=GROOVE
            )
        self.per.place(x=900,y=280, width=150, height=50)  

#====================================================================================Search Data from database=====================

    def search(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_search.get()=="":
                messagebox.showerror("Error","Roll No. should be required",parent=self.root)
            else:
                cur.execute("select * from result where roll=?",(self.var_search.get(),))
                row=cur.fetchone()
                if row!=None:
                    self.var_id=row[0]
                    self.roll.config(text=row[1])
                    self.name.config(text=row[2])
                    self.course.config(text=row[3])
                    self.marks.config(text=row[4])
                    self.full.config(text=row[5])
                    self.per.config(text=row[6])
                else:
                    messagebox.showerror("Error","No record found",parent=self.root)
                              
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

#====================================================================================Clearing Data Inputs===============================

    def clear(self):
        self.var_id=""
        self.roll.config(text="")
        self.name.config(text="")
        self.course.config(text="")
        self.marks.config(text="")
        self.full.config(text="")
        self.per.config(text="")
        self.var_search.set("")

#===================================================================================Delete data from table==============================

    def delete(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_id=="":
                messagebox.showerror("Error","Search Student result first", parent=self.root)
            else:
                cur.execute("select * from result where rid=?",(self.var_id,))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Student Result",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?") 
                    if op==TRUE:
                        cur.execute("delete from result where rid=?",(self.var_id,))
                        con.commit()
                        messagebox.showinfo("Delete","Result Deleted Successfilly",parent=self.root)
                        self.clear   
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")   





if __name__=="__main__":
    root=Tk()
    obj=reportClass(root)
    root.mainloop()