from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk,messagebox
import sqlite3

class CourseClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")                         #window_title
        self.root.geometry("1200x480+80+170")                                       #window size
        self.root.config(bg="white")
        self.root.focus_force()

#==========================================================Title===============================================

        title=Label(
            self.root,
            text="Manage Course Details",                                           #main header
            font=("goudy old style",20,"bold"),
            bg="#033054",
            fg="white"
            )
        title.place(x=10,y=15,width=1170,height=35)       

#===================================================================================Variables==============================

        self.var_course=StringVar()
        self.var_duration=StringVar()
        self.var_charges=StringVar()
        self.var_search=StringVar()                                                 #search variable inputs

#===================================================================================Widgets========================================

#=======Course============================================

        lbl_courseName=Label(
            self.root,
            text="Course Name",
            font=("goudy old style",15,"bold"),
            bg="white"
            )
        lbl_courseName.place(x=10,y=60)

#=======Duration==========================================

        lbl_duration=Label(
            self.root,
            text="Duration",
            font=("goudy old style",15,"bold"),
            bg="white"
            )
        lbl_duration.place(x=10,y=100)

#=======Charges============================================

        lbl_charges=Label(
            self.root,
            text="Charges",
            font=("goudy old style",15,"bold"),
            bg="white"
            )
        lbl_charges.place(x=10,y=140)

#=======Description=========================================

        lbl_description=Label(
            self.root,
            text="Description",
            font=("goudy old style",15,"bold"),
            bg="white"
            )
        lbl_description.place(x=10,y=180)

#==================================================================================Widgets_Inputs============================

#=======Course===============================================

        self.txt_courseName=Entry(
            self.root,
            textvariable=self.var_course,
            font=("goudy old style",15,"bold"),
            bg="lightyellow"
            )
        self.txt_courseName.place(x=150,y=60,width=200)

#=======Duration=============================================

        txt_duration=Entry(
            self.root,
            textvariable=self.var_duration,
            font=("goudy old style",15,"bold"),
            bg="lightyellow"
            )
        txt_duration.place(x=150,y=100,width=200)

#=======Charges===============================================

        txt_charges=Entry(
            self.root,
            textvariable=self.var_charges,
            font=("goudy old style",15,"bold"),
            bg="lightyellow"
            )
        txt_charges.place(x=150,y=140,width=200)

#=======Description===========================================

        self.txt_description=Text(
            self.root,
            font=("goudy old style",15,"bold"),
            bg="lightyellow"
            )
        self.txt_description.place(x=150,y=180,width=500,height=130)

#===================================================================================Buttons========================================

#=======Save Button============================================

        self.btn_add=Button(
            self.root,
            text='Save',
            font=("goudy old style",15,"bold"),
            bg="#2196f3",
            fg="white",
            cursor="hand2",
            command=self.add
            )
        self.btn_add.place(x=150,y=400,width=110,height=40)

#=======Update Button=============================================

        self.btn_update=Button(
            self.root,
            text='Update',
            font=("goudy old style",15,"bold"),
            bg="#4caf50",
            fg="white",
            cursor="hand2",
            command=self.update
            )
        self.btn_update.place(x=270,y=400,width=110,height=40)

#=======Delete Button=============================================

        self.btn_delete=Button(
            self.root,
            text='Delete',
            font=("goudy old style",15,"bold"),
            bg="#f44336",
            fg="white",
            cursor="hand2",
            command=self.delete
            )
        self.btn_delete.place(x=390,y=400,width=110,height=40)

#=======Clear Button===============================================

        self.btn_clear=Button(
            self.root,
            text='Clear',
            font=("goudy old style",15,"bold"),
            bg="#607d8b",
            fg="white",
            cursor="hand2",
            command=self.clear
            )
        self.btn_clear.place(x=510,y=400,width=110,height=40)

#===================================================================================Search Panel========================================

#=======Course Name Search=========================================

        lbl_search_courseName=Label(                                                #search label 
            self.root,
            text="Course Name",
            font=("goudy old style",15,"bold"),
            bg="white"
            )
        lbl_search_courseName.place(x=720,y=60)

        txt_search_courseName=Entry(                                                 #search input data variable
            self.root,
            textvariable=self.var_search,
            font=("goudy old style",15,"bold"),
            bg="lightyellow"
            )
        txt_search_courseName.place(x=870,y=60,width=180)

        btn_search=Button(                                                           #seach button preference
            self.root,
            text='Search',
            font=("goudy old style",15,"bold"),
            bg="#03a9f4",
            fg="white",
            cursor="hand2",
            command=self.search
            )
        btn_search.place(x=1060,y=60,width=120,height=28)

