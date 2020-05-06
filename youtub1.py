from tkinter import *
from tkinter import ttk
import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    database = 'youtube',
    user='root',
    passwd = '1234'
)

cursor =  connection.cursor()



class Gui(Frame):
    def __init__(self, parent):
        self.parent = parent
        Frame.__init__(self, parent)

        self.titleFrame = Frame()
        self.titleFrame.pack(fill=X)

        self.label = Label(self.titleFrame,text ="Student Managent System", fg ="white",bg="red")
        self.label.pack(side=TOP, fill= X)

        self.labelFrame =Frame()
        self.labelFrame.pack(fill = X)

        self.studentid = Label(self.labelFrame, text="Student ID")
        self.studentid.pack(side=LEFT, padx= 50)

        self.studentname = Label(self.labelFrame, text="Student Name")
        self.studentname.pack(side=LEFT, padx=50)

        self.studentsurname = Label(self.labelFrame, text="Student surname")
        self.studentsurname.pack(side=LEFT, padx=50)

        self.entryFrame =Frame()
        self.entryFrame.pack(fill=X)

        self.studentidEntry = Entry(self.entryFrame)
        self.studentidEntry.pack(side=LEFT,padx=15,pady=10)

        self.studentNameEntry = Entry(self.entryFrame)
        self.studentNameEntry.pack(side=LEFT,padx=45)

        self.studentsurnameEntry = Entry(self.entryFrame)
        self.studentsurnameEntry.pack(side=LEFT)

        self.buttonFrame = Frame()
        self.buttonFrame.pack(fill=X)

        self.addButton = Button(self.buttonFrame, text="ADD", command = self.add_user)
        self.addButton.pack(side=LEFT, padx=60,pady=10)

        self.deleteButton = Button(self.buttonFrame, text="DELETE", command = self.delete_user)
        self.deleteButton.pack(side=LEFT,padx=60)

        self.showstudents = Button(self.buttonFrame, text ="SHow students ", command = self.insert_users)
        self.showstudents.pack(side= LEFT, padx=40)
        self.treeFrame = Frame()
        self.treeFrame.pack(fill=X)

        self.treeview = ttk.Treeview(self.treeFrame, height=15)
        self.treeview["show"] = "headings"
        self.treeview["columns"] = ("id", "name", "surname")
        self.treeview.column("id", width=150)
        self.treeview.column("name", width=150)
        self.treeview.column("surname", width=150)

        self.treeview.heading("id", text="id")
        self.treeview.heading("name", text="name")
        self.treeview.heading("surname", text="surname")
        self.treeview.pack(side=LEFT, padx=40)


    def add_user(self):

        student_id =  self.studentidEntry.get()
        student_name = self.studentNameEntry.get()
        student_surname = self.studentsurnameEntry.get()

        cursor.execute('insert into students(student_id,student_name,student_surname) values(%s,%s,%s)',[student_id,student_name,student_surname])
        connection.commit()

    def delete_user(self):

        student_id =  self.studentidEntry.get()
        cursor.execute('delete from students where student_id = %s',[student_id])
        connection.commit()

    def insert_users(self):
        for i in self.treeview.get_children():
            self.treeview.delete(i)


        cursor.execute('select * from students')
        all_students = cursor.fetchall()

        for any in all_students:
            self.treeview.insert("", 'end', values = (any[0], any[1], any[2]))



if __name__ == '__main__':

    root = Tk()
    root.configure()
    root.title('Student Management System')
    app = Gui(root)
    app.pack()
    root.geometry("900x600")
    root.mainloop()
