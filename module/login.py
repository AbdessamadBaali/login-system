import sqlite3
from tkinter import messagebox


class Login:
    @staticmethod
    def loginAcc(email, password):
        try:
            db = sqlite3.connect("loginSysteme.db")
            cr = db.cursor()
            cr.execute(f"select email,password from register where email = '{email}' and password = '{password}'")
            data = cr.fetchall()

        except Exception as e:
            messagebox.showerror("Message info", f"{str(e)}")

        finally:
            db.commit()
            db.close()
            
        return data

    @staticmethod
    def getAccInfo(email):
        try:
            db = sqlite3.connect("loginSysteme.db")
            cr = db.cursor()
            cr.execute(f"select * from register where email = '{email}'")
            data = cr.fetchall()

        except Exception as e:
            messagebox.showerror("Message info", f"{str(e)}")

        finally:
            db.commit()
            db.close()

        return data