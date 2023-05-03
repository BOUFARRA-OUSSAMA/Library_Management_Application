import os
from ui_interface import *
from myWidgets.Widgets  import *
from Books import Books
from Members import Member
from Emprunts import Emprunt
from Librarian import Librarian
#from Custom_Widgets.Widgets import *
# INITIALIZE APP SETTINGS
settings = QSettings()

class MainWindow(QMainWindow):
    def __init__(self,isAdmin):
        QMainWindow.__init__(self)
        self.isAdmin = int(isAdmin)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui) 
        self.show()
        QAppSettings.updateAppSettings(self)
        settings.setValue("THEME", "Dark-Theme")
        QAppSettings.updateAppSettings(self)
        
        #books
        book = Books(self.ui)
        book.displayBooks(book.get_all_books())
        self.ui.bookAdd.clicked.connect(lambda: book.add())
        self.ui.bookEdit.clicked.connect(lambda: book.edit())
        self.ui.deleteBookBtn.clicked.connect(lambda: book.delete())
        self.ui.searchBookBtn.clicked.connect(lambda: book.filter())
        self.ui.clearBookBtn.clicked.connect(lambda: book.clear_filter())
        self.ui.bookupload.clicked.connect(lambda: book.setImage())
        #members
        member=Member(self.ui)
        member.display_members(member.get_allMembers())
        self.ui.addMemberBtn.clicked.connect(lambda: member.add_member())
        self.ui.editMemberBtn.clicked.connect(lambda: member.edit_member())
        self.ui.deleteMemberBtn.clicked.connect(lambda: member.delete_member())
        self.ui.MemberApplyFilter.clicked.connect(lambda: member.filter_membres())
        self.ui.MemberClearFilter.clicked.connect(lambda: member.clear_filter())

        #emprunt
        emprunt = Emprunt(self.ui)
        emprunt.display_emprunts(emprunt.get_all_emprunts())
        emprunt.display_history(emprunt.get_all_history())
        self.ui.ajouterEmpruntBtn.clicked.connect(lambda: emprunt.borrow_book())
        self.ui.returnEmpruntBtn.clicked.connect(lambda: emprunt.return_book())
        self.ui.searchApplyBtn.clicked.connect(lambda: emprunt.filter_emprunt())
        self.ui.searchClearBtn.clicked.connect(lambda: emprunt.clear_Empfilter())
        self.ui.searchHistoryApplyBtn.clicked.connect(lambda: emprunt.filter_history())
        self.ui.searchHistoryClearBtn.clicked.connect(lambda: emprunt.clear_Historyfilter())

        #librarian
        librarian=Librarian(self.ui)
        if self.isAdmin != 1:
            self.ui.pushButton_6.hide()
        self.ui.addLibrarianBtn.clicked.connect(lambda : librarian.create_librarian())
        self.ui.editLibrarianBtn.clicked.connect(lambda : librarian.edit_Librarian())
        self.ui.deleteLibrarianBtn.clicked.connect(lambda : librarian.delete_librarian())
        self.ui.searchLibrarianBtn.clicked.connect(lambda : librarian.filter_librarian())
        self.ui.LibrarianClearBtn.clicked.connect(lambda : librarian.clear_filter())

        #logout 
        #self.ui.pushButton.clicked.connect(lambda: self.logout())
    
    def logout(self):
        from Login import Ui_login
        login_ui = Ui_login()
        login_ui.window2.show()
        # self.hide()

            
       
             


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow(1)
#     window.show()
#     app.exec_()
