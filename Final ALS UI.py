from tkinter import *
import tkinter as tk
from tkinter import font
from functools import partial
from doctest import master
from itertools import count
from pickle import TRUE
from textwrap import fill
from tkinter import BOTH, BOTTOM, CENTER, RIGHT, Y, font
from tkinter import ttk
from turtle import width
from tkcalendar import DateEntry
from PIL import ImageTk,Image
#from BT2102 import *


import pymysql.cursors
import datetime

connection = pymysql.connect(host = "localhost",
                             user="root",
                             password='amir159874',  #CHANGE PASSWORD                           
                             db='library',
                             cursorclass=pymysql.cursors.DictCursor) 


def show_frame(frame):
    frame.tkraise()

window = tk.Tk()
window.state("zoomed")
window.columnconfigure(0,weight = 1)
window.rowconfigure(0,weight = 1)

#FONTS
titleFont = font.Font(family='Helvetica', name='titleFont', size=25)
buttonFont = font.Font(family='Helvetica', name='btnFont', size=18)
entryFont = font.Font(family='Helvetica', name='entryFont', size=18)
alertFont = font.Font(family='Helvetica', name='alertFont', size=22)
messageFont = font.Font(family='Helvetica', name='messageFont', size=18)

#FOR DEBUGGING
def hello():
    top = tk.Toplevel(window)
    top.geometry("300x300")
    top.title("child window")
    lbl = tk.Label(top, text = "popup window")
    lbl.pack()
    btn = tk.Button(top, text = "okay", command = top.destroy)
    btn.pack()
#===========================ALL PAGES========================#
#start_page
start_page = tk.Frame(window, bg="light coral")
start_page.grid(row=0,column=0,sticky="nsew")
#my_bg = tk.Label(start_page, image = app_bg)
#my_bg.place(x=0, y=0, relwidth=1, relheight=1)
#membership_page
membership_page = tk.Frame(window, bg="light coral")
membership_page.grid(row=0,column=0,sticky="nsew")
#books_page
books_page = tk.Frame(window, bg="light coral")
books_page.grid(row=0,column=0,sticky="nsew")
#loans_page
loans_page = tk.Frame(window, bg="light coral")
loans_page.grid(row=0,column=0,sticky="nsew")
#reservations_page
reservations_page = tk.Frame(window, bg="light coral")
reservations_page.grid(row=0,column=0,sticky="nsew")
#fines_page
fines_page = tk.Frame(window, bg="light coral")
fines_page.grid(row=0,column=0,sticky="nsew")
#report_page
report_page = tk.Frame(window, bg="light coral")
report_page.grid(row=0,column=0,sticky="nsew")

##MEMBERSHIPS
#membercreation_page
membercreation_page = tk.Frame(window, bg="light coral")
membercreation_page.grid(row=0,column=0,sticky="nsew")
#memberdeletion_page
memberdeletion_page = tk.Frame(window, bg="light coral")
memberdeletion_page.grid(row=0,column=0,sticky="nsew")
#memberupdate_page
memberupdate_page = tk.Frame(window, bg="light coral")
memberupdate_page.grid(row=0,column=0,sticky="nsew")

##BOOKS
#addbook_page
addbook_page = tk.Frame(window, bg="light coral")
addbook_page.grid(row=0,column=0,sticky="nsew")
#deletebook_page
deletebook_page = tk.Frame(window, bg="light coral")
deletebook_page.grid(row=0,column=0,sticky="nsew")

##LOANS
#borrowbook_page
borrowbook_page = tk.Frame(window, bg="light coral")
borrowbook_page.grid(row=0,column=0,sticky="nsew")
#returnbook_page
returnbook_page = tk.Frame(window, bg="light coral")
returnbook_page.grid(row=0,column=0,sticky="nsew")

##RESERVATIONS
#makereservation_page
makereservation_page = tk.Frame(window, bg="light coral")
makereservation_page.grid(row=0,column=0,sticky="nsew")
#cancelreservation_page
cancelreservation_page = tk.Frame(window, bg="light coral")
cancelreservation_page.grid(row=0,column=0,sticky="nsew")

##FINES
#finepayment_page
finepayment_page = tk.Frame(window, bg="light coral")
finepayment_page.grid(row=0,column=0,sticky="nsew")

##REPORT
#booksearch_page
booksearch_page = tk.Frame(window, bg="light coral")
booksearch_page.grid(row=0,column=0,sticky="nsew")
booksearch_results_page = tk.Frame(window,bg="light coral")
booksearch_results_page.grid(row=0,column=0,sticky="nsew")
#onloans_page
onloans_page = tk.Frame(window, bg="light coral")
onloans_page.grid(row=0,column=0,sticky="nsew")
#onreservation_page
onreservation_page = tk.Frame(window, bg="light coral")
onreservation_page.grid(row=0,column=0,sticky="nsew")
#oustandingfines_page
oustandingfines_page = tk.Frame(window, bg="light coral")
oustandingfines_page.grid(row=0,column=0,sticky="nsew")
#onloanbymember_page
onloanbymember_page = tk.Frame(window, bg="light coral")
onloanbymember_page.grid(row=0,column=0,sticky="nsew")
onloanbymember_results_page = tk.Frame(window,bg="light coral")
onloanbymember_results_page.grid(row=0,column=0,sticky="nsew")
#===========================START PAGE=======================#
#text Main Menu
#button membership
#button books
#button loans
#button reservations
#button fines
#button report

#Page Title
start_page_text = tk.Label(master = start_page, text = "Main Menu", font = titleFont, bg= "light coral")
start_page_text.grid(row=0,column=0,columnspan=3)

#All button images
books_img = ImageTk.PhotoImage(Image.open("C:/NUS/Y1S2/BT2102/Assignment 1/GRP_47_AS1/Images/booksnew.png"))
reservations_img = ImageTk.PhotoImage(Image.open("C:/NUS/Y1S2/BT2102/Assignment 1/GRP_47_AS1/Images/reservationsnew.png"))
reports_img = ImageTk.PhotoImage(Image.open("C:/NUS/Y1S2/BT2102/Assignment 1/GRP_47_AS1/Images/reportsnew.png"))
membership_img = ImageTk.PhotoImage(Image.open("C:/NUS/Y1S2/BT2102/Assignment 1/GRP_47_AS1/Images/membershipnew.png"))
fines_img = ImageTk.PhotoImage(Image.open("C:/NUS/Y1S2/BT2102/Assignment 1/GRP_47_AS1/Images/finesnew.png"))
loans_img = ImageTk.PhotoImage(Image.open("C:/NUS/Y1S2/BT2102/Assignment 1/GRP_47_AS1/Images/loansnew.png"))

#All sidebars
books_sbar = ImageTk.PhotoImage(Image.open("C:/NUS/Y1S2/BT2102/Assignment 1/GRP_47_AS1/Images/booksidebar.png"))
reservations_sbar = ImageTk.PhotoImage(Image.open("C:/NUS/Y1S2/BT2102/Assignment 1/GRP_47_AS1/Images/reservationsidebar.png"))
reports_sbar = ImageTk.PhotoImage(Image.open("C:/NUS/Y1S2/BT2102/Assignment 1/GRP_47_AS1/Images/reportsidebar.png"))
membership_sbar = ImageTk.PhotoImage(Image.open("C:/NUS/Y1S2/BT2102/Assignment 1/GRP_47_AS1/Images/membershipsidebar.png"))
fines_sbar = ImageTk.PhotoImage(Image.open("C:/NUS/Y1S2/BT2102/Assignment 1/GRP_47_AS1/Images/finesidebar.png"))
loans_sbar = ImageTk.PhotoImage(Image.open("C:/NUS/Y1S2/BT2102/Assignment 1/GRP_47_AS1/Images/loansidebar.png"))


#button membership
membership_button = tk.Button(master = start_page,
                              text = "Membership",
                              font = buttonFont,
                              image = membership_img,
                              compound = "top",
                              bg = "aquamarine",
                              command = lambda:show_frame(membership_page))
membership_button.grid(row=1, column=0, sticky = "ew", padx = 7)

#button books
books_button = tk.Button(master = start_page,
                         text = "Books",
                         font = buttonFont,
                         image = books_img,
                         compound = "top",
                         bg = "aquamarine",
                         command = lambda:show_frame(books_page))
books_button.grid(row=1, column=1, sticky = "ew", padx = 7)

#button loans
loans_button = tk.Button(master=start_page,
                         text = "Loans",
                         font = buttonFont,
                         image = loans_img,
                         compound = "top",
                         bg = "aquamarine",
                         command = lambda:show_frame(loans_page))
loans_button.grid(row=1, column=2, sticky = "ew", padx = 7)

#button reservations
reservations_button = tk.Button(master=start_page,
                                text = "Reservations",
                                font = buttonFont,
                                image = reservations_img,
                                compound = "top",
                                bg = "aquamarine",
                                command = lambda:show_frame(reservations_page))
reservations_button.grid(row=2, column=0, sticky = "ew", padx = 7)

#button fines
fines_button  = tk.Button(master=start_page,
                          text = "Fines",
                          font = buttonFont,
                          image = fines_img,
                          compound = "top",
                          bg = "aquamarine",
                          command = lambda:show_frame(fines_page))
fines_button.grid(row=2, column=1, sticky = "ew", padx = 7)

#button report
report_button = tk.Button(master=start_page,
                          text = "Report",
                          font = buttonFont,
                          image = reports_img,
                          compound = "top",
                          bg = "aquamarine",
                          command = lambda:show_frame(report_page))
report_button.grid(row=2, column=2, sticky = "ew", padx = 7)

start_page.rowconfigure(1, weight = 1)
start_page.columnconfigure(0, weight = 1)
start_page.columnconfigure(1, weight = 1)
start_page.columnconfigure(2, weight = 1)
#===========================MEMBERSHIP PAGE======================#
#button createmember
#button deletemember
#button updatemember
#button go back main menu

#Page Title
text = tk.Label(master = membership_page, text = "Select an option",bg="light coral", font = titleFont)
text.grid(row=0, column=1)

#Sidebar
memsidebar = tk.Label(master = membership_page, image = membership_sbar)
memsidebar.grid(row=1,column = 0, rowspan = 3)

#button createmember
creation_button = tk.Button(master = membership_page,
                            text = "1. Creation",
                            font = buttonFont,
                            bg = "aquamarine",
                            command = lambda:show_frame(membercreation_page))
creation_button.grid(row = 1, column=1)

creation_text = tk.Label(master = membership_page,
                         text = "Creation of new Membership Details",
                         font = buttonFont,
                         bg = "aquamarine",width=30, height=2)
creation_text.grid(row = 1, column = 2,pady=20)



#button deletemember
delete_button = tk.Button(master = membership_page,
                          text = "2. Deletion",
                          font = buttonFont,
                          bg = "aquamarine",
                          command = lambda:show_frame(memberdeletion_page))
delete_button.grid(row = 2, column=1,pady=20)
delete_text = tk.Label(master = membership_page,
                       text = "Deletion of existing Membership Details",
                       font = buttonFont,
                       bg = "aquamarine", width =30,height = 2)
delete_text.grid(row =2, column = 2)

#button updatemember
update_button = tk.Button(master = membership_page,
                          text = "3. Update",
                          font = buttonFont,
                          bg = "aquamarine",
                          command = lambda:show_frame(memberupdate_page))
update_button.grid(row=3, column=1,pady=20)
update_text = tk.Label(master = membership_page,
                       text = "Update of existing Membership Details",
                       font = buttonFont,
                       bg = "aquamarine", width =30,height = 2)
update_text.grid(row=3, column =2)

#button go back main menu
back_button = tk.Button(master=membership_page,
                        text="Back to Main Menu",
                        font = buttonFont,
                        bg = "aquamarine",
                        command=lambda:show_frame(start_page))
back_button.grid(row=4, column=1, pady= 20)
#===========================BOOKS PAGE===========================#
#button addbook
#button deletebook
#button go back main menu

