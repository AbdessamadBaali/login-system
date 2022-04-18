from email import message
import sqlite3
from tkinter import messagebox


class CreateAcc:
    def __init__(self,f_name, l_name,email,password, v_password):
        try:
            db = sqlite3.connect("loginSysteme.db")
            cr = db.cursor()
            cr.execute("""create table if not exists register
                        (first_name varchar(25) not null,
                        last_name varchar(25) not null,
                        email varchar(35) not null,
                        password varchar(15) not null,
                        v_password varchar(15) not null,
                        primary key (email)
                        );""")
            cr.execute(f"insert into register values('{f_name}','{l_name}','{email}','{password}','{v_password}')")
        except Exception as e:
            messagebox.showerror("Message info", f"{str(e)}")

        finally:
            db.commit()
            db.close()