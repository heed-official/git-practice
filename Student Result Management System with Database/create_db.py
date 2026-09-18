import sqlite3
import os

def create_db():

    con=sqlite3.connect(database="rms.db")
    cur=con.cursor()

#===============Course Table DB==========================================================

    cur.execute("CREATE TABLE IF NOT EXISTS course (cid INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT, duration TEXT, charges TEXT, description TEXT)")
    con.commit()

#===============Student Table DB=========================================================

    cur.execute("CREATE TABLE IF NOT EXISTS student (roll INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,email TEXT,gender TEXT,dob TEXT,contact TEXT,admission TEXT,course TEXT,state TEXT,city TEXT,pin TEXT,address TEXT)")
    con.commit()

#===============Result Table DB==========================================================

    cur.execute("CREATE TABLE IF NOT EXISTS result (rid INTEGER PRIMARY KEY AUTOINCREMENT,roll TEXT,name TEXT,course TEXT,marks_ob TEXT,full_marks TEXT, per TEXT)")
    con.commit()
#===============Account Login DB=========================================================

    cur.execute("CREATE TABLE IF NOT EXISTS employee (eid INTEGER PRIMARY KEY AUTOINCREMENT,f_name TEXT,l_name TEXT,contact TEXT,email TEXT,question TEXT,answer TEXT,password TEXT)")
    
    con.close()

create_db()