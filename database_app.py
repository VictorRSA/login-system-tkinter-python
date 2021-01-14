
import pymysql.cursors
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

# Connect to the database
# try:
#localhost = "127.0.0.1 " is the ip address of the mysql database server

class MemberConnnect:
    def __init__(self,root):
        self.root = root
        blank_space = " "
        self.root.title(202 * blank_space + "MySQL Connector")
        self.root.geometry("1360x700+0+0") #+0+0 is the coordinate
        MemmberID = StringVar()
        FirstName = StringVar()
        Surname = StringVar()
        Address = StringVar()
        PoBox = StringVar()
        Gender = StringVar()
        Mtype = StringVar()
        Mobile =StringVar()
        Email =StringVar()
        Search = StringVar()
        MemIdBar =StringVar()
        #===================================================================================================================




        MainFrame = Frame(self.root,bd=10,width=1350,height=700,relief=RIDGE,bg="cadetblue")
        MainFrame.grid()

        TitleFrames = Frame(MainFrame,bd=10,width=1320,height=100,relief=RIDGE)
        TitleFrames.grid(row=0,column=0)

        TitleFrame = Frame(TitleFrames,bd=7,width=1320,height=100,relief=RIDGE)
        TitleFrame.grid(row=0,column=0)

        ButtonFrame = Frame(MainFrame,bd=7,width=1340,height=50,relief=RIDGE,bg="cadet blue")
        ButtonFrame.grid(row=1,column=0)

        SearchFrame = Frame(MainFrame,bd=5,width=1340,height=50,relief=RIDGE)
        SearchFrame.grid(row=2,column=0)

        MidFrame = Frame(MainFrame,bd=5,width=1340,height=500,relief=RIDGE)
        MidFrame.grid(row=3,column=0)

        LeftFrame = Frame(MidFrame,bd=10,width=1340,height=400,padx=2,relief=RIDGE,bg="Powder blue")
        LeftFrame.pack(side=LEFT,padx=5,pady=0)

        InnerLeftFrame = Frame(LeftFrame,bd=5,width=1350,height=700,padx=4,pady=4,relief=RIDGE,bg="cadetblue")
        InnerLeftFrame.pack(side=TOP,padx=10,pady=0)
    #===================================================================================================================
        self.labelTitle = Label(TitleFrame,font=("Arial",12,"bold"),text="MySql Connection" ,bd=7,bg="cadetblue")
        self.labelTitle.grid(row=0,column=0,pady=0)


    #===================================================================================================================
        self.labelMemberID = Label(InnerLeftFrame,font=("Arial",12,"bold"),text="Member ID" ,anchor="w",justify=LEFT)
        self.labelMemberID.grid(row=0,column=0,stikcy=W,padx=5)

        self.txtMemeberID = Entry(InnerLeftFrame,font=("Arial",12,"bold"),bd=5,width=35,justify="left",textvariable=MemmberID)
        self.txtMemeberID.grid(row=0,column=1)

        self.labelFirstName = Label(InnerLeftFrame,font=("Arial",12,"bold"),text="FirstName",bd=7,anchor="w",justify=LEFT)
        self.labelFirstName.grid(row=1,column=0,sticky=W,padx=5)

        self.txtFirstName = Entry(InnerLeftFrame,font=("Arial",12,"bold"),text="FirstName",bd=7,textvariable=FirstName,justify=LEFT)
        self.txtFirstName.grid(row=2,column=0)

        self.LabelSurname =Label(InnerLeftFrame,font=("Arial",12,"bold"),text="Surname",bd=7,justify=LEFT)
        self.LabelSurname.grid(row=3,column=0,sticky=W,padx=5)

        self.txtSurname = Entry(InnerLeftFrame,font=("Arial",12,"bold"),bd=5,width=35,justify="left",textvariable=Surname)
        self.txtSurname.grid(row=4,column=1)


        self.LabelAddress = Label(InnerLeftFrame,font=("Arial",12,"bold"),text="Address",bd=7,justify=LEFT)
        self.LabelAddress.grid()
        self.txtAddress = Entry(InnerLeftFrame,font=("Arial",12,"bold"),text="FirstName",bd=7,textvariable=FirstName,justify=LEFT)
        self.txtAddress.grid(row=2,column=0)


        self.txtFirstName = Entry(InnerLeftFrame,font=("Arial",12,"bold"),text="FirstName",bd=7,textvariable=FirstName,justify=LEFT)
        self.txtFirstName.grid(row=2,column=0)

        self.txtFirstName = Entry(InnerLeftFrame,font=("Arial",12,"bold"),text="FirstName",bd=7,textvariable=FirstName,justify=LEFT)
        self.txtFirstName.grid(row=2,column=0)


        self.txtFirstName = Entry(InnerLeftFrame,font=("Arial",12,"bold"),text="FirstName",bd=7,textvariable=FirstName,justify=LEFT)
        self.txtFirstName.grid(row=2,column=0)

        s
        self.txtFirstName = Entry(InnerLeftFrame,font=("Arial",12,"bold"),text="FirstName",bd=7,textvariable=FirstName,justify=LEFT)
        self.txtFirstName.grid(row=2,column=0)


        self.txtFirstName = Entry(InnerLeftFrame,font=("Arial",12,"bold"),text="FirstName",bd=7,textvariable=FirstName,justify=LEFT)
        self.txtFirstName.grid(row=2,column=0)


        self.txtFirstName = Entry(InnerLeftFrame,font=("Arial",12,"bold"),text="FirstName",bd=7,textvariable=FirstName,justify=LEFT)
        self.txtFirstName.grid(row=2,column=0)


        self.txtFirstName = Entry(InnerLeftFrame,font=("Arial",12,"bold"),text="FirstName",bd=7,textvariable=FirstName,justify=LEFT)
        self.txtFirstName.grid(row=2,column=0)











    #===================================================================================================================


    #===================================================================================================================











if __name__ == '__main__':
    root = Tk()
    application = MemberConnnect(root)
    root.mainloop()
#
# connection = pymysql.connect(host='localhost',
#                              #I can use host ="127.0.0.1"
#                              user='root',
#                              password='',
#                              database='hospitals',
#                              charset='utf8mb4'
#
#                              )
#
#
#
# cursor=connection.cursor()