#====================================================================================Content Frame====================================

        self.C_Frame=Frame(
            self.root,
            bd=2,
            relief=RIDGE
            )
        self.C_Frame.place(x=720,y=100,width=470,height=340)
        
        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)                             #putting scroll in the Content Frame for search result
        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)

        self.CourseTable=ttk.Treeview(                                              #used to display data in rows and columns, similar to a table in Excel or a database result.
            self.C_Frame,                                                           #setting variables and scrollbar inside course table
            columns=("cid","name","duration","charges","description"),
            xscrollcommand=scrollx.set,yscrollcommand=scrolly.set
            )
        
        scrollx.pack(side=BOTTOM,fill=X)                                            #placement of scroll
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)
        
        self.CourseTable.heading("cid",text="Course ID")                            #header of the tables
        self.CourseTable.heading("name",text="Name")
        self.CourseTable.heading("duration",text="Duration")
        self.CourseTable.heading("charges",text="Charges")
        self.CourseTable.heading("description",text="Description")
        self.CourseTable["show"]='headings'                                         #diclaration of 'show'ing the 'headings'

        self.CourseTable.column("cid",width=100)                                    #placement of header
        self.CourseTable.column("name",width=100)
        self.CourseTable.column("duration",width=100)
        self.CourseTable.column("charges",width=100)
        self.CourseTable.column("description",width=170)

        self.CourseTable.pack(fill=BOTH,expand=1)                                   #fill in information if searched
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        
        self.show()                                                                 #when button is release it will appear at editing part of the system if you want to update it

#=============================================================================================================

#===================================================================================Clear Data from table====================================

    def clear(self):
        self.show()
        self.var_course.set("")
        self.var_duration.set("")
        self.var_charges.set("")
        self.var_search.set("")
        self.txt_description.delete('1.0',END)
        self.txt_courseName.config(state=NORMAL)

#===================================================================================Delete data from table=====================================

    def delete(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Choose course name to delete!", parent=self.root)
            else:
                cur.execute("select * from course where name=?",(self.var_course.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please select course from the list first",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?") 
                    if op==TRUE:
                        cur.execute("delete from course where name=?",(self.var_course.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Course Deleted Successfilly",parent=self.root)
                        self.clear   
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")   

#===================================================================================Getting data from table===============================

    def get_data(self,ev):
        #for updating the course details, you cant change the course title
        self.txt_courseName.config(state='readonly')
        self.txt_courseName
        r=self.CourseTable.focus()
        content=self.CourseTable.item(r)
        row=content["values"]
        self.var_course.set(row[1])
        self.var_duration.set(row[2])
        self.var_charges.set(row[3])
        self.txt_description.delete('1.0',END)
        self.txt_description.insert(END,row[4])

#===================================================================================Adding data to the table================================

    def add(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Course Name should be required!", parent=self.root)
            else:
                cur.execute("select * from course where name=?",(self.var_course.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Course Name Already present",parent=self.root)
                else:
                    cur.execute("insert into course (name,duration,charges,description) values(?,?,?,?)",(
                        self.var_course.get(),
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_description.get("1.0",END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Course Added Successfully",parent=self.root)
                    self.show()#when successfully saved it will show automatically in table

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

#===================================================================================Showing data in the table=============================

    def show(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select * from course")
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:#loop for never ending input of data
                self.CourseTable.insert('',END,values=row)
                          
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

#===================================================================================Search data in the table================================

    def search(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute(f"select * from course where name LIKE '%{self.var_search.get()}%'")
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:#loop for never ending input of data
                self.CourseTable.insert('',END,values=row)
                              
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

#====================================================================================Updating data the has been listed============================

    def update(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Course Name should be required!", parent=self.root)
            else:
                cur.execute("select * from course where name=?",(self.var_course.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select Course from list",parent=self.root)
                else:
                    cur.execute("update course set duration=?, charges=?, description=? where name=?",(

                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_description.get("1.0",END),
                        self.var_course.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Course Updated Successfully",parent=self.root)
                    self.show()                                                     #when successfully saved it will show automatically in table

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")





if __name__=="__main__":
    root=Tk()
    obj=CourseClass(root)
    root.mainloop()