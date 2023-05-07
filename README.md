# PyMySQL-Library-App
Implementation of a Library Database Management Application implemented using Python Tkinter, MySQL and PyMySQL Library to interact with the MySQL Database using a simplified frontend user interface.

## Logical Schema
Member (*Membership ID*(PK), Name, Faculty, Phone Number, Email Address, Outstanding Fines)   

Book (*Accession Number*(PK) Title, Authors, ISBN, Publisher, Publication Year)    

Loan (***Accession Number**(FK), Borrow Date*(PK), Due Date, Membership ID, Return Date)   

Fine Payment (***Membership ID**(FK), Payment Date*(PK), Amount)   

Reservation (**Accession Number(FK), Membership ID(FK)**,( Reserve Date)   

Legend:   
Italics - Personal Key(PK)   
Bolded- Foreign Keys(FK)   

## Logical Data Model

| Tables       | Keys |
| ------------ |  ------------|
| Member (membershipID, name, faculty, email address, outstandingFines) | **Primary Key** membershipID      | 
| Loan (accessionNumber, borrowDate, dueDate, membershipID, returnDate) |**Primary Key** accessionNumber, borrowDate **Foreign Key** accessionNumber references Book(accessionNumber)Foreign Key membershipID references Member (membershipID)  |
| Fines (membershipID, paymentDate, paidAmount) | **Primary Key** membershipID, paymentDate **Foreign Key** membershipID references Member (membershipID) |
| Book (accessionNumber, title, authors, isbn, publisher,publicationYear) | **Primary Key** accessionNumber |
| Reservation (accessionNumber, reserveDate, membershipID) | **Primary Key** accessionNumber, membershipID **Foreign key** accessionNumber references Book (accessionNumber) **Foreign key** membershipID references Member (membershipID)