#Page Title
text = tk.Label(master = books_page, text = "Select an option",bg="light coral", font = titleFont)
text.grid(row=0,column=1)


#Sidebar
booksidebar = tk.Label(master = books_page, image = books_sbar)
booksidebar.grid(row=1,column = 0, rowspan = 2)

#button addbook
addbook_button = tk.Button(master=books_page,
                           text="4. Acquisition",
                           font=buttonFont,
                           bg = "aquamarine",
                           command=lambda:show_frame(addbook_page))
addbook_button.grid(row=1, column=1,pady= 20)

#text addbook
addbook_text = tk.Label(master=books_page,
                        text="Book Acquisition",
                        font = buttonFont,
                        bg = "aquamarine",
                        width = 30,
                        height = 1)
addbook_text.grid(row=1,column=2,pady= 20)

#button deletebook
deletebook_button = tk.Button(master=books_page,
                              text="5. Withdrawal",
                              font=buttonFont,
                              bg = "aquamarine",
                              command=lambda:show_frame(deletebook_page))
deletebook_button.grid(row=2, column=1,pady= 20)

#text deletebook
deletebook_text = tk.Label(master=books_page,
                        text="Book Withdrawal",
                        font = buttonFont,
                        bg = "aquamarine",
                        width = 30,
                        height = 1)
deletebook_text.grid(row=2,column=2,pady= 20)

#button go back main menu
back_button = tk.Button(master = books_page,
                        text="Back to Main Menu",
                        font = buttonFont,
                        bg= "aquamarine",
                        command=lambda:show_frame(start_page))
back_button.grid(row=3,column=1,pady=20)
#===========================LOANS PAGE============================#
#button borrowbook
#button returnbook
#button go back main menu

#Page Title
text = tk.Label(master = loans_page, text = "Select an option",bg="light coral", font = titleFont)
text.grid(row = 0, column = 1)

#Sidebar
loansidebar = tk.Label(master = loans_page, image = loans_sbar)
loansidebar.grid(row=1,column = 0, rowspan = 2)

#button borrowbook
borrowbook_button = tk.Button(master=loans_page,\
                           text="6. Borrow",\
                           font=buttonFont,
                              bg = "aquamarine",
                           command=lambda:show_frame(borrowbook_page))
borrowbook_button.grid(row=1, column=1,pady= 20)

#text borrowbook
borrowbook_text = tk.Label(master = loans_page,
                           text = "Book Borrowing",
                           font=buttonFont,
                           bg = "aquamarine",
                           width=30,
                           height=1)
borrowbook_text.grid(row=1,column=2,pady= 20)

#button returnbook
returnbook_button = tk.Button(master=loans_page,\
                              text="7. Return",\
                              font=buttonFont,
                              bg= "aquamarine",
                              command=lambda:show_frame(returnbook_page))
returnbook_button.grid(row=2, column=1,pady= 20)

#text returnbook
returnbook_text = tk.Label(master = loans_page,
                           text = "Book Returning",
                           font=buttonFont,
                           bg = "aquamarine",
                           width=30,
                           height=1)
returnbook_text.grid(row=2,column=2,pady= 20)

#button go back main menu
back_button = tk.Button(master = loans_page,
                        text="Back to Main Menu",
                        font = buttonFont,
                        bg= "aquamarine",
                        command=lambda:show_frame(start_page))
back_button.grid(row = 3, column=1,pady=20)
#=====================RESERVATIONS PAGE============================#
#button bookreserve
#button cancelreservation
#button go back main menu

#Page Title
text = tk.Label(master = reservations_page, text = "Select an option",bg="light coral", font = titleFont)
text.grid(row =0, column=1)

#Sidebar
reservationsidebar = tk.Label(master = reservations_page, image = reservations_sbar)
reservationsidebar.grid(row=1,column = 0, rowspan = 2)

#button bookreserve
reservebook_button = tk.Button(master=reservations_page,
                              text="8. Reserve a Book",
                              font=buttonFont,
                               bg = "aquamarine",
                              command=lambda:show_frame(makereservation_page))
reservebook_button.grid(row=1,column=1,pady= 20)

#text bbokreserve
bookreserve_text = tk.Label(master = reservations_page,
                           text = "Book Reservation",
                           font=buttonFont,
                           bg = "aquamarine",
                           width=30,
                           height=1)
bookreserve_text.grid(row=1,column=2,pady= 20)

#button cancelreservation
cancelreservation_button = tk.Button(master=reservations_page,
                              text="9. Cancel Reservation",
                              font=buttonFont,bg = "aquamarine",
                              command=lambda:show_frame(cancelreservation_page))
cancelreservation_button.grid(row=2, column=1,pady= 20)

#text cancelreservation
cancelres_text = tk.Label(master = reservations_page,
                           text = "Reservation Cancellation",
                           font=buttonFont,
                           bg = "aquamarine",
                           width=30,
                           height=1)
cancelres_text.grid(row=2,column=2,pady= 20)

#button go back main menu
back_button = tk.Button(master = reservations_page,
                        text="Back to Main Menu",
                        font = buttonFont,
                        bg = "aquamarine",
                        command=lambda:show_frame(start_page))
back_button.grid(row=3, column=1,pady= 20)
#===========================FINES PAGE============================#
#button finepayment
#button go back main menu

#Page Title
text = tk.Label(master = fines_page, text = "Select an option", bg="light coral",font = titleFont)
text.grid(row = 0, column = 1,pady= 20)


#Sidebar
finesidebar = tk.Label(master = fines_page, image = fines_sbar)
finesidebar.grid(row=0,column = 0, rowspan = 1)


#button finepayment
payfine_button = tk.Button(master = fines_page,
                              text="10. Payment",
                              font=buttonFont,
                           bg = "aquamarine",
                              command=lambda:show_frame(finepayment_page))
payfine_button.grid(row=1, column = 1,pady= 20)

#text finepayment
payfine_text = tk.Label(master = fines_page,
                           text = "Fine Payment",
                           font=buttonFont,
                           bg = "aquamarine",
                           width=30,
                           height=1)
payfine_text.grid(row=1,column=2,pady= 20)

#button go back main menu
back_button = tk.Button(master = fines_page,
                        text="Back to Main Menu",
                        bg = "aquamarine",
                        font = buttonFont,
                        command=lambda:show_frame(start_page))
back_button.grid(row=2, column=1,pady=20)
#===========================REPORT PAGE============================#
#button booksearch
#button display bookonloan
#button display bookonreservation
#button display memberwithfine
#button display loansbymember
#button go back main menu

#Page Title
text = tk.Label(master = report_page, text = "Select an option",bg="light coral", font = titleFont)
text.grid(row=0,column=1)


#Sidebar
reportsidebar = tk.Label(master = report_page, image = reports_sbar)
reportsidebar.grid(row=1,column = 0, rowspan = 5)


#button booksearch
booksearch_button = tk.Button(master = report_page,
                              text="11. Book Search",
                              bg = "aquamarine",
                              font=buttonFont,
                              command=lambda:show_frame(booksearch_page))
booksearch_button.grid(row=1,column=1,pady= 20)

#text booksearch
booksearch_text = tk.Label(master = report_page,
                           text = "A member can perform a search on the collection of books",
                           font=buttonFont,
                           bg = "aquamarine",
                           width=60,
                           height=1)
booksearch_text.grid(row=1,column=2,pady= 20)

#button display bookonloan
bookonloan_button = tk.Button(master = report_page,
                              text="12. Books on Loan",
                              bg = "aquamarine",
                              font=buttonFont,
                              command=lambda:ActionDL())
bookonloan_button.grid(row=2,column=1,pady= 20)

#text bookonloan
bookonloan_text = tk.Label(master = report_page,
                           text = "Displays all the books currently on loan to members",
                           font=buttonFont,
                           bg = "aquamarine",
                           width=60,
                           height=1)
bookonloan_text.grid(row=2,column=2)

#button display bookonreservation
bookonreservation_button = tk.Button(master = report_page,
                              text="13. Books on Reservation",
                              font=buttonFont,
                                     bg = "aquamarine",
                              command=lambda:ActionDBR())
bookonreservation_button.grid(row=3,column=1,pady= 10)

#text bookonreservation
bookonreservation_text = tk.Label(master = report_page,
                           text = "Displays all the books that members have reserved",
                           font=buttonFont,
                           bg = "aquamarine",
                           width=60,
                           height=1)
bookonreservation_text.grid(row=3,column=2,pady= 10)

#button display memberwithfine
memberwithfine_button = tk.Button(master = report_page,
                              text="14. Outstanding Fines",
                              font=buttonFont,
                                  bg = "aquamarine",
                              command=lambda:ActionDMWF())
memberwithfine_button.grid(row=4,column=1,pady= 10)

#text outstandingfines
outstandingfines_text = tk.Label(master = report_page,
                           text = "Displays all the fines that members have",
                           font=buttonFont,
                           bg = "aquamarine",
                           width=60,
                           height=1)
outstandingfines_text.grid(row=4,column=2,pady= 10)

#button display loansbymember
loansbymember_button = tk.Button(master = report_page,
                              text="15. Books on Loan to Member",
                              font=buttonFont,
                                 bg = "aquamarine",
                              command=lambda:show_frame(onloanbymember_page))
loansbymember_button.grid(row=5,column=1,pady= 10)

#text loansbymember
loansbymember_text = tk.Label(master = report_page,
                           text = "Displays all the books borrowed by a member",
                           font=buttonFont,
                           bg = "aquamarine",
                           width=60,
                           height=1)
loansbymember_text.grid(row=5,column=2,pady= 10)

#button go back main menu
back_button = tk.Button(master = report_page,
                        text="Back to Main Menu",
                        font = buttonFont,
                        bg = "aquamarine",
                        command=lambda:show_frame(start_page))
back_button.grid(row=6,column=1, pady= 10)
#==========================MEMBERCREATION PAGE====================#
#entry membershipID
#entry name
#entry faculty
#entry phoneNo
#entry email
#button create
#button go back main menu

membershipID = tk.StringVar()
name = tk.StringVar()
faculty = tk.StringVar()
phoneNo = tk.StringVar()
email = tk.StringVar()

def CreateMember(memID, name, faculty, num, email):
    conditionA = False #Member ID already exist
    conditionB = False #Have missing entries
    
    cursor = connection.cursor()
    sql = "SELECT * FROM members WHERE MemID = %s"
    cursor.execute(sql, (memID.get()))
    rows = cursor.fetchall()
    if rows:
        conditionA = True
    
    if not memID.get() or not name.get() or not faculty.get() \
       or not num.get() or not email.get():
        conditionB = True

    top = tk.Toplevel(window)
    top.geometry("400x300")
    if conditionA or conditionB:
        #Show Error Message
        tk.Label(top, text = "Error!", font = alertFont).pack()
        tk.Label(top, text = "Member already exist; Missing or incomplete fields.",
                 font = messageFont).pack()
    else:
        
        sql = "INSERT INTO members(MemID,Name,Faculty,Number,Email,Fines) \
values(%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,(memID.get(),name.get(),faculty.get(),num.get(),email.get(),0))
        #Show Success Message
        tk.Label(top, text = "Success!", font = alertFont).pack()
        tk.Label(top, text = "ALS Membership Created",
                 font = messageFont).pack()
    connection.commit()
    tk.Button(top, text = "Back to Create Function", command = top.destroy).pack()


#Page Title
text = tk.Label(master = membercreation_page,
                text = "To Create Member, Please Enter Requested Information Below:",
                bg="light coral",
                font = titleFont)
text.grid(row=0,column=0,columnspan=2)

#entry membershipID
membershipID_entry = tk.Entry(master = membercreation_page, 
                              font = entryFont, 
                              textvariable = membershipID)
membershipID_label = tk.Label(master = membercreation_page, text = "Membership ID",
                              bg = "light coral",font=30)
