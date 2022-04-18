import re 
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from module.contact import Contact
from module.createAcc import CreateAcc
from module.login import Login


def createAccount():
    root = Tk()
    root.geometry("400x550+300+10")
    root.iconbitmap("iconesW/login.ico")
    root.title("login system".upper())
    root.resizable(False, False)
    root.config(bg="#ffeaa7")

    # title of the app
    titleapp = Label(root, text='sing up'.upper(), font=('verdana', 18),bg="#ffeaa7")
    titleapp.place(x=10, y=10)

    para = Label(root, text='join with us'.title(), font=12,bg="#ffeaa7")
    para.place(x=10, y=45)

    # label and entry for the first name
    first_name = Label(root, text='first name'.title(), font=12,bg="#ffeaa7")
    valFirstName = StringVar()
    entry_firstN = Entry(root, width=25, textvariable=valFirstName)
    first_name.place(x=30 , y= 80)
    entry_firstN.place(x=30 , y= 120)

    # label and entry for the last name
    last_name = Label(root, text='last name'.title(), font=12,bg="#ffeaa7")
    valLastName = StringVar()
    entry_firstL = Entry(root, width=25, textvariable=valLastName)
    last_name.place(x=200 , y= 80)
    entry_firstL.place(x=200 , y= 120)

    # label and entry for email
    mail = Label(root, text='email'.title(), font=12,bg="#ffeaa7")
    valEmail = StringVar()
    entry_mail = Entry(root, width=53, textvariable=valEmail)
    mail.place(x=30 , y= 160)
    entry_mail.place(x=30 , y= 200)


    # label and entry for password
    password = Label(root, text='password'.title(), font=12,bg="#ffeaa7")
    valPass = StringVar()
    entry_pass = Entry(root, show="*", width=53, textvariable=valPass)
    password.place(x=30 , y= 240)
    entry_pass.place(x=30 , y= 280)


    # label and entry for validate password
    password_valide = Label(root, text='validate password'.title(), font=12,bg="#ffeaa7")
    valPassValid = StringVar()
    entry_pass_valide = Entry(root, show="*", width=53, textvariable=valPassValid)
    password_valide.place(x=30 , y= 320)
    entry_pass_valide.place(x=30 , y= 360)


    # checkbox with label
    valcheck = IntVar()
    check = Checkbutton(root, text='I Agree the terms & condition'.title(),variable=valcheck,
                            bg="#ffeaa7", onvalue=1, offvalue=0)
    check.place(x=30 , y= 400)

    # link for window create account
    link1 = Button(root, text="i already i have an account".title(),bg="#ffeaa7", fg="blue", borderwidth=0,
    command=lambda : changeLogIn(root))
    link1.place(x=30 , y= 440)


    def CreateAccount():
        f_name = valFirstName.get()
        l_name = valLastName.get()
        email = valEmail.get()
        password = valPass.get()
        v_password = valPassValid.get()
        check = valcheck.get()
        if check == 1:
            if f_name != '' or l_name != '' or email != ''or password != '' or v_password != '':
                if len(password) >= 8 :
                    check_mail = re.findall(r"^[a-z0-9._-]+@[gmail.com]+\.[(com|fr)]+", email) 
                    if check_mail[0] == email:
                        if  password == v_password:
                            CreateAcc(f_name, l_name,email,password,v_password)
                            messagebox.showinfo("Message info", f"{f_name} {l_name} your account is create with successfully")
                            changeLogIn(root)
                        else:
                            messagebox.showwarning("Message info", "password and validate password should be the same".title())
                    else:
                        messagebox.showwarning("Message info", "email is incorrect".title())
                else:
                    messagebox.showwarning("Message info", "the password show be more than 8 caracter".title())
                    
        else:
            messagebox.showerror("Message info", "You must agree to the terms and conditions\nif you want to create an account and all the inputs are required".title())
    
    # button for creat acount
    btn = Button(root, text="create account".title(), command=CreateAccount)
    btn.place(x=30 , y= 480)
    root.mainloop()





