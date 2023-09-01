from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import random

class Student:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1369x719+0+1')
        self.window.title("Management Schools ")
        self.window.config(background="silver")
        self.window.iconbitmap("E:\\Python\\Python_desktop_student\\iconstu.ico")
        title1 = Label(self.window, text='[Student Registration System]', bg='#34495E', font=('monospace', 14), fg='white')
        title1.pack(fill=X)

        # ------ Variable student
        self.idVar = StringVar()
        self.fnameVar = StringVar()
        self.lnameVar = StringVar()
        self.genderVar = StringVar()
        self.dateVar = StringVar()
        self.type_booldVar = StringVar()
        self.stu_classVar = StringVar()
        self.parent_numberVar = StringVar()
        self.addressVar = StringVar()
        self.deleteVar = StringVar()

        # --------------- Variable Search
        self.search_byVar = StringVar()
        self.searchVar2 = StringVar()

        self.sort_dataVar = StringVar()

        global buttonAdd
        global frame3
        
        # --------------- Tools Control + Frame 1
        # get full name 
        frame1 = Frame(self.window, bg="#34495E")
        frame1.place(x=1159, y=30, width=210, height=370)

        labelFirstname = Label(frame1, text='First Name', bg='#34495E', font=('monospace', 11), fg='white')
        labelFirstname.pack()

        entryFirstname = Entry(frame1, textvariable=self.fnameVar, justify='center', bg='white', bd='3')
        entryFirstname.pack()

        labelLastname = Label(frame1, text='Last Name', bg='#34495E', font=('monospace', 11), fg='white')
        labelLastname.pack()

        entryLastname = Entry(frame1, textvariable=self.lnameVar, justify='center', bg='white', bd='3')
        entryLastname.pack()
        # -----------------------------

        labelGender = Label(frame1, text="Sex", bg='#34495E', font=('monospace', 11), fg='white')
        labelGender.pack()

        comboboxGender = ttk.Combobox(frame1, textvariable=self.genderVar)
        comboboxGender['value'] = ('Male', 'Female')
        comboboxGender.pack()

        labelDate = Label(frame1, text='Date', bg='#34495E', font=('monospace', 11), fg='white')
        labelDate.pack()

        entryDate = Entry(frame1, textvariable=self.dateVar, justify='center', bg='white', bd='3')
        entryDate.pack()

        labelTypeBlood = Label(frame1, text='Type Blood', bg='#34495E', font=('monospace', 11), fg='white')
        labelTypeBlood.pack()

        comboboxTypeBlood = ttk.Combobox(frame1, textvariable=self.type_booldVar)
        comboboxTypeBlood['value'] = ('AB+', 'AB-', 'A+', 'A-', 'B+', 'B-', 'O+', 'O-')
        comboboxTypeBlood.pack()

        labelClass = Label(frame1, text='Class ', bg='#34495E', font=('monospace', 11), fg='white')
        labelClass.pack()

        comboboxClass = ttk.Combobox(frame1, textvariable=self.stu_classVar)
        comboboxClass['value'] = ('High 1', 'High 2', 'High 3')
        comboboxClass.pack()

        labelClass = Label(frame1, text='Parent No. ', bg='#34495E', font=('monospace', 11), fg='white')
        labelClass.pack()

        entryparent = Entry(frame1, textvariable=self.parent_numberVar, justify='center', bg='white', bd='3')
        entryparent.pack()

        labelAddres = Label(frame1, text='Address', bg='#34495E', font=('monospace', 11), fg='white')
        labelAddres.pack()

        entryaddres = Entry(frame1, textvariable=self.addressVar, justify='center', bg='white', bd='3')
        entryaddres.pack()
        # -----------------

        # ------- Control Panel + Frame 2
        frame2 = Frame(self.window, bg='#34495E')
        frame2.place(x=1159, y=412, width=210, height=284)

        title2 = Label(frame2, text='Control Panel', font=('Deco', 14), fg='white', bg='#34495E')
        title2.pack()

        buttonAdd = Button(frame2, text="Add Stu", bg='#8E44AD', fg='white',
                            font=('monospace', 12), width=12, command=self.addStudent)
        buttonAdd.place(x=48, y=35)

        buttonUpdate = Button(frame2, text="Update Stu", bg='#8E44AD', fg='white',
                            font=('monospace', 12), width=12, command=self.updateStudent)
        buttonUpdate.place(x=48, y=75)

        entrydelete = Entry(frame2, textvariable=self.deleteVar, justify='center', bg='white', bd='3')
        entrydelete.place(x=41, y=135)

        labelAddres = Label(frame2, text='Enter ID To Delete', bg='#34495E', font=('monospace', 10), fg='white')
        labelAddres.place(x=50, y=110)
        buttonDelete = Button(frame2, text="Delete Stu", bg='#E72111', fg='white',
                            font=('monospace', 12), width=12, command=self.deleteStudent)
        buttonDelete.place(x=48, y=170)

        buttonClear = Button(frame2, text="Clear", bg='#8E44AD', fg='white',
                            font=('monospace', 12), width=12, command=self.clearEntrys)
        buttonClear.place(x=48, y=210)
        

        # ------------- Search area + frame 3
        frame3 = Frame(self.window, bg='#34495E')
        frame3.place(x=2, y=30, width=1150, height=70)

        comboboxSearch_by = ttk.Combobox(frame3, textvariable=self.search_byVar)
        comboboxSearch_by['value'] = ('ID', 'First Name', "Last Name")
        comboboxSearch_by.place(x=999, y=20)

        labelSearchby = Label(frame3, text='Search By', bg='#34495E', font=('monospace', 11), fg='white')
        labelSearchby.place(x=915, y=21)

        entrysearch = Entry(frame3, textvariable=self.searchVar2, justify='center', bg='white', bd='3')
        entrysearch.place(x=740, y=20)

        buttonSearch = Button(frame3, text="Search", bg='#8E44AD', fg='white',
                            font=('monospace', 12), width=11, command=self.searchStudent)
        buttonSearch.place(x=605, y=17)

        buttonClearSearch = Button(frame3, text="Clear", bg='#8E44AD', fg='white',
                            font=('monospace', 12), width=11, command=self.clearSearch)
        buttonClearSearch.place(x=485, y=17)

        labelSort = Label(frame3, text='Sort By:', bg='#34495E', font=('monospace', 11), fg='white')
        labelSort.place(x=3, y=21)

        comboboxSort = ttk.Combobox(frame3, textvariable=self.sort_dataVar)
        comboboxSort['value'] = ('ID', 'First Name', 'Last Name')
        comboboxSort.place(x=68, y=21)

        # ------------------------------

        # ----------- View Data and Result + frame 4
        frame4 = Frame(self.window, bg='#34495E')
        frame4.place(x=2, y=105, width=1150, height=600)

        # ------ Treeview 
        self.student_table = ttk.Treeview(frame4, columns=('address', 'parent_no', 'class', 'type_boold', 'date', 'gender', 'lname', 'fname', 'id'))
        self.student_table.place(x=10, y=0, width=1144, height=598)
        
        # ------ Scroll
        scroll_y = ttk.Scrollbar(frame4, orient=VERTICAL, command=self.student_table.yview)
        self.student_table.configure(yscrollcommand=scroll_y.set)
        scroll_y.pack(side=LEFT, fill=Y)

        self.student_table['show'] = 'headings'
        self.student_table.heading('address', text='Address')
        self.student_table.heading('parent_no', text='Parent No')
        self.student_table.heading('class', text='Class')
        self.student_table.heading('type_boold', text='Type Blood')
        self.student_table.heading('date', text='Bitrh Day')
        self.student_table.heading('gender', text='Gender')
        self.student_table.heading('lname', text='Last Name')
        self.student_table.heading('fname', text='First Name')
        self.student_table.heading('id', text='ID')

        self.student_table.column('address', width=115, anchor='center')
        self.student_table.column('parent_no', width=80, anchor='center')
        self.student_table.column('class', width=50, anchor='center')
        self.student_table.column('type_boold', width=30, anchor='center')
        self.student_table.column('date', width=50, anchor='center')
        self.student_table.column('gender', width=30, anchor='center')
        self.student_table.column('lname', width=100, anchor='center')
        self.student_table.column('fname', width=100, anchor='center')
        self.student_table.column('id', width=50, anchor='center')

        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)
        comboboxSort.bind('<<ComboboxSelected>>', self.sortData)
        self.fetch_all()
        
    def addStudent(self):
        # create id 
        random1 = random.randint(100, 1000)
        random2 = random.randint(100, 1000)

        idStu = str(random1) + str(random2) # get id and convert to str
        fname = self.fnameVar.get().capitalize()
        lname = self.lnameVar.get().capitalize()
        gender = self.genderVar.get()
        date = self.dateVar.get()
        blood = self.type_booldVar.get()
        stuClass = self.stu_classVar.get()
        perNum = self.parent_numberVar.get()
        address = self.addressVar.get()

        if len(fname) > 0 and len(lname) > 0:
            if gender:
                if date:
                    if blood:
                        if stuClass:
                            if perNum:
                                if address:
                                    db = sqlite3.connect("E:\\Python\\Python_desktop_student\\School_stud.db")
                                    cursor = db.cursor()
                                    sql = f"INSERT INTO student(id, first_name, last_name, gender, birth_date, type_blood, class, perent_no, address)"\
                                        f"values('{idStu}', '{fname}', '{lname}', '{gender}', '{date}', '{blood}', '{stuClass}', '{perNum}', '{address}')"
                                    cursor.execute(sql)
                                    db.commit()
                                    self.clearEntrys()
                                    self.deleteItems()
                                    self.fetch_all()
                                    messagebox.showinfo('Done', 'Successfully Add New Student ..')
                                else:
                                    messagebox.showerror('Adress Empty!', 'You must enter address !')
                            else:
                                messagebox.showerror('Perent Number Empty!', 'You must enter number perent student!')
                        else:
                            messagebox.showerror('Class Empty!', 'You must choice class for student !')
                    else:
                        messagebox.showerror('Type Blood Empty!', 'You must choice type blood !')
                else:
                    messagebox.showerror('Date Empty!', 'Enter correct date !')
            else:
                messagebox.showerror('Gender Empty!', 'You must choice gender !')
        else:
            messagebox.showerror('Name Empty!', 'You must enter first name and last name !')

    def deleteStudent(self):
        idStud = self.deleteVar.get()

        if len(idStud) != 6:
            messagebox.showerror('Sorry', 'The id must be 10 digits !')

        else:
            db = sqlite3.connect("E:\\Python\\Python_desktop_student\\School_stud.db")
            cursor = db.cursor()
            cursor.execute(f"SELECT * FROM student WHERE id = '{idStud}' ")
            row = cursor.fetchone()
            if row:
                ask1 = messagebox.askyesno('Delete Confirm', 'Are you sure to deleted ?')
                if ask1:
                    cursor.execute(f"DELETE FROM student WHERE id = '{idStud}' ")
                    db.commit()
                    messagebox.showinfo("Successful", "Deleted is done ..")
                    db.close()
                    self.deleteItems()
                    self.fetch_all()
                    self.clearEntrys()
                else:
                    pass
            else:
                messagebox.showerror('Sorry', "This id not can't found !!")

    def updateStudent(self):
        db = sqlite3.connect("E:\\Python\\Python_desktop_student\\School_stud.db")
        cursor = db.cursor()
        fname = self.fnameVar.get()
        lname = self.lnameVar.get()
        gender = self.genderVar.get()
        date = self.dateVar.get()
        blood = self.type_booldVar.get()
        stuClass = self.stu_classVar.get()
        perNum = self.parent_numberVar.get()
        address = self.addressVar.get()

        if len(fname) > 0 and len(lname) > 0 and len(gender) > 0 and len(date) > 0 \
                and len(blood) > 0 and len(stuClass) > 0 and len(perNum) > 0 and len(address) > 0:
            cursorRow = self.student_table.focus()
            contents = self.student_table.item(cursorRow)
            row = contents['values']
            fullName = row[7]+" "+row[6]
            idStud = row[8]
            
            ask2 = messagebox.askquestion("Update Data", f"Are you sure about edit: {fullName}")
            if ask2 == "yes":
                sql = f"UPDATE student SET address = '{address}', perent_no = '{perNum}', class = '{stuClass}', type_blood = '{blood}',\
                    birth_date = '{date}', gender = '{gender}', last_name = '{lname.capitalize()}', first_name = '{fname.capitalize()}' WHERE id = '{idStud}' "
                cursor.execute(sql)
                db.commit()
                db.close()
                self.deleteItems()
                self.fetch_all()
                self.clearEntrys()
                messagebox.showinfo('Done', 'Update done ..')
            else:
                pass
        else:
            pass
   
    def clearEntrys(self):
        self.fnameVar.set('')
        self.lnameVar.set('')
        self.genderVar.set('')
        self.dateVar.set('')
        self.type_booldVar.set('')
        self.stu_classVar.set('')
        self.parent_numberVar.set('')
        self.addressVar.set('')
        self.deleteVar.set('')
        buttonAdd.config(state='normal')
        self.deleteItems()
        self.fetch_all()

    def fetch_all(self):
        db = sqlite3.connect("E:\\Python\\Python_desktop_student\\School_stud.db")
        cursor = db.cursor()
        cursor.execute("SELECT address, perent_no, class, type_blood, birth_date, gender, last_name, first_name, id FROM student ORDER BY id")
        rows = cursor.fetchall()
        labelCount = Label(frame3, text=f'Number of Students: {len(rows)}', bg='#34495E', font=('monospace', 11), fg='white')
        labelCount.place(x=224, y=12)
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.children)

            for row in rows:
                self.student_table.insert("", END, values=row)
            db.commit()
        else:
            pass
        db.close()

    def searchStudent(self):
        global labelResultSerach
        self.clearEntrys()
        if len(self.search_byVar.get()) == 0:
            messagebox.showwarning('Sorry', 'You must select search by !')

        elif len(self.searchVar2.get()) == 0:
             messagebox.showwarning('Sorry', 'You must write id or first Name !')
        else:

            serach1 = self.search_byVar.get()
            serach2 = self.searchVar2.get()
            if self.search_byVar.get() == "First Name":
                serach1 = "first_name"
            if self.search_byVar.get() == "Last Name":
                serach1 = "last_name"

            db = sqlite3.connect("E:\\Python\\Python_desktop_student\\School_stud.db")
            cursor = db.cursor()
            cursor.execute("SELECT address, perent_no, class, type_blood, birth_date, gender, last_name, first_name, id FROM student WHERE "+str(serach1)+" LIKE '%"+str(serach2)+"%'")
            rows = cursor.fetchall()
            labelResultSerach = Label(frame3, text=f'Research Results: {len(rows)}', bg='#34495E', font=('monospace', 11), fg='#6FE711')
            labelResultSerach.place(x=224, y=34)
            if len(rows) != 0:
                self.deleteItems()
                self.student_table.delete(*self.student_table.children)

                for row in rows:
                    self.student_table.insert("", END, values=row)
                db.commit()
            else:
                self.deleteItems()
                messagebox.showwarning('Sorry', "No can't found !")
                labelResultSerach.config(text='')
            cursor.close()
    
    def deleteItems(self):
        for items in self.student_table.get_children():
            self.student_table.delete(items)

    def get_cursor(self, event):
        cursor_row = self.student_table.focus()
        contents = self.student_table.item(cursor_row)
        row = contents['values']
        if len(row) > 0:
            buttonAdd.config(state='disable')
            self.addressVar.set(row[0])
            self.parent_numberVar.set(row[1])
            self.stu_classVar.set(row[2])
            self.type_booldVar.set(row[3])
            self.dateVar.set(row[4])
            self.genderVar.set(row[5])
            self.lnameVar.set(row[6])
            self.fnameVar.set(row[7])

        else:
            buttonAdd.config(state='normal')
    
    def clearSearch(self):
        labelResultSerach.config(text='')
        buttonAdd.config(state='normal')
        self.search_byVar.set('')
        self.searchVar2.set('')
        self.sort_dataVar.set('')
        self.deleteItems()
        self.fetch_all()

    def sortData(self, event):
        if self.sort_dataVar.get() == "ID":
            sortData = 'id'
        if self.sort_dataVar.get() == "First Name":
            sortData = 'first_name'
        if self.sort_dataVar.get() == "Last Name":
            sortData = 'last_name'

        self.deleteItems()

        db = sqlite3.connect("E:\\Python\\Python_desktop_student\\School_stud.db")
        cursor = db.cursor()
        cursor.execute(f"SELECT address, perent_no, class, type_blood, birth_date, gender, last_name, first_name, id FROM student ORDER BY {sortData}")
        rows = cursor.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.children)

            for row in rows:
                self.student_table.insert("", END, values=row)
            db.commit()
        else:
            pass
        db.close()


app = Tk()
Student(app)
app.mainloop()