membershipID_label.grid(row=1,column=0)
membershipID_entry.grid(row=1,column=1,pady=20)

#entry name
name_entry = tk.Entry(master = membercreation_page,
                      font = entryFont,
                      textvariable = name)
name_label = tk.Label(master = membercreation_page, text = "Name",
                      bg = "light coral",font=30)
name_label.grid(row=2,column=0)
name_entry.grid(row=2,column=1,pady=20)

#entry faculty
faculty_entry = tk.Entry(master = membercreation_page,
                         font = entryFont,
                         textvariable = faculty)
faculty_label = tk.Label(master = membercreation_page, text = "Faculty",
                         bg = "light coral",font=30)
faculty_label.grid(row=3,column=0)
faculty_entry.grid(row=3,column=1,pady=20)

#entry phoneNo
phoneNo_entry = tk.Entry(master = membercreation_page,
                         font = entryFont,
                         textvariable = phoneNo)
phoneNo_label = tk.Label(master = membercreation_page, text = "Phone Number",
                         bg = "light coral",font=30)
phoneNo_label.grid(row=4,column=0)
phoneNo_entry.grid(row=4,column=1,pady=20)

#entry email
email_entry = tk.Entry(master = membercreation_page,
                              font = entryFont, 
                              textvariable = email)
email_label = tk.Label(master = membercreation_page, text = "Email Address",
                       bg = "light coral",font=30)
email_label.grid(row=5,column=0)
email_entry.grid(row=5,column=1,pady=20)

CreateMember = partial(CreateMember, membershipID, name, faculty, phoneNo, email)

#button create
create_button = tk.Button(master = membercreation_page,
                          text = "Create Member",
                          font = buttonFont,
                          bg =  "aquamarine",
                          command = CreateMember)
create_button.grid(row=6,column=0,pady=20)

back_button = tk.Button(master = membercreation_page,
                        text="Back to Membership Menu",
                        font = buttonFont,
                        bg = "aquamarine",
                        command=lambda:show_frame(membership_page))
back_button.grid(row=6,column=1,pady=20)

membercreation_page.columnconfigure(0, weight = 1)
membercreation_page.columnconfigure(1, weight = 1)
#==========================MEMBERDELETION PAGE====================#
#entry membershipID
#button delete
#button go back membership menu

membershipID = tk.StringVar()

def DeleteMember(memID):
    def delete():
        cursor = connection.cursor()
        sql = "DELETE FROM members where MemID = %s"
        cursor.execute(sql, (memID.get()))
        sql = "DELETE FROM fines where MemID = %s"
        cursor.execute(sql, (memID.get()))
        sql = "DELETE FROM loans where MemID = %s"
        cursor.execute(sql, (memID.get()))
        sql = "DELETE FROM reservations where MemID = %s"
        cursor.execute(sql, (memID.get()))
        top = tk.Toplevel(window)
        top.geometry("400x300")
        tk.Label(top, text = "Success!", font = alertFont).pack()
        tk.Label(top, text = "ALS Membership Deleted.",
                 font = messageFont).pack()
        tk.Button(top, text = "Back to Delete Function", command = top.destroy).pack()
        connection.commit()
        
    conditionA = False #Member does not exist
    conditionB = False #Member has loans
    conditionC = False #Member has outstanding fines

    cursor = connection.cursor()
    sql = "SELECT * FROM members WHERE MemID = %s"
    cursor.execute(sql, (memID.get()))
    row = cursor.fetchone()
    if not row:
        conditionA = True

    if conditionA:
        top = tk.Toplevel(window)
        top.geometry("400x300")
        tk.Label(top, text = "Error!", font = alertFont).pack()
        tk.Label(top, text = "Member does not exist.",
                 font = messageFont).pack()
        tk.Button(top, text = "Back to Delete Function", command = top.destroy).pack()
    else:
        sql = "SELECT Fines FROM members where MemID = %s"
        cursor.execute(sql,(memID.get()))
        row = cursor.fetchone()
        fine = row["Fines"]
        if fine > 0:
            conditionB = True

        sql = "SELECT * FROM loans where MemID = %s AND ReturnDate IS NULL"
        cursor.execute(sql, (memID.get()))
        rows = cursor.fetchall()
        if rows:
            conditionC = True

        top = tk.Toplevel(window)
        top.geometry("400x300")
        if conditionB or conditionC:
            #Show Error Message
            tk.Label(top, text = "Error!", font = alertFont).pack()
            tk.Label(top, text = "Member has loans, reservations or outstanding fines.",
                     font = messageFont).pack()
            tk.Button(top, text = "Back to Delete Function", command = top.destroy).pack()
        else:
            #Show Confirmation Page
            sql = "SELECT * FROM members WHERE MemID = %s"
            cursor.execute(sql, (memID.get()))
            row = cursor.fetchone()
            tk.Label(top, text = "Please Confirm Details to \n Be Correct",
                     font = alertFont).grid(row=0,column=0,columnspan=2)
            tk.Label(top, text = "Member ID", font = messageFont).grid(row=1,column=0)
            tk.Label(top, text = row["MemID"], font = messageFont).grid(row=1,column=1)
            tk.Label(top, text = "Name", font = messageFont).grid(row=2,column=0)
            tk.Label(top, text = row["Name"], font = messageFont).grid(row=2,column=1)
            tk.Label(top, text = "Faculty", font = messageFont).grid(row=3,column=0)
            tk.Label(top, text = row["Faculty"], font = messageFont).grid(row=3,column=1)
            tk.Label(top, text = "Phone Number", font = messageFont).grid(row=4,column=0)
            tk.Label(top, text = row["Number"], font = messageFont).grid(row=4,column=1)
            tk.Label(top, text = "Email Address", font = messageFont).grid(row=5,column=0)
            tk.Label(top, text = row["Email"], font = messageFont).grid(row=5,column=1)
            tk.Button(top, text = "Confirm \n Deletion",
                      command = lambda:[delete(), top.destroy()]).grid(row=6,column=0)
            tk.Button(top, text = "Back to Delete Function",
                      command = top.destroy).grid(row=6,column=1)

            top.columnconfigure(0, weight = 1)
            top.columnconfigure(1, weight = 1)

#Page Title
text = tk.Label(master = memberdeletion_page,
                text = "To Delete Member, Please Enter Membership ID:", 
                font = titleFont,
                bg="light coral")
text.grid(row=0,column=0,columnspan=2)

#entry membershipID
membershipID_entry = tk.Entry(master = memberdeletion_page, 
                              font = entryFont, 
                              textvariable = membershipID)
membershipID_label = tk.Label(master = memberdeletion_page, text = "Membership ID",
                              bg = "light coral",font=30)
membershipID_label.grid(row=1,column=0)
membershipID_entry.grid(row=1,column=1,pady=20)

DeleteMember = partial(DeleteMember, membershipID)

#button delete
delete_button = tk.Button(master = memberdeletion_page,
                          text = "Delete Member",
                          font = buttonFont,
                          bg = "aquamarine",
                          command = DeleteMember)
delete_button.grid(row=2,column=0,pady = 20)

#button go back membership menu
back_button = tk.Button(master = memberdeletion_page,
                        text="Back to Membership Menu",
                        font = buttonFont,
                        bg = "aquamarine",
                        command=lambda:show_frame(membership_page))
back_button.grid(row=2,column=1, pady = 20)

memberdeletion_page.columnconfigure(0, weight = 1)
memberdeletion_page.columnconfigure(1, weight = 1)
#==========================MEMBERUPDATE PAGE====================#
#entry membershipID
#entry name
#entry faculty
#entry phoneNo
#entry email
#button update
#button back to membership

membershipID = tk.StringVar()
name = tk.StringVar()
faculty = tk.StringVar()
phoneNo = tk.StringVar()
email = tk.StringVar()

def UpdateMember(memID, name, faculty, num, email):
    cursor = connection.cursor()
    def update():
        sql = "UPDATE members SET Name = %s, Faculty = %s, Number = %s, \
Email = %s WHERE MemID = %s"
        cursor.execute(sql, (name.get(),faculty.get(),num.get(),email.get(),memID.get()))
        top = tk.Toplevel(window)
        top.geometry("400x300")
        tk.Label(top, text = "Success!", font = alertFont).pack()
        tk.Label(top, text = "ALS Membership Updated",
                 font = messageFont).pack()
        tk.Button(top, text = "Create Another\nMember",
                  command = lambda:[show_frame(membercreation_page), top.destroy()]).pack()
        tk.Button(top, text = "Back to\nUpdate\nMember",
                  command = top.destroy).pack()
        connection.commit()
    
    conditionA = True #If memID not exist
    conditionB = False #Fields are invalid (missing)
    sql = "SELECT * FROM members WHERE MemID = %s"
    cursor.execute(sql, (memID.get()))
    rows = cursor.fetchall()
    if rows:
        conditionA = False

    if not memID.get() or not name.get() or not faculty.get() \
       or not num.get() or not email.get():
        conditionB = True

    top = tk.Toplevel(window)
    top.geometry("400x300")
    if conditionA:
        tk.Label(top, text = "Error!", font = alertFont).pack()
        tk.Label(top, text = "Membership ID does not exist.",
                 font = messageFont).pack()
        tk.Button(top, text = "Back to Update Function", command = top.destroy).pack()
    elif conditionB:
        tk.Label(top, text = "Error!", font = alertFont).pack()
        tk.Label(top, text = "Missing or incomplete fields.",
                 font = messageFont).pack()
        tk.Button(top, text = "Back to Update Function", command = top.destroy).pack()
    else:
        tk.Label(top, text = "Please Confirm Updated \nDetails to Be Correct",
                 font = alertFont).grid(row=0,column=0,columnspan=2)
        tk.Label(top, text = "Member ID", font = messageFont).grid(row=1,column=0)
        tk.Label(top, text = memID.get(), font = messageFont).grid(row=1,column=1)
        tk.Label(top, text = "Name", font = messageFont).grid(row=2,column=0)
        tk.Label(top, text = name.get(), font = messageFont).grid(row=2,column=1)
        tk.Label(top, text = "Faculty", font = messageFont).grid(row=3,column=0)
        tk.Label(top, text = faculty.get(), font = messageFont).grid(row=3,column=1)
        tk.Label(top, text = "Phone Number", font = messageFont).grid(row=4,column=0)
        tk.Label(top, text = num.get(), font = messageFont).grid(row=4,column=1)
        tk.Label(top, text = "Email Address", font = messageFont).grid(row=5,column=0)
        tk.Label(top, text = email.get(), font = messageFont).grid(row=5,column=1)
        tk.Button(top, text = "Confirm \n Update",
                  command = lambda:[update(), top.destroy()]).grid(row=6,column=0)
        tk.Button(top, text = "Back to Update Function",
                  command = top.destroy).grid(row=6,column=1)

        top.columnconfigure(0, weight = 1)
        top.columnconfigure(1, weight = 1)        



#Page Title
text = tk.Label(master = memberupdate_page,
                text = "To Enter Update Details:",
                bg="light coral",
                font = titleFont)
text.grid(row=0,column=0,columnspan=2)

#entry membershipID
membershipID_entry = tk.Entry(master = memberupdate_page, 
                              font = entryFont, 
                              textvariable = membershipID)
membershipID_label = tk.Label(master = memberupdate_page, text = "Membership ID",
                              bg = "light coral",font=30)
membershipID_label.grid(row=1,column=0)
membershipID_entry.grid(row=1,column=1,pady=20)

#entry name
name_entry = tk.Entry(master = memberupdate_page,
                      font = entryFont,
                      textvariable = name)
name_label = tk.Label(master = memberupdate_page, text = "Name", bg = "light coral",font=30)
name_label.grid(row=2,column=0)
name_entry.grid(row=2,column=1,pady=20)

#entry faculty
faculty_entry = tk.Entry(master = memberupdate_page,
                         font = entryFont,
                         textvariable = faculty)
