import sqlite3
from tkinter import messagebox

class Contact:

    def __init__(self,name,phone,mail):
        try:
            db = sqlite3.connect("contactData.db")
            cr = db.cursor()
            cr.execute("""create table if not exists contactInfo
            (id_contact integer primary key autoincrement,
            name varchar(25) not null,
            phone varchar(25) not null unique,
            mail varchar(35) not null  )""")
            cr.execute(f"insert into contactinfo(name,phone,mail) values('{name}', '{phone}', '{mail}')")
            messagebox.showinfo("Message Info", "The Contact is Added With Successfully")
            
        except Exception as e:
            messagebox.showerror("Message Error", f"Something wrong {str(e)}")

        finally:
            db.commit()
            db.close()

    @staticmethod
    def updateContact(id_contact, nameN, phoneN, mailN):
        if nameN == '' or phoneN == '' or mailN == '':
            messagebox.showerror("Message Info", "please fill all the input if you want to add a contact".title())
        else:
            try:
                db = sqlite3.connect("contactData.db")
                cr = db.cursor()
                cr.execute(f"update contactinfo set name = '{nameN}', phone = '{phoneN}', mail = '{mailN}' where id_contact = '{id_contact}'")
                messagebox.showinfo("Message Info", "The Contact is update With Successfully")
                
            except Exception as e:
                messagebox.showerror("Message Error", f"Something wrong {str(e)}")

            finally:
                db.commit()
                db.close()

    @staticmethod
    def searchContact(nameN):
        if nameN == '':
            messagebox.showerror("Message Info", "please fill the input if you want to search for a contact".title())
        else:
            try:
                db = sqlite3.connect("contactData.db")
                cr = db.cursor()
                cr.execute(f"select * from contactinfo where name = '{nameN}'")
                infoContact = cr.fetchall()
                
            except Exception as e:
                messagebox.showerror("Message Error", f"Something Wrong {str(e)}")

            finally:
                db.commit()
                db.close()
            return infoContact


    @staticmethod
    def deleteContact(name):
        if name == '':
            messagebox.showerror("Message Info", "please fill the input if you want to delete a contact".title())
        else:
            reponse = messagebox.askyesno("Message Info", "Are You Sure That You Want To delete this contact".title())
            if reponse:
                try:
                    db = sqlite3.connect("contactData.db")
                    cr = db.cursor()
                    cr.execute("""create table if not exists trashcontact
                    (id_contact integer,
                    name varchar(25),
                    phone varchar(25) ,
                    mail varchar(35))""")

                    cr.execute(f"select * from contactinfo where name = '{name}'")
                    data = cr.fetchall()
                    cr.execute(f"delete from contactinfo where name = '{name}'")
                    cr.execute(f"insert into trashcontact values('{data[0][0]}','{data[0][1]}', '{data[0][2]}', '{data[0][3]}')")
                    messagebox.showinfo("Message Info", "The Contact is deleted With Successfully")
                    
                except Exception as e:
                    messagebox.showerror("Message Error", f"Something Wrong {str(e)}")

                finally:
                    db.commit()
                    db.close()
            else:
                messagebox.showwarning("message info".title(), "the contact is not deleted".title())


    @staticmethod
    def showAllContact():
        try:
            db = sqlite3.connect("contactData.db")
            cr = db.cursor()
            cr.execute(f"select name,phone,mail from contactinfo ")
            dataShow = cr.fetchall()
    
        except Exception as e:
            messagebox.showerror("Message Error", f"Something Wrong {str(e)}")

        finally:
            db.commit()
            db.close()
        
        return dataShow

    @staticmethod
    def showTrashContact():
        try:
            db = sqlite3.connect("contactData.db")
            cr = db.cursor()
            cr.execute(f"select name,phone,mail from trashcontact ")
            datatrash = cr.fetchall()
    
        except Exception as e:
            messagebox.showerror("Message Error", f"Something Wrong {str(e)}")

        finally:
            db.commit()
            db.close()
        
        return datatrash