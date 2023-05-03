import MySQLdb
from PySide2.QtWidgets import QTableWidgetItem,QMessageBox

class Member:
    def __init__(self,ui):
        self.ui=ui
        self.db = MySQLdb.connect(host='localhost',user='root',password='',database='library')
        self.cursor = self.db.cursor()
        self.create_table()
    
    def create_table(self):
        try:
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS members (
                                id INT AUTO_INCREMENT PRIMARY KEY, 
                                nom VARCHAR(50),
                                prenom VARCHAR(50),
                                adresse VARCHAR(50),
                                tel VARCHAR(50),
                                date_inscription DATE)''')
            self.db.commit()
        except:
            print('table not created')

    def add_member(self):
        nom=self.ui.addMemberNom.text().rstrip()
        prenom=self.ui.addMemberPrenom.text().rstrip()
        adresse=self.ui.addMemberAdresse.text().rstrip()
        tel=self.ui.addMemberTel.text().rstrip()
        if nom and prenom:
            sql = "INSERT INTO members (nom, prenom, adresse,tel,date_inscription) VALUES (%s, %s, %s, %s,CURDATE())"
            val = (nom, prenom, adresse, tel)
            self.cursor.execute(sql, val)
            self.db.commit()
            
            self.ui.addMemberNom.setText("")
            self.ui.addMemberPrenom.setText("")
            self.ui.addMemberAdresse.setText("")
            self.ui.addMemberTel.setText("")

            self.display_members(self.get_allMembers())
        else:
            dialog = QMessageBox(self.ui.centralwidget)
            dialog.setText("Nom ou Prenom est vide")
            dialog.setWindowTitle("Error !!")
            dialog.setIcon(QMessageBox.Critical)
            dialog.exec_()

    def update(self, id, nom=None, prenom=None, adresse=None, tel=None):
        if id:
            sql = "UPDATE members SET"
            values = []
            if nom is not None:
                sql += " nom = %s,"
                values.append(nom)
            if prenom is not None:
                sql += " prenom = %s,"
                values.append(prenom)
            if adresse is not None:
                sql += " adresse = %s,"
                values.append(adresse)
            if tel is not None:
                sql += " tel = %s,"
                values.append(tel)

            sql = sql[:-1] + " WHERE id = %s"
            values.append(id)
            self.cursor.execute(sql, values)
            self.db.commit()
        else:
            dialog = QMessageBox(self.ui.centralwidget)
            dialog.setText("id ne doit pas etre vide")
            dialog.setWindowTitle("Error !!")
            dialog.setIcon(QMessageBox.Critical)
            dialog.exec_()
    
    def edit_member(self):
        e_id=self.ui.editMemberid.text().rstrip()
        e_nom =self.ui.editMemberNom.text().rstrip()
        e_prenom= self.ui.editMemberPrenom.text().rstrip()
        e_adresse= self.ui.editMemberAdresse.text().rstrip()
        e_tel=self.ui.editMemberTel.text().rstrip()

        if e_id:
            if not e_nom: e_nom=None
            if not e_prenom: e_prenom=None
            if not e_adresse: e_adresse=None
            if not e_tel: e_tel=None

            self.update(e_id,nom=e_nom,prenom=e_prenom,adresse=e_adresse,tel=e_tel)

            self.ui.editMemberid.setText("")
            self.ui.editMemberNom.setText("")
            self.ui.editMemberPrenom.setText("")
            self.ui.editMemberAdresse.setText("")
            self.ui.editMemberTel.setText("")
            
            self.display_members(self.get_allMembers())

    def delete_member(self):
        id=self.ui.deleteMemberid.text().rstrip()
        if id:
            self.cursor.execute("SELECT * FROM members WHERE id =%s",(id,))
            res = self.cursor.fetchone()
            if res is not None:
                dialog = QMessageBox(self.ui.centralwidget)
                dialog.setText("voulez vous vraiment supprimer ce membre")
                dialog.setIcon(QMessageBox.Question)
                dialog.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
                dialog.setWindowTitle("")
                result = dialog.exec_()
                if result==QMessageBox.Ok:
                    self.cursor.execute("DELETE FROM members WHERE id=%s", (id,))
                    self.db.commit()
                    self.display_members(self.get_allMembers())
                    self.ui.deleteMemberid.setText("")
            else:
                dialog1 = QMessageBox(self.ui.centralwidget)
                dialog1.setText("membre n'existe pas")
                dialog1.setWindowTitle("Error !!")
                dialog1.setIcon(QMessageBox.Critical)
                dialog1.exec_()
        else:
            dialog2 = QMessageBox(self.ui.centralwidget)
            dialog2.setText("le champ id ne doit pas etre vide")
            dialog2.setWindowTitle("Error !!")
            dialog2.setIcon(QMessageBox.Critical)
            dialog2.exec_()

    def search(self,id=None, nom=None, prenom=None, adresse=None, tel=None):
        sql = "SELECT * FROM members WHERE"
        values = []
        if id is not None:
            sql += " id = %s AND"
            values.append(id)
        if nom is not None:
            sql += " nom = %s AND"
            values.append(nom)
        if prenom is not None:
            sql += " prenom = %s AND"
            values.append(prenom)
        if adresse is not None:
            sql += " adresse = %s AND"
            values.append(adresse)
        if tel is not None:
            sql += " tel = %s AND"
            values.append(tel)
        if sql.endswith("AND"):
            sql = sql[:-4]
        self.cursor.execute(sql, values)
        return self.cursor.fetchall()

    def filter_membres(self):
        f_id=self.ui.searchMemberid.text().rstrip()
        f_nom =self.ui.searchMemberNom.text().rstrip()
        f_prenom= self.ui.searchMemberPrenom.text().rstrip()
        f_adresse=self.ui.searchMemberAdresse.text().rstrip()
        f_tel=self.ui.searchEdition.text().rstrip()

        if not f_id: f_id = None
        if not f_nom: f_nom=None
        if not f_prenom: f_prenom=None
        if not f_adresse: f_adresse=None
        if not f_tel: f_tel=None

        self.display_members(self.search(id=f_id,nom=f_nom,prenom=f_prenom,adresse=f_adresse,tel=f_tel))
    
    def clear_filter(self):
        self.display_members(self.get_allMembers())
        self.ui.searchMemberid.setText("")
        self.ui.searchMemberNom.setText("")
        self.ui.searchMemberPrenom.setText("")
        self.ui.searchMemberAdresse.setText("")
        self.ui.searchEdition.setText("")

    def get_allMembers(self):
        self.cursor.execute("SELECT * FROM members")
        return self.cursor.fetchall()

    def display_members(self,rows):
        self.ui.tableWidget_3.clearContents()
        self.ui.tableWidget_3.setRowCount(0)
        for row_number, row_data in enumerate(rows):
            self.ui.tableWidget_3.insertRow(row_number)
            for column_number, column_data in enumerate(row_data):
                item = str(column_data)
                qtablewidgetitem = QTableWidgetItem()
                self.ui.tableWidget_3.setItem(row_number, column_number, qtablewidgetitem)
                qtablewidgetitem.setText(str(item))