faculty_label = tk.Label(master = memberupdate_page, text = "Faculty", bg = "light coral",font=30)
faculty_label.grid(row=3,column=0)
faculty_entry.grid(row=3,column=1,pady=20)

#entry phoneNo
phoneNo_entry = tk.Entry(master = memberupdate_page,
                         font = entryFont,
                         textvariable = phoneNo)
phoneNo_label = tk.Label(master = memberupdate_page, text = "Phone Number", bg = "light coral",font=30)
phoneNo_label.grid(row=4,column=0)
phoneNo_entry.grid(row=4,column=1,pady=20)

#entry email
email_entry = tk.Entry(master = memberupdate_page,
                       text = "Email Address",
                       font = entryFont,
                       textvariable = email)
email_label = tk.Label(master = memberupdate_page, text = "Email Address", bg = "light coral",font=30)
email_label.grid(row=5,column=0)
email_entry.grid(row=5,column=1,pady=20)

UpdateMember = partial(UpdateMember, membershipID, name, faculty, phoneNo, email)

#button update
update_button = tk.Button(master = memberupdate_page,
                          text = "Update Member",
                          font = buttonFont,
                          bg = "aquamarine",
                          command = UpdateMember)
update_button.grid(row=6,column=0,pady = 20)

#button back to membership
back_button = tk.Button(master = memberupdate_page,
                        text="Back to Membership Menu",
                        font = buttonFont,
                        bg = "aquamarine",
                        command=lambda:show_frame(membership_page))
back_button.grid(row=6,column=1, pady = 20)

memberupdate_page.columnconfigure(0, weight = 1)
memberupdate_page.columnconfigure(1, weight = 1)
#=========================ACQUISTION PAGE=========================#
#entry accessionNo
#entry title
#entry authors
#entry isbn
#entry publisher
#entry publication year
#button addbook
#button back to books menu

acc = tk.StringVar()
title = tk.StringVar()
authors = tk.StringVar()
isbn = tk.StringVar()
publisher = tk.StringVar()
publication_year = tk.StringVar()


def Success1():
    top = tk.Toplevel(window)
    top.geometry("400x300")
    tk.Label(top,text="Success!",font=alertFont).pack()
    tk.Label(top,text="Book Added",font=messageFont).pack()
    tk.Button(top,text="OK",command=top.destroy).pack()

def sqlAddBook(acc,title,authors,isbn,publisher,publication_year):
    def add():
        cursor = connection.cursor()
        sql = "INSERT into books(Accession, Title, Authors, ISBN, Publisher,\
PublicationYear) value (%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,(acc.get(),title.get(),authors.get(),isbn.get(),publisher.get(),\
                            publication_year.get()))
        connection.commit()
    conA = False #Book ACC alr in database

    cursor = connection.cursor()
    sql = "SELECT Accession FROM Books WHERE Accession = %s"
    cursor.execute(sql,(acc.get()))
    row = cursor.fetchone()
    if row:
        conA = True

    top = tk.Toplevel(window)
    top.geometry("400x300")
    if conA:
        tk.Label(top, text = "Error!", font=alertFont).pack()
        tk.Label(top, text="Book of similar Accession Number already in \
library.", font=messageFont).pack()
        tk.Button(top,text="Go Back",command=top.destroy).pack()
    else:
        tk.Label(top,text="Please Confirm Details Are Correct",
                 font=alertFont).grid(row=0,column=0,columnspan=2)
        tk.Label(top,text="Accession Number",font=messageFont).grid(row=1,column=0)
        tk.Label(top,text=acc.get(),font=messageFont).grid(row=1,column=1)         
        tk.Label(top,text="Title",font=messageFont).grid(row=2,column=0)
        tk.Label(top,text=title.get(),font=messageFont).grid(row=2,column=1)
        tk.Label(top,text="Authors",font=messageFont).grid(row=3,column=0)
        tk.Label(top,text=authors.get(),font=messageFont).grid(row=3,column=1)
        tk.Label(top,text="ISBN",font=messageFont).grid(row=4,column=0)
        tk.Label(top,text=isbn.get(),font=messageFont).grid(row=4,column=1)
        tk.Label(top,text="Publisher",font=messageFont).grid(row=5,column=0)
        tk.Label(top,text=publisher.get(),font=messageFont).grid(row=5,column=1)
        tk.Label(top,text="Publication Year",font=messageFont).grid(row=6,column=0)
        tk.Label(top,text=publication_year.get(),font=messageFont).grid(row=6,column=1)
        tk.Button(top,text="Confirm \n Acquisition",command=\
                  lambda:[add(),top.destroy(),Success1()]).grid\
                                    (row=7,column=0)
        tk.Button(top,text="Go Back",command=top.destroy).grid(row=7,column=1)
#Page Title    
text = tk.Label(master = addbook_page,
                text = "For New Book Acquisition, Enter Required Information Below:", 
                bg="light coral",
                font = titleFont)
text.grid(row=0,column=0,columnspan=2)

#entry accessionNo
acc_entry = tk.Entry(master = addbook_page,
                     font = entryFont, textvariable = acc)
acc_label = tk.Label(master = addbook_page,bg="light coral",font=30, text = "Accession Number")
acc_label.grid(row=1,column=0)
acc_entry.grid(row=1,column=1,pady=20)

#entry title
title_entry = tk.Entry(master=addbook_page,
                       font=entryFont,textvariable=title)
title_label = tk.Label(master = addbook_page,bg="light coral",font=30, text = "Title")
title_label.grid(row=2,column=0)
title_entry.grid(row=2,column=1,pady=20)

#entry authors
authors_entry = tk.Entry(master=addbook_page,
                       font=entryFont,textvariable=authors)
authors_label = tk.Label(master = addbook_page,bg="light coral",font=30, text = "Authors")
authors_label.grid(row=3,column=0)
authors_entry.grid(row=3,column=1,pady=20)

#entry isbn
isbn_entry = tk.Entry(master=addbook_page,
                       font=entryFont,textvariable=isbn)
isbn_label = tk.Label(master = addbook_page,bg="light coral",font=30, text = "ISBN")
isbn_label.grid(row=4,column=0)
isbn_entry.grid(row=4,column=1,pady=20)

#entry publisher
publisher_entry = tk.Entry(master=addbook_page,
                       font=entryFont,textvariable=publisher)
publisher_label = tk.Label(master = addbook_page,bg="light coral",font=30, text = "Publisher")
publisher_label.grid(row=5,column=0)
publisher_entry.grid(row=5,column=1,pady=20)

#entry publication year
publication_entry = tk.Entry(master=addbook_page,
                       font=entryFont,textvariable=publication_year)
publication_label = tk.Label(master = addbook_page,bg="light coral",font=30, text = "Publication Year")
publication_label.grid(row=6,column=0)
publication_entry.grid(row=6,column=1,pady=20)

sqlAddBook = partial(sqlAddBook,acc,title,authors,isbn,publisher,publication_year)

#button addbook
add_button = tk.Button(master=addbook_page,text="Add New Book",\
                       font=buttonFont,bg="aquamarine",command= sqlAddBook)
add_button.grid(row=7,column=0)

#button back to books menu
back_button = tk.Button(master = addbook_page,
                        text="Back to Books Page",
                        font = buttonFont,bg="aquamarine",
                        command=lambda:show_frame(books_page))
back_button.grid(row=7,column=1)

addbook_page.columnconfigure(0, weight = 1)
addbook_page.columnconfigure(1, weight = 1)
#===========================WITHDRAWAL PAGE======================#
#text
#entry withdrawal
#button delete
#button back

acce = tk.StringVar()

def Success2():
    top = tk.Toplevel(window)
    top.geometry("400x300")
    tk.Label(top,text="Success!",font=alertFont).pack()
    tk.Label(top,text="Book Withdrawn",font=messageFont).pack()
    tk.Button(top,text="OK",command=top.destroy).pack()

def WithdrawBook(acc):
    def withdraw():
        cursor=connection.cursor()
        sql = "DELETE FROM loans where Accession = %s"
        cursor.execute(sql,(acc.get()))
        sql = "DELETE FROM books where Accession = %s"
        cursor.execute(sql,(acc.get()))
        connection.commit()
    conA = False

    cursor=connection.cursor()
    sql = "SELECT * FROM books WHERE Accession = %s"
    cursor.execute(sql,(acc.get()))
    row=cursor.fetchone()
    if not row:
        conA=True
    top = tk.Toplevel(window)
    top.geometry("400x300")
    if conA:
        tk.Label(top,text="Error!",font=alertFont).pack()
        tk.Label(top,text="No such Book in Library",font=messageFont).pack()
        tk.Button(top,text="Go Back",command=top.destroy).pack()
    else:
        tk.Label(top,text="Confirm Details of Book to be Deleted",font=alertFont).\
                                   grid(row=0,column=0,columnspan=2)
        tk.Label(top,text="Accession Number",font=messageFont).grid(row=1,column=0)
        tk.Label(top,text=row["Accession"],font=messageFont).grid(row=1,column=1)         
        tk.Label(top,text="Title",font=messageFont).grid(row=2,column=0)
        tk.Label(top,text=row["Title"],font=messageFont).grid(row=2,column=1)
        tk.Label(top,text="Authors",font=messageFont).grid(row=3,column=0)
        tk.Label(top,text=row["Authors"],font=messageFont).grid(row=3,column=1)
        tk.Label(top,text="ISBN",font=messageFont).grid(row=4,column=0)
        tk.Label(top,text=row["ISBN"],font=messageFont).grid(row=4,column=1)
        tk.Label(top,text="Publisher",font=messageFont).grid(row=5,column=0)
        tk.Label(top,text=row["Publisher"],font=messageFont).grid(row=5,column=1)
        tk.Label(top,text="Publication Year",font=messageFont).grid(row=6,column=0)
        tk.Label(top,text=row["PublicationYear"],font=messageFont).grid(row=6,column=1)
        tk.Button(top,text="Confirm Deletion",command=lambda:[withdraw(),top.destroy(),\
                                                              Success2()]).\
                                    grid(row=7,column=0)
        tk.Button(top,text="Go Back",command=top.destroy).grid(row=7,column=1)

        top.columnconfigure(0, weight = 1)
        top.columnconfigure(1, weight = 1)

text = tk.Label(master = deletebook_page,
                text = "For New Book Acquisition, Enter Required Information Below:",
                bg="light coral",
                font = titleFont)

withdraw_entry = tk.Entry(master = deletebook_page,
                     font = entryFont, textvariable = acce)
withdraw_label = tk.Label(master = deletebook_page,font=30,bg="light coral", text = "Accession Number")
withdraw_label.grid(row=1,column=0)
withdraw_entry.grid(row=1,column=1,pady=20)
text.grid(row=0,column=0,columnspan=2)

WithdrawBook = partial(WithdrawBook,acce)

withdraw_button = tk.Button(master=deletebook_page,text="Wtihdraw Book",\
                       font=buttonFont,bg="aquamarine",command= WithdrawBook)
withdraw_button.grid(row=2,column=0,pady=20)

back_button = tk.Button(master = deletebook_page,
                        text="Back to Books Page",
                        font = buttonFont,bg="aquamarine",
                        command=lambda:show_frame(books_page))
back_button.grid(row=2,column=1)

deletebook_page.columnconfigure(0, weight = 1)
deletebook_page.columnconfigure(1, weight = 1)




#===========================BORROW BOOK PAGE======================#
#entry accessionNo
#entry membershipID
#button borrow
#button back to loans page

def Success3():
    top = tk.Toplevel(window)
    top.geometry("400x300")
    tk.Label(top,text="Success!",font=alertFont).pack()
    tk.Label(top,text="Book Borrowed",font=messageFont).pack()
    tk.Button(top,text="OK",command=top.destroy).pack()