def logIn(root):
    root.geometry("400x350+300+10")
    root.config(bg="#ffeaa7")
    root.iconbitmap("iconesW/login.ico")
    root.title("login system".upper())
    root.resizable(False, False)

    # title of the app
    titleapp = Label(root, text='sing in'.upper(), font=('verdana', 18),bg="#ffeaa7")
    titleapp.place(x=10, y=10)

    para = Label(root, text='join with us'.title(), font=12,bg="#ffeaa7")
    para.place(x=10, y=45)

    # label and entry for the email account
    email_acc = Label(root, text='email'.title(), font=12,bg="#ffeaa7")
    valEmailLogin = StringVar()
    entry_emailAcc= Entry(root, width=50, textvariable=valEmailLogin)
    email_acc.place(x=30 , y= 80)
    entry_emailAcc.place(x=30 , y= 120)

    # label and entry for password
    password = Label(root, text='password'.title(), font=12,bg="#ffeaa7")
    valPassLogin = StringVar()
    entry_pass = Entry(root, show="*", width=50, textvariable=valPassLogin)
    password.place(x=30 , y= 160)
    entry_pass.place(x=30 , y= 200)

    # link for window create account
    info = Label(root, text="if you don't have an account".title(),bg="#ffeaa7")
    link1 = Button(root, text="create one".title(), fg="blue", borderwidth=0,bg="#ffeaa7",
    command=lambda : changeToCreate(root))
    info.place(x=30 , y= 240)
    link1.place(x=200 , y= 240)

    def login():
        emailLog = valEmailLogin.get()
        passwordLog = valPassLogin.get()
        check = Login.loginAcc(emailLog, passwordLog)
        if len(check) > 0:
            if check[0][0] == emailLog and check[0][1] == passwordLog:
                changeContact(root,emailLog)
        else:
            messagebox.showerror("Message Info", "password or email incorrect".title())
        
    btn_login = Button(root, text='log in'.title(), command=login)
    btn_login.place(x=30 , y=280)

    root.mainloop()


