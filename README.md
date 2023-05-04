# Library_Management_Application

📚 This is a desktop application built using Python and PyQt5 framework that helps manage a library's books, librarians, and clients. The app has graphical user interfaces (GUIs) for different functionalities:

1. Borrowing/Returning Books: Users can borrow or return books by entering their ID, name, reference, title, and date.
2. Book Management: Librarians can add, delete, and update books with all relevant information.
3. Librarian Management: Admins can add, delete, and update librarians and view all users in the database.
4. History: A record of all transactions of borrowing and returning books with the name of the librarian who performed the action.
5. Client Management: Admins can add, delete, and update clients and view all their information, including the name of the books they took.

## Getting Started

👉 When the app starts, use the following credentials to log in:
- Username: admin
- Password: admin

🚀 To get started, follow these steps:
1. Create a MySQL database named "library" in your preferred MySQL database management system.
```SQL
CREATE DATABASE library ;
```
2. Clone the repository to your local machine.
3. Install the required dependencies using pip:
```bash
pip install -r requirements.txt
```
4. Run the app by executing the `Login.py` file:
```bash
python3 Login.py
```
5. Log in using the provided credentials and start managing your library!

## Screenshots

📸 Here are some screenshots of the app:

## Members GUI
The Members GUI allows you to manage members of your library. There are four buttons available also display list of all the members in the database:

<img width="600" src= https://user-images.githubusercontent.com/118765563/236272933-91a6cc7d-5126-4509-8fbc-8c9ab27e06f3.PNG>


###### Add Member:
  Clicking this button opens a side panel where you can enter the name, address, and phone number of the member you want to add.


###### Modify Member:
  Clicking this button opens a side panel where you can enter the ID of the member whose information you want to modify.
  

###### Delete Member: 
  Clicking this button opens a side panel where you can enter the ID of the member you want to delete and before the suppression a prompt will ask you if you are sure you want to delete the memeber 

###### Search Member:
  Clicking this button opens a side panel where you can enter the ID, name, address, or phone number of the member you are looking for. It will display a list of members that match your search criteria.

The Members GUI is easy to use and allows you to manage your library's members with ease!

## here also we can see the gui for libriarians :

<img width="600" src=https://user-images.githubusercontent.com/118765563/236304816-d779055a-173d-4f64-8167-bdd76deb3d03.PNG >

The Librarians GUI allows you to manage the librarians who work at your library.

###### Add Librarian: 
  Clicking this button opens a side panel where you can enter the name, login name, password (and confirmation), and specify whether the new user is an admin or not.
###### Modify Librarian:
  Clicking this button opens a side panel where you can enter the ID of the librarian whose information you want to modify. You can change the name, password, and admin authority.
###### Delete Librarian: 
  Clicking this button opens a side panel with a text eara for the id of the user that we wish to delete then a prompt window asks you to confirm that you want to delete the librarian.
###### Search Librarian:
  Clicking this button opens a side panel where you can enter the ID or name of the librarian you are looking for.
  
## Acknowledgments

🙏 Special thanks to my teacher for inspiring us to build this app and for providing guidance and support throughout the development process. This project was a collaboration between me and [AdilBendaoud](https://github.com/AdilBendaoud)

## Contact

📧 If you have any questions or feedback, feel free to reach out to me at [oussama.boufarra@emsi-edu.ma](mailto:oussama.boufarra@emsi-edu.ma).