def Borrow(AccessionNo, MemID, currentDate):
    def borrow():
        sql = "DELETE FROM reservations where MemID = %s and Accession = %s"
        cursor.execute(sql, (MemID.get(),AccessionNo.get()))
        dueDate = currentDate + datetime.timedelta(days = 14)
        sql = "INSERT INTO loans (Accession, LoanDate, DueDate, MemID) VALUES \
    (%s, %s, %s, %s)"
        cursor.execute(sql, (AccessionNo.get(), currentDate, dueDate, MemID.get()))
        tk.Label(top, text = "Success!", font = alertFont).grid(row=0)
        tk.Label(top, text = "Book Loan Confirmed", font = messageFont).grid(row=1)
        connection.commit()
    conditionA = False #Member has fines
    conditionB = False #Book reserved
    conditionC = False #Book on loan
    conditionD = False #Member borrow ==2
    
    cursor = connection.cursor()
    #check for fines
    sql = "SELECT MemID, Fines FROM members WHERE MemID = %s"
    cursor.execute(sql, (MemID.get()))
    row = cursor.fetchone()
    if row:
        if row["Fines"] != 0:
            conditionA = True
    #check for reservations
    sql = "SELECT Accession,MemID,ReserveDate FROM reservations WHERE MemID = %s ORDER BY ReserveDate"
    cursor.execute(sql, (MemID.get()))
    row = cursor.fetchone()
    if row:
        if row["MemID"] != MemID.get():
            conditionB = True
    #check whether on loan
    sql = "SELECT Accession, DueDate, ReturnDate from Loans where Accession = %s and ReturnDate is null"
    cursor.execute(sql, (AccessionNo.get()))
    row = cursor.fetchone()
    if row:
        conditionC= True
        date = row["DueDate"]
    #check whether member borrow >= 2
    sql = "SELECT * FROM loans where MemID = %s and \
ReturnDate IS NULL"
    cursor.execute(sql, (MemID.get()))
    row = cursor.fetchall()
    if len(row) >= 2:
        conditionD = True

    top = tk.Toplevel(window)
    top.geometry("500x300")
    if conditionA or conditionB or conditionC or conditionD:
        tk.Label(top, text = "Error!", font = alertFont).pack()
        if conditionA:
            tk.Label(top ,text = "Member has outstanding fines", font = messageFont).pack()
            tk.Button(top,text="OK",command=top.destroy).pack()
        elif conditionB:
            tk.Label(top ,text = "Book currently reserved", font = messageFont).pack()
            tk.Button(top,text="OK",command=top.destroy).pack()
        elif conditionC:
            tk.Label(top ,text = f'Book currently on loan until {date}', font = messageFont).pack()
            tk.Button(top,text="OK",command=top.destroy).pack()
        elif conditionD:
            tk.Label(top, text = "Loan quota exceeded", font = messageFont).pack()
            tk.Button(top,text="OK",command=top.destroy).pack()
    else:
        #CAN BORROW
        sql = "SELECT * FROM members where MemID = %s"
        cursor.execute(sql, (MemID.get()))
        row = cursor.fetchone()
        name = row["Name"]
        sql = "Select Title from books where Accession = %s"
        cursor.execute(sql, (AccessionNo.get()))
        dueDate = currentDate + datetime.timedelta(days = 14)
        row = cursor.fetchone()
        title = row["Title"]
        tk.Label(top, text = "Please Confirm Details to \n Be Correct",
                 font = alertFont).grid(row=0,column=0,columnspan=2)
        tk.Label(top, text = "Accession Number", font = messageFont).grid(row=1,column=0)
        tk.Label(top, text = AccessionNo.get(), font = messageFont).grid(row=1,column=1)
        tk.Label(top, text = "Book Title", font = messageFont).grid(row=2,column=0)
        tk.Label(top, text = title, font = messageFont).grid(row=2,column=1)
        tk.Label(top, text = "Borrow Date", font = messageFont).grid(row=3,column=0)
        tk.Label(top, text = currentDate, font = messageFont).grid(row=3,column=1)
        tk.Label(top, text = "Membership ID", font = messageFont).grid(row=4,column=0)
        tk.Label(top, text = MemID.get(), font = messageFont).grid(row=4,column=1)
        tk.Label(top, text = "Member Name", font = messageFont).grid(row=5,column=0)
        tk.Label(top, text = name, font = messageFont).grid(row=5,column=1)
        tk.Label(top, text = "Due Date", font = messageFont).grid(row=6,column=0)
        tk.Label(top, text = dueDate, font = messageFont).grid(row=6,column=1)
        tk.Button(top, text = "Confirm \n Loan",
                  command = lambda:[borrow(), top.destroy(),Success3()]).grid(row=7,column=0)
        tk.Button(top, text = "Back to Borrow Function", command = top.destroy).grid(row=7, column = 1)

acc = tk.StringVar()
membershipID = tk.StringVar()

#Page Title
text = tk.Label(master = borrowbook_page,
                text = "To Borrow a Book, Please Enter Required\
Information Below:", 
                bg="light coral",
                font = titleFont)
text.grid(row=0,column=0,columnspan=2)

#acc entry
acc_entry = tk.Entry(master = borrowbook_page,
                     font = entryFont, textvariable = acc)
acc_label = tk.Label(master = borrowbook_page,
                              text = "Accession Number", bg= "light coral",font=30)
acc_label.grid(row=1,column=0)
acc_entry.grid(row=1,column=1,pady=20)

#membershipID entry
membershipID_entry = tk.Entry(master = borrowbook_page,
                       font=entryFont,textvariable = membershipID)
membershipID_label = tk.Label(master = borrowbook_page,
                              text = "Membership ID", bg="light coral",font=30)
membershipID_label.grid(row=2,column=0)
membershipID_entry.grid(row=2,column=1,pady=20)


currentdate_label = tk.Label(master = borrowbook_page,
                              text = "Current Date",bg = "light coral",font=30)
currentdate_label.grid(row=3, column = 0)
currentDate = DateEntry(borrowbook_page, height = 30, width = 41)
currentDate.grid(row=3, column =1,pady=20)

Borrow = partial(Borrow, acc, membershipID, currentDate.get_date())

#borrow book button
borrow_button = tk.Button(master=borrowbook_page,text="Borrow Book",\
                       font=buttonFont,bg = "aquamarine", command= Borrow)
borrow_button.grid(row=4,column=0,pady = 20)

#back button
back_button = tk.Button(master = borrowbook_page,
                        text="Back to Loans Page",
                        font = buttonFont, bg="aquamarine",
                        command=lambda:show_frame(loans_page))
back_button.grid(row=4,column=1,pady = 20)



borrowbook_page.columnconfigure(0, weight = 1)
borrowbook_page.columnconfigure(1, weight = 1)

#===========================RETURN BOOK PAGE======================#
#entry accessionNo
#entry returnDate
#button return 
#button back to loans page

acce = tk.StringVar()

def Success():
    top = tk.Toplevel(window)
    top.geometry("400x300")
    tk.Label(top,text="Success!",font=alertFont).pack()
    tk.Label(top,text="Book Returned",font=messageFont).pack()
    tk.Button(top,text="OK",command=top.destroy).pack()

def ReturnBook(acc,rdate):
    def rreturn():
        cursor=connection.cursor()
        sql = "SELECT * FROM loans WHERE Accession = %s"
        cursor.execute(sql,(acc.get()))
        loanRes = cursor.fetchone()
        fines = 0
        if rdate.get_date() > loanRes["DueDate"]:
            fines = rdate.get_date() - loanRes["DueDate"]
            fines = fines.days
        sql = "SELECT * FROM members WHERE MemID = %s"
        cursor.execute(sql,(loanRes["MemID"]))
        row = cursor.fetchone()
        fines += row["Fines"]
        sql = "UPDATE members SET fines=%s WHERE MemID = %s"
        cursor.execute(sql,(fines,loanRes["MemID"]))
        sql="UPDATE loans SET ReturnDate = %s WHERE Accession = %s"
        cursor.execute(sql,(rdate.get_date(),acc.get()))
        connection.commit()
    
    conA = False

    cursor = connection.cursor()
    sql = "SELECT * FROM loans WHERE Accession = %s AND ReturnDate IS NULL"
    cursor.execute(sql,(acc.get()))
    rows = cursor.fetchone()
    if not rows:
        conA = True
    top = tk.Toplevel(window)
    top.geometry("400x300")
    if conA:
        tk.Label(top,text="Error!",font=alertFont).pack()
        tk.Label(top,text="Book is not out on Loan",font=messageFont).pack()
        tk.Button(top,text="Go Back",command=top.destroy).pack()
    else:
        sql = "SELECT DueDate FROM loans WHERE Accession = %s"
        cursor.execute(sql,(acc.get()))
        loanRes = cursor.fetchone()
        fines = 0
        if rdate.get_date() > loanRes["DueDate"]:
            fines = rdate.get_date() - loanRes["DueDate"]
            fines = fines.days
        tk.Label(top,text="Confirm Return?",font=alertFont).grid(row=0,column=0,columnspan=2)
        tk.Label(top,text="Accession Number",font=messageFont).grid(row=1,column=0)
        tk.Label(top,text=rows["Accession"],font=messageFont).grid(row=1,column=1)
        tk.Label(top,text="Fines Generated",font=messageFont).grid(row=2,column=0)
        tk.Label(top,text=f'{fines}',font=messageFont).grid(row=2,column=1)
        tk.Button(top,text="Confirm Return",command=lambda:[rreturn(),top.destroy()]).\
                                    grid(row=3,column=0)
        tk.Button(top,text="Go Back",command=top.destroy).grid(row=3,column=1)

        top.columnconfigure(0, weight = 1)
        top.columnconfigure(1, weight = 1)
        
         
        
        

#Page Title
text = tk.Label(master = returnbook_page,
                text = "To Return a Book, Please Enter Required\
Information Below:", 
                bg="light coral",
                font = titleFont)
text.grid(row=0,column=0,columnspan=2)

#acc entry
acc_entry = tk.Entry(master = returnbook_page,
                     font = entryFont, textvariable = acce)
acc_label = tk.Label(master = returnbook_page,
                              text = "Accession Number",bg="light coral",font=30)
acc_label.grid(row=1,column=0)
acc_entry.grid(row=1,column=1,pady=20)

#return date entry
returnDate = DateEntry(returnbook_page,width=41)
returnDate_label = tk.Label(master = returnbook_page,
                              text = "Return Date",bg="light coral",font=30)
returnDate_label.grid(row=2,column=0)
returnDate.grid(row=2,column=1,pady=20)

ReturnBook = partial(ReturnBook,acce,returnDate)

#return book button
return_button = tk.Button(master=returnbook_page,text="Return Book",\
                       font=buttonFont,bg="aquamarine",command= ReturnBook)
return_button.grid(row=3,column=0,pady=20)

#back button
back_button = tk.Button(master = returnbook_page,
                        text="Back to Loans Page",
                        font = buttonFont,bg="aquamarine",
                        command=lambda:show_frame(loans_page))
back_button.grid(row=3,column=1)

returnbook_page.columnconfigure(0, weight = 1)
returnbook_page.columnconfigure(1, weight = 1)
#===========================MAKE RESERVATION PAGE=================#
#entry accessionNo
#entry membershipID
#entry reserveDate
#button reservebook
#button back to reservation menu

