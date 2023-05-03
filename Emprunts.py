import MySQLdb
from PySide2.QtWidgets import QTableWidgetItem, QMessageBox
from PySide2.QtCore import QDate
from Books import Books

class Emprunt:
    def __init__(self,ui):
        self.ui=ui
        self.db = MySQLdb.connect(host='localhost',user='root',password='',database='library')
        self.cursor = self.db.cursor()
        self.create_table()

    def create_table(self):
        try:
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS emprunts (
                                book_id INT, 
                                member_id INT,
                                date_emprunt DATE,
                                date_retour DATE,
                                FOREIGN KEY (book_id) REFERENCES books(ref),
                                FOREIGN KEY (member_id) REFERENCES members(id),
                                PRIMARY KEY (book_id,member_id,date_emprunt))''')
            self.db.commit()
        except:
            print('table not created')

    def borrow_book(self):
        book_id = self.ui.ajouterEmpruntRef.text().rstrip()
        member_id= self.ui.ajouterEmpruntId.text().rstrip()

        if book_id and member_id:
            self.cursor.execute('SELECT * FROM members WHERE id=%s',(member_id,))
            member_existes = self.cursor.fetchone()
            self.cursor.execute('SELECT * FROM books WHERE ref=%s',(book_id,))
            book_existes = self.cursor.fetchone()
            if member_existes is not None and book_existes is not None:
                self.cursor.execute("SELECT * FROM emprunts WHERE book_id=%s AND member_id=%s AND date_retour IS NULL",(book_id,member_id))
                result = self.cursor.fetchone()
                self.cursor.execute("SELECT quantity FROM books WHERE ref=%s",(book_id,))
                qte=int(self.cursor.fetchone()[0])
                if result==None and qte>0:
                    self.cursor.execute("INSERT INTO emprunts(book_id,member_id,date_emprunt) VALUES(%s,%s,CURDATE())",(book_id,member_id))
                    self.cursor.execute("UPDATE books SET quantity=quantity-1 WHERE ref=%s",(book_id,))
                    self.db.commit()
                    self.display_emprunts(self.get_all_emprunts())
                    Books.displayBooks(self,Books.get_all_books(self))
                    self.ui.ajouterEmpruntRef.setText("")
                    self.ui.ajouterEmpruntId.setText("")
                else:
                    dialog1 = QMessageBox(self.ui.centralwidget)
                    dialog1.setText("Book already borrowed by this member")
                    dialog1.setWindowTitle("Error !!")
                    dialog1.setIcon(QMessageBox.Critical)
                    dialog1.exec_()
            else:
                dialog2 = QMessageBox(self.ui.centralwidget)
                dialog2.setText("Member or book doesn't existe")
                dialog2.setWindowTitle("Error !!")
                dialog2.setIcon(QMessageBox.Critical)
                dialog2.exec_()

    def return_book(self):
        book_id=self.ui.returnEmpruntRef.text().rstrip()
        member_id=self.ui.returnEmprutnId.text().rstrip()
        empDate=self.ui.empruntDate.date().toString('yyyy-MM-dd')
        if book_id and member_id and empDate!="2000-01-01":
            
            self.cursor.execute('SELECT * FROM members WHERE id=%s',(member_id,))
            member_existes = self.cursor.fetchone()
            self.cursor.execute('SELECT * FROM books WHERE ref=%s',(book_id,))
            book_existes = self.cursor.fetchone()

            if member_existes is not None and book_existes is not None:
                self.cursor.execute('''SELECT * FROM emprunts 
                                    WHERE book_id=%s AND member_id=%s AND date_emprunt=%s  AND date_retour IS NULL''',(book_id,member_id,empDate))
                result = self.cursor.fetchone()
                if result !=None:
                    self.cursor.execute('''UPDATE emprunts SET date_retour=CURDATE() 
                                        WHERE book_id=%s AND member_id=%s AND date_emprunt=%s''',(book_id,member_id,empDate))
                    self.cursor.execute("UPDATE books SET quantity=quantity+1 WHERE ref=%s",(book_id,))
                    self.db.commit()
                    Books.displayBooks(self,Books.get_all_books(self))
                    self.display_history(self.get_all_history())
                    self.display_emprunts(self.get_all_emprunts())
                    self.ui.returnEmpruntRef.setText("")
                    self.ui.returnEmprutnId.setText("")
                    date = QDate(2000,1,1)
                    self.ui.empruntDate.setDate(date)
            else:
                dialog = QMessageBox(self.ui.centralwidget)
                dialog.setText("Member or book doesn't existe")
                dialog.setWindowTitle("Error !!")
                dialog.setIcon(QMessageBox.Critical)
                dialog.exec_()


    def get_all_emprunts(self):
        self.cursor.execute('''SELECT members.id,members.nom,members.prenom,books.ref,books.title,emprunts.date_emprunt
                               FROM emprunts
                               JOIN members ON emprunts.member_id=members.id
                               JOIN books ON books.ref=emprunts.book_id
                               WHERE emprunts.date_retour IS NULL''')
        return self.cursor.fetchall()

    def get_all_history(self):
        self.cursor.execute('''SELECT members.id,members.nom,members.prenom,books.ref,books.title,emprunts.date_emprunt,emprunts.date_retour
                               FROM emprunts
                               JOIN members ON emprunts.member_id=members.id
                               JOIN books ON books.ref=emprunts.book_id
                               WHERE emprunts.date_retour IS NOT NULL''')
        return self.cursor.fetchall()

    def display_history(self,rows):
        self.ui.tableWidget_4.clearContents()
        self.ui.tableWidget_4.setRowCount(0)
        for row_number, row_data in enumerate(rows):
            self.ui.tableWidget_4.insertRow(row_number)
            for column_number, column_data in enumerate(row_data):
                item = str(column_data)
                qtablewidgetitem = QTableWidgetItem()
                self.ui.tableWidget_4.setItem(row_number, column_number, qtablewidgetitem)
                qtablewidgetitem.setText(str(item))

    def search(self,id=None, nom=None, prenom=None, ref=None, title=None, empDate=None,returnDate=None,history=False):
        if not history:    
            sql ='''SELECT members.id,members.nom,members.prenom,books.ref,books.title,emprunts.date_emprunt
                                FROM emprunts
                                JOIN members ON emprunts.member_id=members.id
                                JOIN books ON books.ref=emprunts.book_id
                                WHERE emprunts.date_retour IS NULL AND '''
        else:
            sql ='''SELECT members.id,members.nom,members.prenom,books.ref,books.title,emprunts.date_emprunt,emprunts.date_retour
                                FROM emprunts
                                JOIN members ON emprunts.member_id=members.id
                                JOIN books ON books.ref=emprunts.book_id
                                WHERE emprunts.date_retour IS NOT NULL AND '''
        values = []
        if id is not None:
            sql += " emprunts.member_id = %s AND"
            values.append(id)
        if nom is not None:
            sql += " members.nom = %s AND"
            values.append(nom)
        if prenom is not None:
            sql += " members.prenom = %s AND"
            values.append(prenom)
        if ref is not None:
            sql += " emprunts.book_id = %s AND"
            values.append(ref)
        if title is not None:
            sql += " books.title = %s AND"
            values.append(title)
        if empDate is not None:
            sql+= " emprunts.date_emprunt = %s AND"
            values.append(empDate)
        if returnDate is not None and history:
            sql+= " emprunts.date_retour = %s AND"
            values.append(returnDate)
        if sql.endswith("AND"):
            sql = sql[:-4]
        self.cursor.execute(sql, values)
        return self.cursor.fetchall()
    
    def filter_history(self):
        f_id=self.ui.searchHistoryId.text().rstrip()
        f_nom =self.ui.searchHistoryNom.text().rstrip()
        f_prenom = self.ui.searchHistoryPrenom.text().rstrip()
        f_ref =self.ui.searchHistoryRef.text().rstrip()
        f_title =self.ui.searchHistoryTitle.text().rstrip()
        f_empDate =self.ui.searchHistoryEmp.date().toString('yyyy-MM-dd')
        f_returnDate =self.ui.searchHistoryRetour.date().toString('yyyy-MM-dd')

        if not f_id: f_id = None
        if not f_nom: f_nom=None
        if not f_prenom: f_prenom=None
        if not f_ref: f_ref=None
        if not f_title: f_title=None
        if f_empDate=='2000-01-01': f_empDate=None
        if f_returnDate=='2000-01-01': f_returnDate=None

        self.display_history(self.search(id=f_id,nom=f_nom,prenom=f_prenom,ref=f_ref,title=f_title,empDate=f_empDate,returnDate=f_returnDate,history=True))

    def clear_Historyfilter(self):
        self.display_history(self.get_all_history())

        self.ui.searchHistoryId.setText("")
        self.ui.searchHistoryNom.setText("")
        self.ui.searchHistoryPrenom.setText("")
        self.ui.searchHistoryRef.setText("")
        self.ui.searchHistoryTitle.setText("")
        self.ui.searchHistoryEmp.setDate(QDate(2000,1,1))
        self.ui.searchHistoryRetour.setDate(QDate(2000,1,1))

    def filter_emprunt(self):
        f_id=self.ui.searchEmpruntId.text().rstrip()
        f_nom =self.ui.searchEmpruntNom.text().rstrip()
        f_prenom = self.ui.searchEmpruntPrenom.text().rstrip()
        f_ref =self.ui.searchEmpruntRef.text().rstrip()
        f_title =self.ui.searchEmpruntTitle.text().rstrip()
        f_date =self.ui.searchEmpruntDate.date().toString('yyyy-MM-dd')

        if not f_id: f_id = None
        if not f_nom: f_nom=None
        if not f_prenom: f_prenom=None
        if not f_ref: f_ref=None
        if not f_title: f_title=None
        if f_date=='2000-01-01': f_date=None

        self.display_emprunts(self.search(id=f_id,nom=f_nom,prenom=f_prenom,ref=f_ref,title=f_title,empDate=f_date))
    
    def clear_Empfilter(self):
        self.display_emprunts(self.get_all_emprunts())

        self.ui.searchEmpruntId.setText("")
        self.ui.searchEmpruntNom.setText("")
        self.ui.searchEmpruntPrenom.setText("")
        self.ui.searchEmpruntRef.setText("")
        self.ui.searchEmpruntTitle.setText("")
        date = QDate(2000,1,1)
        self.ui.searchEmpruntDate.setDate(date)

    def display_emprunts(self,rows):
        self.ui.tableWidget.clearContents()
        self.ui.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(rows):
            self.ui.tableWidget.insertRow(row_number)
            for column_number, column_data in enumerate(row_data):
                item = str(column_data)
                qtablewidgetitem = QTableWidgetItem()
                self.ui.tableWidget.setItem(row_number, column_number, qtablewidgetitem)
                qtablewidgetitem.setText(str(item))