def contactbook(root, emailLog):
    # fuction for add a contact to contact book
    def addContact():
        name  = valName.get()
        phone = valPhone.get()
        mail = valEmail.get()
        if name == '' or phone == '' or mail == '':
            messagebox.showerror("Message Info", "please fill all the input if you want to add a contact".title())
        else:
            check_phone = re.findall(r"^[+212][0-9]{12}", phone) 
            check_mail = re.findall(r"^[a-z0-9._-]+@[gmail.com]+\.[(com|fr)]+", mail) 
            if check_phone[0] == phone:
                if check_mail[0] == mail:
                    Contact(name,phone,mail)
                else:
                    messagebox.showerror("Message Error", "the email should be like xxxxxx@gmail.com or xxxxxx@gmail.fr".title())
            else:
                messagebox.showerror("Message Error", "the number phone should start with +212\nand take 10 number afther +212".title())

    # function for update a contact and inside the function i create another window
    def updatecontact():
        contact_f = Toplevel()
        contact_f.title("update contact".upper())
        contact_f.geometry("400x350")
        contact_f.iconbitmap("iconesW/contact.ico")
        contact_f.config(bg="#ffeaa7")
        contact_f.resizable(False,False)

        # label for search name that you need to update
        name_search = Label(contact_f, text="Name",bg="#ffeaa7")
        valNameS = StringVar()
        Entry_nameSeach = Entry(contact_f, font=15, width=25, textvariable=valNameS)
        name_search.place(x=10, y=50)
        Entry_nameSeach.place(x=53, y=50)

        # function for search contact if exists we give the option for update
        def search():
            nameN = valNameS.get()
            infocheck = Contact.searchContact(nameN)
            if len(infocheck) > 0:
                # label for name  update
                name = Label(contact_f, text="New Name",bg="#ffeaa7")
                valName = StringVar()
                valName.set(infocheck[0][1])
                Entry_name = Entry(contact_f, font=15, width=25, textvariable=valName)
                name.place(x=10, y=100)
                Entry_name.place(x=130, y=100)

                # label for telephon update
                phone = Label(contact_f, text="New Phone Number",bg="#ffeaa7")
                valPhone = StringVar()
                valPhone.set(infocheck[0][2])
                Entry_phone = Entry(contact_f, font=15, width=25, textvariable=valPhone)
                phone.place(x=10, y=150)
                Entry_phone.place(x=130, y=150)

                # label for email update
                email = Label(contact_f, text="New Email",bg="#ffeaa7")
                valEmail = StringVar()
                valEmail.set(infocheck[0][3])
                Entry_email = Entry(contact_f, font=15, width=25, textvariable=valEmail)
                email.place(x=10, y=200)
                Entry_email.place(x=130, y=200)

                # function for validate the update contact
                def save():
                    new_name = valName.get()
                    new_phone = valPhone.get()
                    new_mail = valEmail.get()
                    Contact.updateContact(infocheck[0][0],new_name, new_phone, new_mail)

                # validation the up date
                btn_save = Button(contact_f, text='save'.upper(),bg="#ffeaa7",command=save)
                btn_save.place(x=10, y=250)
            else :
                messagebox.showwarning("Message Info", "This Contact Is Not Exists")

        # title of contact update 
        title_contact = Label(contact_f, text='contact update'.title(), font=("verdana", 20),
                            fg="#f90",bg="#ffeaa7")
        title_contact.pack()

        # button for search a contact book
        btn = Button(contact_f, text="search contact".title(),bg="#ffeaa7", command=search)
        btn.place(x=290, y=48)

    def delete():
        delete_f = Toplevel()
        delete_f.title("delete contact".upper())
        delete_f.geometry("400x100")
        delete_f.iconbitmap("iconesW/contact.ico")
        delete_f.config(bg="#ffeaa7")
        delete_f.resizable(False,False)

        # label for search name that you need to update
        name_delete = Label(delete_f, text="Name",bg="#ffeaa7")
        valNameD = StringVar()
        Entry_nameDelete = Entry(delete_f, font=15, width=25, textvariable=valNameD)
        name_delete.place(x=10, y=50)
        Entry_nameDelete.place(x=53, y=50)

        # button for search a contact book
        btn = Button(delete_f, text="delete contact".title(),bg="#ffeaa7",
                    command=lambda : Contact.deleteContact(valNameD.get()))
        btn.place(x=290, y=48)


    # show all the contact
    def show():
        show_f = Toplevel()
        show_f.title("show all contact".upper())
        show_f.geometry("500x300")
        show_f.iconbitmap("iconesW/contact.ico")
        show_f.config(bg="#ffeaa7")
        show_f.resizable(False,False)

        titleTab = Label(show_f, text='list of all the contact'.title(), font=16, bg="#ffeaa7")
        titleTab.pack()

        dataShow = Contact.showAllContact()

        area = ('nom', 'phone', 'email')
        table = ttk.Treeview(show_f, columns=area, show='headings')
        for i in range(len(area)):
            table.column(area[i], width=150)
            table.heading(area[i], text=area[i])
        table.pack()
        # insert into the the table
        for i in range(len(dataShow)):
            table.insert('', 'end', values=dataShow[i])


    # show all the trash contact
    def showtrash():
        showTrash_f = Toplevel()
        showTrash_f.title("show all contact".upper())
        showTrash_f.geometry("500x300")    
        showTrash_f.iconbitmap("iconesW/contact.ico")
        showTrash_f.config(bg="#ffeaa7")
        showTrash_f.resizable(False,False)

        titleTab = Label(showTrash_f, text='list of all trash contact'.title(), font=16, bg="#ffeaa7")
        titleTab.pack()

        datatrash = Contact.showTrashContact()

        area = ('nom', 'phone', 'email')
        table = ttk.Treeview(showTrash_f, columns=area, show='headings')
        for i in range(len(area)):
            table.column(area[i], width=150)
            table.heading(area[i], text=area[i])
        table.pack()
        # insert into the the table
        for i in range(len(datatrash)):
            table.insert('', 'end', values=datatrash[i])


    # def showProfiel():
    #     profile_f = Toplevel()
    #     profile_f.title("show all contact".upper())
    #     profile_f.geometry("500x300")    
    #     profile_f.iconbitmap("iconesW/contact.ico")
    #     profile_f.config(bg="#ffeaa7")
    #     profile_f.resizable(False,False)
    #     infoAcc = Login.getAccInfo(emailLog)

    # ---------- gui app contact book

    root.title("contact book".upper())
    root.geometry("400x350")
    root.iconbitmap("iconesW/contact.ico")
    root.config(bg="#ffeaa7")
    root.resizable(False,False)

    titleApp = Label(root, text="Contact book", font=("verdana", 20), fg="#f90",bg="#ffeaa7")
    titleApp.place(x=10, y=5)

    # the account name
    infoAcc = Login.getAccInfo(emailLog)
    full_name = infoAcc[0][0] + ' ' + infoAcc[0][1]
    accName = Label(root, text=full_name.title(), bg='#ffeaa7')
    accName.place(x=200, y=15)

    # label for name
    name = Label(root, text="Name",bg="#ffeaa7")
    valName = StringVar()
    Entry_name = Entry(root, font=15, width=25, textvariable=valName)
    name.place(x=10, y=50)
    Entry_name.place(x=110, y=50)

    # label for telephon
    phone = Label(root, text="Phone Number",bg="#ffeaa7")
    valPhone = StringVar()
    Entry_phone = Entry(root, font=15, width=25, textvariable=valPhone)
    phone.place(x=10, y=100)
    Entry_phone.place(x=110, y=100)

    # label for email
    email = Label(root, text="Email",bg="#ffeaa7")
    valEmail = StringVar()
    Entry_email = Entry(root, font=15, width=25, textvariable=valEmail)
    email.place(x=10, y=150)
    Entry_email.place(x=110, y=150)

    # btn for add a contact
    addBtn = Button(root, text="add contact".title(),bg="#ffeaa7",padx=10,pady=5, command=addContact)
    addBtn.place(x=10, y=200)

    # btn for update a contact
    updateBtn = Button(root, text="update contact".title(),bg="#ffeaa7",padx=10,pady=5, command=updatecontact)
    updateBtn.place(x=120, y=200)

    # btn for delete a contact
    deleteBtn = Button(root, text="delete contact".title(),bg="#ffeaa7",padx=10,pady=5, command=delete)
    deleteBtn.place(x=240, y=200)

    # btn for show a contact
    showBtn = Button(root, text="show all contact".title(),bg="#ffeaa7",padx=10,pady=5, command=show)
    showBtn.place(x=10, y=250)

    # btn for show trash contact
    showBtn = Button(root, text="show trash contact".title(),bg="#ffeaa7",padx=10,pady=5, command=showtrash)
    showBtn.place(x=140, y=250)

    # button for log out  ur account
    exitBtn = Button(root, text="Log out",bg="#ffeaa7",padx=10,pady=5, command=lambda : logoutContact(root))
    exitBtn.place(x=300, y=250)

    # button for show info   account
    # exitBtn = Button(root, text="show profiel".title(),bg="#ffeaa7",padx=10,pady=5, command=showProfiel)
    # exitBtn.place(x=10, y=300)

    root.mainloop()


# functio for move to create account window
def logoutContact(root):
    root.destroy()
    root = Tk()
    logIn(root)    
    root.mainloop()


# functio for move to create account window
def changeContact(root, emailLog):
    root.destroy()
    root = Tk()
    contactbook(root,emailLog)     
    root.mainloop()

# functio for move to log in window
def changeLogIn(root):
    root.destroy()
    root = Tk()
    logIn(root)     
    root.mainloop()

# functio for move to create account window
def changeToCreate(root):
    root.destroy()
    createAccount()     
    root.mainloop()

def mainApp():
    root = Tk()
    logIn(root)
    root.mainloop()

mainApp()