def Reserve(acc,mem,date):
    conditionA = False # Has 2 reservations
    conditionB = False # Has fines
    conditionC = False
    
    #check if alr got 2 reservations
    cursor = connection.cursor()
    sql = "SELECT * FROM reservations WHERE MemID = %s"
    cursor.execute(sql,(mem.get()))
    reservation = cursor.fetchall()
    if len(reservation) >= 2:
        conditionA = True
    #check if got fines
    sql = "SELECT Fines FROM members WHERE MemID = %s"
    cursor.execute(sql,(mem.get()))
    fineslist = cursor.fetchone()
    if fineslist:
        fines = fineslist["Fines"]
        if fines > 0:
            conditionB = True
    #check if member already made reservation
    sql = "SELECT * FROM reservations WHERE MemID=%s AND Accession=%s"
    cursor.execute(sql,(mem.get(),acc.get()))
    row=cursor.fetchone()
    if row:
        conditionC=True
    top = tk.Toplevel(window)
    top.geometry("400x300")
    if conditionA or conditionB or conditionC:
        tk.Label(top, text = "Error!", font = alertFont).pack()
        if conditionA:
            tk.Label(top, text = "Member currently has 2 Books on Reservation",font = messageFont).pack()
        elif conditionB:
            tk.Label(top, text = "Member currently has outstanding fines", font = messageFont).pack()
        elif conditionC:
            tk.Label(top,text="Member already reserved this book",font=messageFont).pack()
    else:
        #reserve success
        sql = "INSERT into reservations(Accession, MemID, ReserveDate) value \
    (%s,%s,%s)"
        cursor.execute(sql,(acc.get(),mem.get(),date))
        tk.Label(top, text = "Success!", font = alertFont).pack()
        tk.Label(top, text = "Reservation made",font = messageFont).pack()
        connection.commit()
        tk.Button(top, text = "Back to Reserve Book Function", command = top.destroy).pack()

acc = tk.StringVar()
membershipID = tk.StringVar()

#Page Title    
text = tk.Label(master = makereservation_page,
                text = "For Reserve a Book, Please Enter Information Below:", 
                bg="light coral",
                font = titleFont)
text.grid(row=0,column=0,columnspan=2)



#entry accessionNo
acc_entry = tk.Entry(master = makereservation_page,
                     font = entryFont, textvariable = acc)
acc_label = tk.Label(master = makereservation_page, text = "Accession Number", bg = "light coral",font=30)
acc_label.grid(row=1,column=0)
acc_entry.grid(row=1,column=1,pady=20)

#entry membershipID
membershipID_entry = tk.Entry(master = makereservation_page, 
                              font = entryFont, textvariable = membershipID)
membershipID_label = tk.Label(master = makereservation_page, text = "Membership ID",bg = "light coral",font=30)
membershipID_label.grid(row=2,column=0)
membershipID_entry.grid(row=2,column=1,pady=20)

#entry reserveDate
reserveDate_label = tk.Label(master = makereservation_page, text = "Reserve Date",bg = "light coral",font=30)
reserveDate = DateEntry(makereservation_page, height = 30, width = 41)
reserveDate_label.grid(row=3, column=0,pady=20)
reserveDate.grid(row=3, column =1)

reservebook = partial(Reserve, acc, membershipID, reserveDate.get_date())

#button reservebook
reservebook_button = tk.Button(master=makereservation_page,text="Reserve Book",\
                       font=buttonFont,command = reservebook, bg= "aquamarine")
reservebook_button.grid(row=4,column=0, pady=20)

#button back to reservation menu
back_button = tk.Button(master = makereservation_page,
                        text="Back to Reservations Menu",
                        font = buttonFont, bg= "aquamarine",
                        command=lambda:show_frame(reservations_page))
back_button.grid(row=4,column=1, pady = 20)

makereservation_page.columnconfigure(0, weight = 1)
makereservation_page.columnconfigure(1, weight = 1)
#===========================CANCEL RESERVATION PAGE===============#
#entry accessionNo
#entry membershipID
#entry cancelDate
#button cancelreservation
#button back to reservation menu

acc = tk.StringVar()
membershipID = tk.StringVar()

def CancelReservation(acc, memID, date):
    cursor = connection.cursor()
    def cancel():
        sql = "DELETE FROM reservations WHERE \
Accession = %s AND MemID = %s AND ReserveDate = %s"
        cursor.execute(sql, (acc.get(), memID.get(), date))
        top = tk.Toplevel(window)
        top.geometry("400x300")
        tk.Label(top, text = "Success!", font = alertFont).pack()
        tk.Label(top, text = "Reservation Cancelled", font =messageFont).pack()
        tk.Button(top, text = "Go Back" , command = top.destroy).pack()
        connection.commit()
    
    conditionA = False #Member has no such reservation
    sql = "SELECT * from reservations WHERE Accession = %s \
and MemID = %s and ReserveDate = %s"
    cursor.execute(sql, (acc.get(), memID.get(), date))
    row = cursor.fetchone()
    if not row:
        conditionA = True

    top = tk.Toplevel(window)
    top.geometry("400x300")
    if conditionA:
        tk.Label(top, text = "Error!", font=alertFont).pack()
        tk.Label(top, text="Member has no such reservation.", font=messageFont).pack()
        tk.Button(top,text="Go Back",command=top.destroy).pack()
    else:
        #Show Confirmation Page
        sql = "SELECT Title FROM books WHERE Accession = %s"
        cursor.execute(sql, (acc.get()))
        book = cursor.fetchone()
        sql = "SELECT Name FROM members WHERE MemID = %s"
        cursor.execute(sql, (memID.get()))
        member = cursor.fetchone()
        
        tk.Label(top, text = "Confirm Cancellation\nDetails to Be Correct",
                 font = alertFont).grid(row=0,column=0,columnspan=2)
        tk.Label(top, text = "Accession Number", font = messageFont).grid(row=1,column=0)
        tk.Label(top, text = acc.get(), font = messageFont).grid(row=1,column=1)
        tk.Label(top, text = "Book Title", font = messageFont).grid(row=2,column=0)
        tk.Label(top, text = book["Title"], font = messageFont).grid(row=2,column=1)
        tk.Label(top, text = "Membership ID", font = messageFont).grid(row=3,column=0)
        tk.Label(top, text = memID.get(), font = messageFont).grid(row=3,column=1)
        tk.Label(top, text = "Member Name", font = messageFont).grid(row=4,column=0)
        tk.Label(top, text = member["Name"], font = messageFont).grid(row=4,column=1)
        tk.Label(top, text = "Cancellation Date", font = messageFont).grid(row=5,column=0)
        tk.Label(top, text = date, font = messageFont).grid(row=5,column=1)
        tk.Button(top, text = "Confirm\nCancellation",
                  command = lambda:[cancel(),top.destroy()]).grid(row=6,column=0)
        tk.Button(top,text="Go Back",command=top.destroy).grid(row=6,column=1)

        top.columnconfigure(0, weight = 1)
        top.columnconfigure(1, weight = 1) 
        

#Page Title    
text = tk.Label(master = cancelreservation_page,
                text = "For Cancel a Reservation, Please Enter Information Below:",
                bg="light coral",
                font = titleFont)
text.grid(row=0,column=0,columnspan=2)

#entry accessionNo
acc_entry = tk.Entry(master = cancelreservation_page,
                     font = entryFont, textvariable = acc)
acc_label = tk.Label(master = cancelreservation_page, text = "Accession Number", bg="light coral",font=30)
acc_label.grid(row=1,column=0)
acc_entry.grid(row=1,column=1,pady=20)

#entry membershipID
membershipID_entry = tk.Entry(master = cancelreservation_page, 
                              font = entryFont, textvariable = membershipID)
membershipID_label = tk.Label(master = cancelreservation_page, text = "Membership ID", bg="light coral",font=30)
membershipID_label.grid(row=2,column=0)
membershipID_entry.grid(row=2,column=1,pady=20)

#entry cancelDate
cancelDate_label = tk.Label(master = cancelreservation_page, text = "Cancel date", bg="light coral",font=30)
cancelDate = DateEntry(cancelreservation_page, height=30, width=41)
cancelDate_label.grid(row=3,column=0)
cancelDate.grid(row=3,column=1,pady=20)

CancelReservation = partial(CancelReservation, acc, membershipID, cancelDate.get_date())

#button cancelreservation
cancelreservation_button = tk.Button(master=cancelreservation_page,text="Cancel Reservation",
                                     font=buttonFont,bg = "aquamarine",command = CancelReservation)
cancelreservation_button.grid(row=4,column=0,pady = 20)

#button back to reservation menu
back_button = tk.Button(master = cancelreservation_page,
                        text="Back to Reservations Menu",
                        font = buttonFont,
                        bg="aquamarine",
                        command=lambda:show_frame(reservations_page))
back_button.grid(row=4,column=1, pady = 20)

cancelreservation_page.columnconfigure(0, weight = 1)
cancelreservation_page.columnconfigure(1, weight = 1)
#===========================FINE PAYMENT PAGE===============#
#entry membershipID
#entry paymentDate
#entry amount
#button payfine
#button back to fines menu

#entry membershipID
#entry paymentDate
#entry amount
#button payfine
#button back to fines menu

membershipID = tk.StringVar()
amount = tk.StringVar()

def Success():
    top=tk.Toplevel(window)
    tk.Label(top,text="Success",font=alertFont).pack()
    tk.Label(top,text="Fines paid",font=messageFont).pack()
    tk.Button(top,text="OK",command=top.destroy).pack()

def Payfine(mem,pdate,amnt):
    def payfine():
        cursor = connection.cursor()
        sql = "INSERT into fines(MemID,PaymentDate,PaidAmount) value\
(%s,%s,%s)"
        cursor.execute(sql,(mem.get(),pdate.get_date(),amnt.get()))
        sql = "UPDATE members SET Fines = 0 WHERE MemID = %s"
        cursor.execute(sql,(mem.get()))
        connection.commit()
    conA=False
    conB=False
    
    cursor = connection.cursor()
    sql = "SELECT Fines FROM members WHERE MemID = %s"
    cursor.execute(sql,(mem.get()))
    row = cursor.fetchone()
    fine = 0
    if row:
        fine = row["Fines"]
    if fine == 0:
        conA = True
    if fine != int(amnt.get()):
        conB = True

    top = tk.Toplevel(window)
    top.geometry("400x300")
    if conA or conB:
        tk.Label(top,text="Error!",font=alertFont).pack()
        tk.Label(top,text="Member has no Fines or Payment is not Exact",font=messageFont).\
                                  pack()
        tk.Button(top,text="Go Back",command=top.destroy).pack()
    else:
        tk.Label(top,text="Please Confirm Details",font=alertFont).grid(row=0,column=0,\
                                                                        columnspan=2)
        tk.Label(top,text="Member ID",font=messageFont).grid(row=1,column=0)
        tk.Label(top,text=mem.get(),font=messageFont).grid(row=1,column=1)
        tk.Label(top,text="Payment Amount",font=messageFont).grid(row=2,column=0)
        tk.Label(top,text=amnt.get(),font=messageFont).grid(row=2,column=1)
        tk.Label(top,text="Payment Date",font=messageFont).grid(row=3,column=0)
        tk.Label(top,text=pdate.get_date(),font=messageFont).grid(row=3,column=1)
        tk.Button(top,text="Confirm Payment",command=lambda:[payfine(),top.destroy(),\
                                                             Success()]).\
                                    grid(row=4,column=0)
        tk.Button(top,text="Go Back",command=top.destroy).grid(row=4,column=1)
        
        top.columnconfigure(0, weight = 1)
        top.columnconfigure(1, weight = 1)
    

#Page Title    
text = tk.Label(master = finepayment_page,
                text = "For Pay a Fine, Please Enter Information Below:", 
                bg="light coral",
                font = titleFont)
text.grid(row=0,column=0,columnspan=2)

#entry membershipID
membershipID_entry = tk.Entry(master = finepayment_page, 
                              font = entryFont, textvariable = membershipID)
membershipID_label = tk.Label(master = finepayment_page,bg="light coral", text = "Membership ID",font=30)
membershipID_label.grid(row=1,column=0)
membershipID_entry.grid(row=1,column=1,pady=20)

#entry paymentDate
paymentDate = DateEntry(finepayment_page) 
                              
paymentDate_label = tk.Label(master = finepayment_page, text = "Payment Date",font=30,bg="light coral")
paymentDate_label.grid(row=2,column=0)
paymentDate.grid(row=2,column=1,pady=20)

#entry amount
amount_entry = tk.Entry(master = finepayment_page, 
                        font = entryFont, textvariable = amount)
