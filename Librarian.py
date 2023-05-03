import mysql.connector
import bcrypt
from PySide2.QtWidgets import QTableWidgetItem, QMessageBox
from PySide2.QtCore import Qt

class Librarian:
    def __init__(self, ui = None):
        self.ui = ui
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="library"
        )
        self.cursor = self.conn.cursor()
        self.create_librarian_table()
        self.create_default_librarian()
        if ui is not None:
            self.loadLibrarians(self.get_all_librarians())


    def create_default_librarian(self):
        self.cursor.execute("SELECT * FROM librarian  WHERE login='admin' ")
        fetch = self.cursor.fetchone()
        if fetch is None:
            nom ="admin"
            prenom = "admin"
            isAdmin = 1
            login="admin"
            password = "admin"
            salt = bcrypt.gensalt()
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
            query = '''INSERT INTO librarian (nom, prenom, isAdmin, login, salt, password, creationDate) 
                                            VALUES (%s, %s, %s, %s, %s, %s ,CURDATE())'''
            values = (nom, prenom, isAdmin, login, salt, hashed_password)
            self.cursor.execute(query, values)
            self.conn.commit()

    def loadLibrarians(self,data):
        self.ui.tableWidget_5.clearContents()
        self.ui.tableWidget_5.setRowCount(0)
        for row_number, row_data in enumerate(data):
            self.ui.tableWidget_5.insertRow(row_number)
            for column_number, column_data in enumerate(row_data):
                item = str(column_data)
                qtablewidgetitem = QTableWidgetItem()
                self.ui.tableWidget_5.setItem(row_number, column_number, qtablewidgetitem)
                qtablewidgetitem.setText(item)

    def get_all_librarians(self):
        self.cursor.execute("SELECT idLib,nom,prenom,isAdmin,creationDate FROM librarian")
        return self.cursor.fetchall()

    def create_librarian_table(self):
        try:
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS librarian (
                idLib INTEGER PRIMARY KEY AUTO_INCREMENT,
                nom VARCHAR(50) NOT NULL,
                prenom VARCHAR(50) NOT NULL,
                isAdmin BOOLEAN NOT NULL,
                login VARCHAR(255) NOT NULL UNIQUE,
                salt VARCHAR(255),
                password VARCHAR(255) NOT NULL,
                creationDate DATE
            )''')
        except:
            print("Error creating users table")

    def create_librarian(self):

        nom = self.ui.addLibrarianNom.text()
        prenom = self.ui.addLibrarianPrenom.text()
        login = self.ui.addLibrarianLogin.text()
        password=self.ui.addLibrarianPassword.text()
        confirm_password = self.ui.addLibrarianConf.text()
        isAdmin = self.ui.addAdmin.currentText()

        if nom and prenom and login and password and confirm_password:
            if confirm_password == password:
                self.cursor.execute('SELECT * FROM librarian WHERE login=%s',(login,))
                result = self.cursor.fetchone()
                if not result:
                    isAdmin= False if isAdmin == "is Admin" or isAdmin=="No" else True
                    salt = bcrypt.gensalt()
                    hashed_password = bcrypt.hashpw(password.encode('utf-8'),salt)
                    query = '''INSERT INTO librarian (nom, prenom, isAdmin, login, salt, password, creationDate) 
                                VALUES (%s, %s, %s, %s, %s, %s ,CURDATE())'''
                    values = (nom, prenom, isAdmin,login, salt,hashed_password)
                    self.cursor.execute(query, values)
                    self.conn.commit()
                    print(f"{nom} {prenom} has been added to the database.")
                    self.loadLibrarians(self.get_all_librarians())
                    self.ui.addLibrarianNom.setText("")
                    self.ui.addLibrarianPrenom.setText("")
                    self.ui.addLibrarianLogin.setText("")
                    self.ui.addLibrarianPassword.setText("")
                    self.ui.addLibrarianConf.setText("")
                    self.ui.addAdmin.setCurrentText("is Admin")
                else:
                    dialog1 = QMessageBox(self.ui.centralwidget)
                    dialog1.setText("login exist deja")
                    dialog1.setWindowTitle("Error !!")
                    dialog1.setIcon(QMessageBox.Critical)
                    dialog1.exec_()

            else:
                dialog2 = QMessageBox(self.ui.centralwidget)
                dialog2.setText("password not matching")
                dialog2.setWindowTitle("Error !!")
                dialog2.setIcon(QMessageBox.Critical)
                dialog2.exec_()

    def delete_librarian(self):
        id = self.ui.deleteLibrarianId.text()
        if id:
            self.cursor.execute("SELECT * FROM librarian WHERE idLib=%s",(id,))
            res = self.cursor.fetchone()
            if not res:
                dialog = QMessageBox(self.ui.centralwidget)
                dialog.setText("voulez vous vraiment supprimer !!")
                dialog.setWindowTitle("")
                dialog.setIcon(QMessageBox.Question)
                dialog.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
                result = dialog.exec_()
                if result==QMessageBox.Ok:
                    self.cursor.execute("DELETE FROM librarian WHERE idLib = %s", (id,))
                    self.conn.commit()
                    print(f"Librarian with ID {id} has been deleted from the database.")
                    self.loadLibrarians(self.get_all_librarians())
                    self.ui.deleteLibrarianId.setText("")
            else:
                dialog2 = QMessageBox(self.ui.centralwidget)
                dialog2.setText("librarian n'existe pas")
                dialog2.setWindowTitle("Error !!")
                dialog2.setIcon(QMessageBox.Critical)
                dialog2.exec_()



    def update(self, id, nom=None, prenom=None, isAdmin=None,login=None, password=None):
        if id:
            query = "UPDATE librarian SET"
            values = []
            if nom is not None:
                query += " nom = %s,"
                values.append(nom)
            if prenom is not None:
                query += " prenom = %s,"
                values.append(prenom)
            if isAdmin is not None:
                isAdmin = False if isAdmin=="No" else True
                query += " isAdmin = %s,"
                values.append(isAdmin)
            if login is not None:
                query += " login = %s,"
                values.append(login)
            if password is not None:
                self.cursor.execute('SELECT salt FROM librarian WHERE idLib=%s',(id,))
                salt = self.cursor.fetchone()
                hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
                query += " password = %s,"
                values.append(hashed_password)

            query = query[:-1] + " WHERE idLib = %s"
            values.append(id)
            self.cursor.execute(query, values)
            self.conn.commit()
        else:
            dialog = QMessageBox(self.ui.centralwidget)
            dialog.setText("id ne doit pas etre vide")
            dialog.setWindowTitle("Error !!")
            dialog.setIcon(QMessageBox.Critical)
            dialog.exec_()
    
    def edit_Librarian(self):
        Id=self.ui.editLibrarianId.text()
        Nom =self.ui.editLibrarianNom.text()
        Prenom= self.ui.editLibrarianPrenom.text()
        IsAdmin= self.ui.editAdmin.currentText()
        Login=self.ui.editLibrarianLogin.text()
        Password=self.ui.editLibrarianPassword.text()
        Conf_Password=self.ui.editLibrarianConf.text()

        if Id:
            if not Nom: Nom=None
            if not Prenom: Prenom=None
            if not Login: Login=None
            if IsAdmin=="is Admin": IsAdmin=None
            if Password and Password!=Conf_Password:
                dialog = QMessageBox(self.ui.centralwidget)
                dialog.setText("password not matching")
                dialog.setWindowTitle("Error !!")
                dialog.setIcon(QMessageBox.Critical)
                dialog.exec_()
            else:
                if not Password: Password=None
                self.update(Id,nom=Nom,prenom=Prenom,isAdmin=IsAdmin,login=Login,password=Password)
                self.ui.editLibrarianId.setText("")
                self.ui.editLibrarianNom.setText("")
                self.ui.editLibrarianPrenom.setText("")
                self.ui.editLibrarianLogin.setText("")
                self.ui.editLibrarianConf.setText("")
                self.ui.editLibrarianPassword.setText("")
                self.ui.editAdmin.setCurrentText("is Admin")
                
                self.loadLibrarians(self.get_all_librarians())
            
        else:
            dialog = QMessageBox(self.ui.centralwidget)
            dialog.setText("id ne doit pas etre vide")
            dialog.setWindowTitle("Error !!")
            dialog.setIcon(QMessageBox.Critical)
            dialog.exec_()

    def search(self,id=None, nom=None, prenom=None, isAdmin=None):
        sql = "SELECT idLib,nom,prenom,isAdmin,creationDate FROM librarian WHERE"
        values = []
        if id is not None:
            sql += " idLib = %s AND"
            values.append(id)
        if nom is not None:
            sql += " nom = %s AND"
            values.append(nom)
        if prenom is not None:
            sql += " prenom = %s AND"
            values.append(prenom)
        if isAdmin is not None:
            isAdmin= False if isAdmin=="No" else True
            sql += " isAdmin = %s AND"
            values.append(isAdmin)
        if sql.endswith("AND"):
            sql = sql[:-4]
        self.cursor.execute(sql, values)
        return self.cursor.fetchall()

    def filter_librarian(self):
        Id=self.ui.searchLibrarianId.text().rstrip()
        Nom =self.ui.searchLibrarianNom.text().rstrip()
        Prenom= self.ui.searchLibrarianPrenom.text().rstrip()
        IsAdmin= self.ui.searchAdmin.currentText()

        if not Id: Id = None
        if not Nom: Nom=None
        if not Prenom: Prenom=None
        if IsAdmin == 'is Admin': IsAdmin=None
        
        self.loadLibrarians(self.search(id=Id,nom=Nom,prenom=Prenom,isAdmin=IsAdmin))
    
    def clear_filter(self):
        self.ui.searchLibrarianId.setText("")
        self.ui.searchLibrarianNom.setText("")
        self.ui.searchLibrarianPrenom.setText("")
        self.ui.searchAdmin.setCurrentText("is Admin")
        self.loadLibrarians(self.get_all_librarians())
        