import MySQLdb
from PySide2.QtCore import QDate
from PyQt5.QtWidgets import QFileDialog
from PySide2.QtWidgets import QTableWidgetItem,QMessageBox
from PySide2.QtGui import QPixmap, QIcon
import datetime
import os
import shutil

class Books:
    def __init__(self,ui):
        self.ui=ui
        self.image=''
        self.db = MySQLdb.connect(host='localhost',user='root',password='',database='library')
        self.cursor = self.db.cursor()
        self.create_table()
        
    def create_table(self):
        try:
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                                ref INT AUTO_INCREMENT PRIMARY KEY, 
                                title VARCHAR(255),
                                author VARCHAR(255),
                                year DATE,
                                edition VARCHAR(255),
                                quantity int,
                                imagePath VARCHAR(255))''')
        except:
            print('table not created')

    def add(self):
        title =self.ui.bookTitle.text().rstrip()
        author= self.ui.bookAuthor.text().rstrip()
        year=self.ui.bookYear.date().toString('yyyy-MM-dd')
        edition=self.ui.Edition.text().rstrip()
        qte=self.ui.bookqte.text()
        path='.\\assets'
        image_Path=''
        if title and author and year and edition and qte:
            if self.image != '':
                full_imageName=self.image.split('/')[-1]
                image_name=full_imageName.split('.')[0]
                ext=full_imageName.split('.')[1]
                now = datetime.datetime.now()
                date_time = now.strftime("%Y-%m-%d-%H-%M-%S")
                new_image_name=image_name+date_time+'.'+ext
                image_Path=os.path.join(path, new_image_name)
                shutil.copy(self.image, image_Path)

            sql = "INSERT INTO books (title, author, year,edition, quantity, imagePath) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (title, author, year, edition, qte, image_Path)
            self.cursor.execute(sql, values)
            self.db.commit()
            self.ui.bookupload.setText("Upload image")
            self.ui.bookTitle.setText("")
            self.ui.bookAuthor.setText("")
            date = QDate(2000,1,1)
            self.ui.bookYear.setDate(date)
            self.ui.Edition.setText("")
            self.ui.bookqte.setText("")

            Books.displayBooks(self,Books.get_all_books(self))
        else:
            dialog = QMessageBox(self.ui.centralwidget)
            dialog.setText("les champs ne doivent pas etre vide")
            dialog.setWindowTitle("Error !!")
            dialog.setIcon(QMessageBox.Critical)
            dialog.exec_()

    def delete(self):
        ref = self.ui.deleteRef.text().strip()
        if ref:
            self.cursor.execute("SELECT * FROM books WHERE ref=%s",(ref,))
            result = self.cursor.fetchone()
            if result is not None:
                dialog = QMessageBox(self.ui.centralwidget)
                dialog.setText("voulez vous vraiment supprimer ce membre")
                dialog.setWindowTitle("")
                dialog.setIcon(QMessageBox.Question)
                dialog.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
                result = dialog.exec_()
                if result==QMessageBox.Ok:
                    self.cursor.execute("DELETE FROM books WHERE ref = %s", (ref,))
                    self.db.commit()
                    self.displayBooks(self.get_all_books())
            else:
                dialog1 = QMessageBox(self.ui.centralwidget)
                dialog1.setText("livre n'existe pas")
                dialog1.setWindowTitle("Error !!")
                dialog1.setIcon(QMessageBox.Critical)
                dialog1.exec_()
        else:
            dialog2 = QMessageBox(self.ui.centralwidget)
            dialog2.setText("le champ ref ne doit pas etre vide")
            dialog2.setWindowTitle("Error !!")
            dialog2.setIcon(QMessageBox.Critical)
            dialog2.exec_()

    def update(self, id, title=None, author=None, edition=None, year=None, qte=None):
        sql = "UPDATE books SET"
        values = []
        if title is not None:
            sql += " title = %s,"
            values.append(title)
        if author is not None:
            sql += " author = %s,"
            values.append(author)
        if edition is not None:
            sql += " edition = %s,"
            values.append(edition)
        if year is not None:
            sql += " year = %s,"
            values.append(year)
        if qte is not None:
            sql += " quantity = %s,"
            values.append(qte)
        sql = sql[:-1] + " WHERE ref = %s"
        values.append(id)
        self.cursor.execute(sql, values)
        self.db.commit()
    
    def edit(self):
        e_ref=self.ui.editRef.text().rstrip()
        e_title =self.ui.editTitle.text().rstrip()
        e_author= self.ui.editAuthor.text().rstrip()
        e_year=self.ui.editYear.date().toString('yyyy-MM-dd')
        e_edition=self.ui.editEdition.text().rstrip()
        e_qte=self.ui.editQte.text().rstrip()
        if e_ref:
            self.cursor.execute("SELECT * FROM books WHERE ref=%s",(e_ref,))
            result = self.cursor.fetchone()
            if result is not None:
                if not e_title: e_title=None
                if not e_author: e_author=None
                if not e_year: e_year=None
                if not e_edition: e_edition=None
                if not e_qte: e_publisher=None
                if e_year=='2000-01-01': e_year=None

                self.update(e_ref,title=e_title,author=e_author,year=e_year,edition=e_edition,qte=e_qte)

                self.ui.editRef.setText("")
                self.ui.editTitle.setText("")
                self.ui.editAuthor.setText("")
                date = QDate(2000,1,1)
                self.ui.editYear.setDate(date)
                self.ui.editEdition.setText("")
                self.ui.editQte.setText("")
                
                Books.displayBooks(self,Books.get_all_books(self))
            else:
                dialog1 = QMessageBox(self.ui.centralwidget)
                dialog1.setText("livre n'existe pas")
                dialog1.setWindowTitle("Error !!")
                dialog1.setIcon(QMessageBox.Critical)
                dialog1.exec_()
        else:
            dialog2 = QMessageBox(self.ui.centralwidget)
            dialog2.setText("le champ ref ne doit pas etre vide")
            dialog2.setWindowTitle("Error !!")
            dialog2.setIcon(QMessageBox.Critical)
            dialog2.exec_()


    def search(self,ref=None, title=None, author=None, year=None,edition=None):
        sql = "SELECT imagePath,ref,title,author,year,edition,quantity FROM books WHERE"
        values = []
        if ref is not None:
            sql += " ref = %s AND"
            values.append(ref)
        if title is not None:
            sql += " title = %s AND"
            values.append(title)
        if author is not None:
            sql += " author = %s AND"
            values.append(author)
        if year is not None:
            sql += " year = %s AND"
            values.append(year)
        if edition is not None:
            sql += " edition = %s AND"
            values.append(edition)
        if sql.endswith("AND"):
            sql = sql[:-4]
        self.cursor.execute(sql, values)
        return self.cursor.fetchall()

    def filter(self):
        e_ref=self.ui.searchRef.text().strip()
        e_title =self.ui.searchTitle.text().strip()
        e_author= self.ui.searchAuthor.text().strip()
        e_year=self.ui.searchYear.date().toString('yyyy-MM-dd')
        e_edition=self.ui.searchEdition.text().strip()

        if not e_ref: e_ref = None
        if not e_title: e_title=None
        if not e_author: e_author=None
        if not e_year: e_year=None
        if not e_edition: e_edition=None
        if e_year=='2000-01-01': e_year=None

        self.displayBooks(self.search(ref=e_ref,title=e_title,author=e_author,year=e_year,edition=e_edition))
    
    def clear_filter(self):
        self.displayBooks(self.get_all_books())
        self.ui.searchRef.setText("")
        self.ui.searchTitle.setText("")
        self.ui.searchAuthor.setText("")
        date = QDate(2000,1,1)
        self.ui.searchYear.setDate(date)
        self.ui.searchEdition.setText("")

    def get_all_books(self):
        self.cursor.execute("SELECT imagePath,ref,title,author,year,edition,quantity FROM books")
        return self.cursor.fetchall()

    def setImage(self):
        file = QFileDialog.getOpenFileName(caption='open file',directory='C:',filter='images ( *.png *.jpeg *.jpg)')
        filename=file[0].split('/')
        if filename=="":
            self.ui.bookupload.setText("Upload image")
        else:    
            self.ui.bookupload.setText(filename[-1])
            self.image = file[0]
    
    def close(self):
        self.cursor.close()
        self.db.close()
    
    def displayBooks(self, rows):
         # Create new row
        self.ui.tableWidget_2.clearContents()
        self.ui.tableWidget_2.setRowCount(0)
        for row_number, row_data in enumerate(rows):
            self.ui.tableWidget_2.insertRow(row_number)
            for column_number, column_data in enumerate(row_data):
                item = str(column_data)
                if column_number == 0:
                    pixmap=QPixmap(item)
                    icon = QIcon(pixmap)
                    TableItem = QTableWidgetItem()
                    TableItem.setIcon(icon)
                    self.ui.tableWidget_2.setItem(row_number, column_number,TableItem)
                else:
                    qtablewidgetitem = QTableWidgetItem()
                    self.ui.tableWidget_2.setItem(row_number, column_number, qtablewidgetitem)
                    qtablewidgetitem.setText(str(item))
        self.ui.tableWidget_2.verticalHeader().setDefaultSectionSize(80)
            # # Get number of rows
            # rowPosition = self.ui.tableWidget_2.rowCount()

            # # Skip rows that have already been loaded to table
            # itemCount = 0
            # # Create new table row
            # self.ui.tableWidget_2.setRowCount(rowPosition+1)
            # qtablewidgetitem = QTableWidgetItem()
            # self.ui.tableWidget_2.setVerticalHeaderItem(rowPosition, qtablewidgetitem)

            # # Add items to row

            # for item in row:
            #     self.qtablewidgetitem = QTableWidgetItem()
            #     self.ui.tableWidget_2.setItem(rowPosition, itemCount, self.qtablewidgetitem)
            #     self.qtablewidgetitem = self.ui.tableWidget_2.item(rowPosition, itemCount)
            #     self.qtablewidgetitem.setText(str(item))

            #     itemCount = itemCount+1

            # rowPosition = rowPosition+1