amount_label = tk.Label(master = finepayment_page,bg="light coral", text = "Payment Amount",font=30)
amount_label.grid(row=3,column=0)
amount_entry.grid(row=3,column=1,pady=20)

Payfine = partial(Payfine,membershipID,paymentDate,amount)

#button payfine
payfine_button = tk.Button(master=finepayment_page,text="Pay Fine",
                           font=buttonFont,bg="aquamarine",command = Payfine)
payfine_button.grid(row=4,column=0,pady=20)

#button back to fines menu
back_button = tk.Button(master = finepayment_page,
                        text="Back to Fines Menu",
                        font = buttonFont,bg="aquamarine",
                        command=lambda:show_frame(fines_page))
back_button.grid(row=4,column=1)

finepayment_page.columnconfigure(0, weight = 1)
finepayment_page.columnconfigure(1, weight = 1)

#===========================BOOK SEARCH REPORT===============#
#entry title
#entry authors
#entry isbn
#entry publisher
#entry publication year
#button searchbook
#button back to reports menu

title_bsr = tk.StringVar()
authors_bsr = tk.StringVar()
isbn_bsr = tk.StringVar()
publisher_bsr = tk.StringVar()
publication_year_bsr = tk.StringVar()

def sqlBookSearch():
    BookSearch()

#Page Title    
text = tk.Label(master = booksearch_page,
                text = "Search based on one of the categories below:", 
                bg="light coral",
                font = titleFont)
text.grid(row=0,column=0,columnspan=2)

#entry title
title_entry = tk.Entry(master=booksearch_page,
                       font=entryFont,textvariable=title_bsr)
title_label = tk.Label(master = booksearch_page, text = "Title",font=30,bg="light coral")
title_label.grid(row=1,column=0)
title_entry.grid(row=1,column=1,pady=20)

#entry authors
authors_entry = tk.Entry(master=booksearch_page,
                       font=entryFont,textvariable=authors_bsr)
authors_label = tk.Label(master = booksearch_page, text = "Authors",font=30,bg="light coral")
authors_label.grid(row=2,column=0)
authors_entry.grid(row=2,column=1,pady=20)

#entry isbn
isbn_entry = tk.Entry(master=booksearch_page,
                       font=entryFont,textvariable=isbn_bsr)
isbn_label = tk.Label(master = booksearch_page, text = "ISBN",font=30,bg="light coral")
isbn_label.grid(row=3,column=0)
isbn_entry.grid(row=3,column=1,pady=20)

#entry publisher
publisher_entry = tk.Entry(master=booksearch_page,
                       font=entryFont,textvariable=publisher_bsr)
publisher_label = tk.Label(master = booksearch_page, text = "Publisher",font=30,bg="light coral")
publisher_label.grid(row=4,column=0)
publisher_entry.grid(row=4,column=1,pady=20)

#entry publication year
publication_entry = tk.Entry(master=booksearch_page,
                       font=entryFont,textvariable=publication_year_bsr)
publication_label = tk.Label(master = booksearch_page, text = "Publication Year",font=30,bg="light coral")
publication_label.grid(row=5,column=0)
publication_entry.grid(row=5,column=1,pady=20)

#button searchbook
searchbook_button = tk.Button(master=booksearch_page,text="Search Book",
                           font=buttonFont,bg="aquamarine",command = lambda:ActionBSR(title_bsr.get(),authors_bsr.get(),isbn_bsr.get(),publisher_bsr.get(),publication_year_bsr.get()))
searchbook_button.grid(row=6,column=0,pady=20)

#button back to reports menu
back_button = tk.Button(master = booksearch_page,
                        text="Back to Reports Menu",
                        font = buttonFont, bg ="aquamarine",
                        command=lambda:show_frame(report_page))
back_button.grid(row=6,column=1)

booksearch_page.columnconfigure(0, weight = 1)
booksearch_page.columnconfigure(1, weight = 1)

#=======================BOOKS SEARCH RESULTS REPORT=====================#

def sqlDisplayLoans():
    DisplayLoans()

#Page Title    
text = tk.Label(master = booksearch_results_page,
                text = "Book Search Report", 
                bg="light coral",
                font = titleFont)
text.pack()

#Treeview
bsr_scroll = ttk.Scrollbar(master = booksearch_results_page)
bsr_scroll.pack(side=RIGHT,fill=Y)

bsr_tree = ttk.Treeview(master = booksearch_results_page, yscrollcommand = bsr_scroll.set)
bsr_scroll.config(command = bsr_tree.yview)

bsr_tree["show"] = "headings"
bsr_tree["columns"] = ("Accession Number", "Title", "Authors", "ISBN", "Publisher", "Year")
s = ttk.Style(master = booksearch_results_page)
s.theme_use("clam")

bsr_tree.column('Accession Number', width = 200, minwidth= 50, anchor = CENTER)
bsr_tree.column('Title', width = 200, minwidth= 50, anchor = CENTER)
bsr_tree.column('Authors', width = 200, minwidth= 50, anchor = CENTER)
bsr_tree.column('ISBN', width = 150, minwidth= 50, anchor = CENTER)
bsr_tree.column('Publisher', width = 150, minwidth= 50, anchor = CENTER)
bsr_tree.column('Year', width = 150, minwidth= 50, anchor = CENTER)

bsr_tree.heading('Accession Number', text = 'Accession Number', anchor = CENTER)
bsr_tree.heading('Title', text = 'Title', anchor = CENTER)
bsr_tree.heading('Authors', text = 'Authors', anchor = CENTER)
bsr_tree.heading('ISBN', text = 'ISBN', anchor = CENTER)
bsr_tree.heading('Publisher', text = 'Publisher', anchor = CENTER)
bsr_tree.heading('Year', text = 'Year', anchor = CENTER)
bsr_tree.pack(expand=True,fill="both")

bsr_test = [
    ["A123","Diary Of wimpy Kid", "LOL", '11233', 'Popular','2001'],
    ["D575","Harry Potter", "jk Rowling", '11233', 'wtv','2301'],
    ["D575","Harry Potter", "jk Rowling", '11233', 'wtv','2301'],
    ["D575","Harry Potter", "jk Rowling", '11233', 'wtv','2301'],
    ["D575","Harry Potter", "jk Rowling", '11233', 'wtv','2301'],
    ["D575","Harry Potter", "jk Rowling", '11233', 'wtv','2301'],
    ["D575","Harry Potter", "jk Rowling", '11233', 'wtv','2301'],
    ["D575","Harry Potter", "jk Rowling", '11233', 'wtv','2301'],
    ["D575","Harry Potter", "jk Rowling", '11233', 'wtv','2301'],
    ["D575","Harry Potter", "jk Rowling", '11233', 'wtv','2301'],
    ["D575","Harry Potter", "jk Rowling", '11233', 'wtv','2301'],
    ["D575","Harry Potter", "jk Rowling", '11233', 'wtv','2301'],
    ["D075","Harry Potter", "jk Rowling", '11233', 'wtv','2301']
]

table_bsr = []

def BookSearch(title,author,isbn,publisher,publicationyr):
    cursor = connection.cursor()
    sql = "SELECT * FROM books WHERE Title = %s OR Authors = %s OR ISBN = %s OR Publisher = %s or PublicationYear = %s"
    cursor.execute(sql,(title,author,isbn,publisher,publicationyr))
    rows = cursor.fetchall()
    table = []
    for row in rows:
        table.append((row["Accession"], row["Title"], \
                      row["Authors"], row["ISBN"], \
                      row["Publisher"], row["PublicationYear"]))
    return table

def ActionBSR(title,author,isbn,publisher,publication_year):
    for item in bsr_tree.get_children():
        bsr_tree.delete(item)
    table_bsr = BookSearch(title,author,isbn,publisher,publication_year)
    for i in table_bsr:
        bsr_tree.insert(parent = '', index = 'end', text = '', values = i)
    show_frame(booksearch_results_page)

#button back to reports menu
back_button = tk.Button(master = booksearch_results_page,
                        text="Back to Search Function",
                        font = buttonFont,bg="aquamarine",
                        command=lambda:show_frame(booksearch_page))
back_button.pack()

#=======================BOOKS ON LOAN REPORT=====================#

def sqlDisplayLoans():
    DisplayLoans()

#Page Title    
text = tk.Label(master = onloans_page,
                text = "Books on Loan Report", 
                bg="light coral",
                font = titleFont)
text.pack()

#Treeview
loans_scroll = ttk.Scrollbar(master = onloans_page)
loans_scroll.pack(side=RIGHT,fill=Y)

loans_tree = ttk.Treeview(master = onloans_page, yscrollcommand = loans_scroll.set)
loans_scroll.config(command = loans_tree.yview)

loans_tree["show"] = "headings"
loans_tree["columns"] = ("Accession Number", "Title", "Authors", "ISBN", "Publisher", "Year")
s = ttk.Style(master = onloans_page)
s.theme_use("clam")

loans_tree.column('Accession Number', width = 200, minwidth= 50, anchor = CENTER)
loans_tree.column('Title', width = 200, minwidth= 50, anchor = CENTER)
loans_tree.column('Authors', width = 200, minwidth= 50, anchor = CENTER)
loans_tree.column('ISBN', width = 150, minwidth= 50, anchor = CENTER)
loans_tree.column('Publisher', width = 150, minwidth= 50, anchor = CENTER)
loans_tree.column('Year', width = 150, minwidth= 50, anchor = CENTER)

loans_tree.heading('Accession Number', text = 'Accession Number', anchor = CENTER)
loans_tree.heading('Title', text = 'Title', anchor = CENTER)
loans_tree.heading('Authors', text = 'Authors', anchor = CENTER)
loans_tree.heading('ISBN', text = 'ISBN', anchor = CENTER)
loans_tree.heading('Publisher', text = 'Publisher', anchor = CENTER)
loans_tree.heading('Year', text = 'Year', anchor = CENTER)
loans_tree.pack(expand=True,fill="both")

loans_test = [
    ["A123","Diary Of wimpy Kid", "LOL", '11233', 'Popular','2001'],
    ["D575","Harry Potter", "jk Rowling", '11233', 'wtv','2301'],
    ["D575","Harry Potter", "jk Rowling", '11233', 'wtv','2301'],
    ["D575","Harry Potter", "jk Rowling", '11233', 'wtv','2301'],
    ["D575","Harry Potter", "jk Rowling", '11233', 'wtv','2301'],
    ["D575","Harry Potter", "jk Rowling", '11233', 'wtv','2301'],
    ["D575","Harry Potter", "jk Rowling", '11233', 'wtv','2301'],
    ["D575","Harry Potter", "jk Rowling", '11233', 'wtv','2301'],
    ["D575","Harry Potter", "jk Rowling", '11233', 'wtv','2301'],
    ["D575","Harry Potter", "jk Rowling", '11233', 'wtv','2301'],
    ["D575","Harry Potter", "jk Rowling", '11233', 'wtv','2301'],
    ["D575","Harry Potter", "jk Rowling", '11233', 'wtv','2301'],
    ["D075","Harry Potter", "jk Rowling", '11233', 'wtv','2301']
]

table_loans = []

def DisplayAllBooksOnLoans():
    cursor = connection.cursor()
    #Find null return date then reference book
    sql = "SELECT * FROM books WHERE Accession in \
(SELECT Accession from loans where ReturnDate is null)"
    cursor.execute(sql)
    rows = cursor.fetchall()
    table = []
    for row in rows:
        table.append((row["Accession"], row["Title"], \
                      row["Authors"], row["ISBN"], \
                      row["Publisher"], row["PublicationYear"]))
    return table

def ActionDL():
    for item in loans_tree.get_children():
        loans_tree.delete(item)
    table_loans = DisplayAllBooksOnLoans()
    for i in table_loans:
        loans_tree.insert(parent = '', index = 'end', text = '', values = i)
    show_frame(onloans_page)
    
#button back to reports menu
back_button = tk.Button(master = onloans_page,
                        text="Back to Reports Menu",
                        font = buttonFont,bg="aquamarine",
                        command=lambda:show_frame(report_page))
back_button.pack()

#=======================BOOKS ON RESERVATION REPORT=====================#

def sqlDisplayReservation():
    DisplayReservation()

#Page Title    
text = tk.Label(master = onreservation_page,
                text = "Books on Reservation Report", 
                bg="light coral",
                font = titleFont)
text.pack()

#Treeview
reservations_scroll = ttk.Scrollbar(master = onreservation_page)
reservations_scroll.pack(side=RIGHT,fill=Y)

reservations_tree = ttk.Treeview(master = onreservation_page, yscrollcommand = reservations_scroll.set)
reservations_scroll.config(command = reservations_tree.yview)

reservations_tree["show"] = "headings"
reservations_tree["columns"] = ("Accession Number", "Title", "Membership ID", "Name")
s = ttk.Style(master = onreservation_page)
s.theme_use("clam")

reservations_tree.column('Accession Number', width = 250, minwidth= 50, anchor = CENTER)
reservations_tree.column('Title', width = 250, minwidth= 50, anchor = CENTER)
reservations_tree.column('Membership ID', width = 250, minwidth= 50, anchor = CENTER)
reservations_tree.column('Name', width = 250, minwidth= 50, anchor = CENTER)

reservations_tree.heading('Accession Number', text = 'Accession Number', anchor = CENTER)
reservations_tree.heading('Title', text = 'Title', anchor = CENTER)
reservations_tree.heading('Membership ID', text = 'Membership ID', anchor = CENTER)
reservations_tree.heading('Name', text = 'Name', anchor = CENTER)
reservations_tree.pack(expand=True,fill="both")

reservations_test = [
    ["Test","Diary Of wimpy Kid", "LOL", '11233'],
    ["TEst","Harry", "jkd aodkasRowling", '11233'],
    ["TEsgd","Potter", "Rowling", '11233'],
    ["TEsy","Harry Potter", "jk Rowling", '11233']
]

table_reserve = []

def DisplayBooksonReservation():
    cursor = connection.cursor()
    sql = "SELECT Accession, MemID FROM reservations"
    cursor.execute(sql)
    rows = cursor.fetchall()
    table = []
    for row in rows:
        sql = "SELECT Title FROM books WHERE Accession = %s"
        cursor.execute(sql,(row["Accession"]))
        title = cursor.fetchone()

        sql = "SELECT Name FROM members WHERE MemID = %s"
        cursor.execute(sql,(row["MemID"]))
        name = cursor.fetchone()

        table.append((row["Accession"], title["Title"], row["MemID"], name["Name"]))
    return table

def ActionDBR():
    for item in reservations_tree.get_children():
        reservations_tree.delete(item)
    table_reserve = DisplayBooksonReservation()
    for i in table_reserve:
        reservations_tree.insert(parent = '', index = 'end', text = '', values = i)
    show_frame(onreservation_page)

#button back to reports menu
back_button = tk.Button(master = onreservation_page,
                        text="Back to Reports Menu",
                        font = buttonFont,bg="aquamarine",
                        command=lambda:show_frame(report_page))
back_button.pack()

#=======================MEMBERS WITH OUTSTANDING FINES REPORT=====================#

def sqlDisplayOutstandingFines():
    DisplayOutstandingFines()

#Page Title    
text = tk.Label(master = oustandingfines_page,
                text = "Members with Outstanding Fines", 
                bg="light coral",
                font = titleFont)
text.pack()

#Treeview
outstandingfines_scroll = ttk.Scrollbar(master = oustandingfines_page)
outstandingfines_scroll.pack(side=RIGHT,fill=Y)

outstandingfines_tree = ttk.Treeview(master = oustandingfines_page, yscrollcommand = outstandingfines_scroll.set)
outstandingfines_scroll.config(command = outstandingfines_tree.yview)

outstandingfines_tree["show"] = "headings"
outstandingfines_tree["columns"] = ("Membership ID", "Name", "Faculty", "Phone Number", "Email Address")
s = ttk.Style(master = oustandingfines_page)
s.theme_use("clam")

outstandingfines_tree.column('Membership ID', width = 200, minwidth= 50, anchor = CENTER)
outstandingfines_tree.column('Name', width = 200, minwidth= 50, anchor = CENTER)
outstandingfines_tree.column('Faculty', width = 200, minwidth= 50, anchor = CENTER)
outstandingfines_tree.column('Phone Number', width = 150, minwidth= 50, anchor = CENTER)
outstandingfines_tree.column('Email Address', width = 200, minwidth= 50, anchor = CENTER)

outstandingfines_tree.heading('Membership ID', text = 'Membership ID', anchor = CENTER)
outstandingfines_tree.heading('Name', text = 'Name', anchor = CENTER)
outstandingfines_tree.heading('Faculty', text = 'Faculty', anchor = CENTER)
outstandingfines_tree.heading('Phone Number', text = 'Phone Number', anchor = CENTER)
outstandingfines_tree.heading('Email Address', text = 'Email Address', anchor = CENTER)
outstandingfines_tree.pack(expand=True,fill="both")

outstandingfines_test = [
    ["Test","???", "LOL", '11233','test'],
    ["55555","Harry", "fah", '11233', 'test'],
    ["987689","Potter", "Rowling", '11233', 'test'],
    ["TEsy","Harry Potter", "jk Rowling", '11233', 'test']
]

table_outstandingfines = []

def DisplayMembersWithFines():
    cursor = connection.cursor()
    sql = "SELECT MemID, Name, Faculty, Number, Email FROM members where Fines > 0"
    cursor.execute(sql)
    rows = cursor.fetchall()
    table = []
    for row in rows:
        table.append((row["MemID"], row["Name"], row["Faculty"], row["Number"], row["Email"]))
    return table

def ActionDMWF():
    for item in outstandingfines_tree.get_children():
        outstandingfines_tree.delete(item)
    table_outstandingfines = DisplayMembersWithFines()
    for i in table_outstandingfines:
        outstandingfines_tree.insert(parent = '', index = 'end', text = '', values = i)
    show_frame(oustandingfines_page)

#button back to reports menu
back_button = tk.Button(master = oustandingfines_page,
                        text="Back to Reports Menu",
                        font = buttonFont, bg= "aquamarine",
                        command=lambda:show_frame(report_page))
back_button.pack()

#=======================DISPLAY BOOK ON LOAN TO MEMBER REPORT=====================#
#entry membershipID
#button searchmember
#button back to reports menu

membershipID_bol = tk.StringVar()

def sqlDisplayLoansByMember():
    DisplayLoansByMember()

#Page Title    
text = tk.Label(master = onloanbymember_page,
                text = "Books on Loan to Member", 
                bg="light coral",
                font = titleFont)
text.grid(row=0,column=0,columnspan=2)

#entry membershipID
membershipID_entry = tk.Entry(master = onloanbymember_page, 
                              font = entryFont, textvariable = membershipID_bol)
membershipID_label = tk.Label(master = onloanbymember_page, text = "Membership ID",font=30,bg="light coral")
membershipID_label.grid(row=1,column=0)
membershipID_entry.grid(row=1,column=1,pady=20)

#button searchmember
searchmember_button = tk.Button(master=onloanbymember_page,text="Search Member",
                           font=buttonFont,bg="aquamarine",command = lambda:ActionBOL(membershipID_bol.get()))
searchmember_button.grid(row=2,column=0,pady=20)

#button back to reports menu
back_button = tk.Button(master = onloanbymember_page,
                        text="Back to Reports Menu",
                        font = buttonFont,bg="aquamarine",
                        command=lambda:show_frame(report_page))
back_button.grid(row=2,column=1,pady=20)

onloanbymember_page.columnconfigure(0, weight = 1)
onloanbymember_page.columnconfigure(1, weight = 1)

#=======================DISPLAY BOOK ON LOAN (RESULT) TO MEMBER REPORT=====================#

#Page Title    
text = tk.Label(master = onloanbymember_results_page,
                text = "Books on Loan to Member", 
                bg="light coral",
                font = titleFont)
text.pack()

#Treeview
bol_scroll = ttk.Scrollbar(master = onloanbymember_results_page)
bol_scroll.pack(side=RIGHT,fill=Y)

bol_tree = ttk.Treeview(master = onloanbymember_results_page, yscrollcommand = bol_scroll.set)
bol_scroll.config(command = bol_tree.yview)

bol_tree["show"] = "headings"
bol_tree["columns"] = ("Accession Number", "Title", "Authors", "ISBN", "Publisher", "Year")
s = ttk.Style(master = onloanbymember_results_page)
s.theme_use("clam")

bol_tree.column('Accession Number', width = 200, minwidth= 50, anchor = CENTER)
bol_tree.column('Title', width = 200, minwidth= 50, anchor = CENTER)
bol_tree.column('Authors', width = 200, minwidth= 50, anchor = CENTER)
bol_tree.column('ISBN', width = 150, minwidth= 50, anchor = CENTER)
bol_tree.column('Publisher', width = 150, minwidth= 50, anchor = CENTER)
bol_tree.column('Year', width = 150, minwidth= 50, anchor = CENTER)

bol_tree.heading('Accession Number', text = 'Accession Number', anchor = CENTER)
bol_tree.heading('Title', text = 'Title', anchor = CENTER)
bol_tree.heading('Authors', text = 'Authors', anchor = CENTER)
bol_tree.heading('ISBN', text = 'ISBN', anchor = CENTER)
bol_tree.heading('Publisher', text = 'Publisher', anchor = CENTER)
bol_tree.heading('Year', text = 'Year', anchor = CENTER)
bol_tree.pack(expand=True,fill="both")

bol_test = [
    ["A123","Diary Of wimpy Kid", "LOL", '11233', 'Popular','2001'],
    ["D575","Harry Potter", "jk Rowling", '11233', 'wtv','2301'],
    ["D575","Harry Potter", "jk Rowling", '11233', 'wtv','2301'],
    ["D575","Harry Potter", "jk Rowling", '11233', 'wtv','2301'],
    ["D575","Harry Potter", "jk Rowling", '11233', 'wtv','2301'],
    ["D575","Harry Potter", "jk Rowling", '11233', 'wtv','2301'],
    ["D575","Harry Potter", "jk Rowling", '11233', 'wtv','2301'],
    ["D575","Harry Potter", "jk Rowling", '11233', 'wtv','2301'],
    ["D575","Harry Potter", "jk Rowling", '11233', 'wtv','2301'],
    ["D575","Harry Potter", "jk Rowling", '11233', 'wtv','2301'],
    ["D575","Harry Potter", "jk Rowling", '11233', 'wtv','2301'],
    ["D575","Harry Potter", "jk Rowling", '11233', 'wtv','2301'],
    ["D075","Harry Potter", "jk Rowling", '11233', 'wtv','2301']
]

table_bol = []

def DisplayLoansByMember(MemID):
    cursor = connection.cursor()
    sql = "SELECT * FROM books where Accession in(SELECT Accession from \
loans where MemID = %s and ReturnDate is null)"
    cursor.execute(sql, (MemID))
    rows = cursor.fetchall()
    table = []
    if len(rows)> 0:
        for row in rows:
            table.append((row["Accession"], \
                          row["Title"], \
                          row["Authors"], row["ISBN"], \
                          row["Publisher"], row["PublicationYear"]))
    return table 

def ActionBOL(MemID):
    for item in bol_tree.get_children():
        bol_tree.delete(item)
    table_bol = DisplayLoansByMember(MemID)
    for i in table_bol:
        bol_tree.insert(parent = '', index = 'end', text = '', values = i)
    show_frame(onloanbymember_results_page)

#button back to reports menu
back_button = tk.Button(master = onloanbymember_results_page,
                        text="Back to Search Function",
                        font = buttonFont,bg="aquamarine",
                        command=lambda:show_frame(onloanbymember_page))
back_button.pack()

#========================================================================================

show_frame(start_page)
window.mainloop()

