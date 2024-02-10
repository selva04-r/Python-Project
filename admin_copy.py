from tkinter import *
from tkinter import ttk
import tkinter.messagebox as tmsg
import mysql.connector as mm
import time as ti
import os
import pickle
import random as rd
import csv
from datetime import date
import holidays

def login():
     global login_screen   
     login_screen = Toplevel()
     login_screen.geometry("1350x700+0+0")
     login_screen.title("Login window")

     photo1 = PhotoImage(file="loginwindow.png")
     Label(login_screen,image=photo1).pack()

     Label(login_screen, text="Please enter details below to login", font=("Copperplate Gothic Bold",25),fg='white',width=45,bg="green").place(x=0,y=30)

     photo2 = PhotoImage(file="icon.png")

     Label(login_screen,image=photo2).place(x=100,y=175)

     global username_verify,password_verify,Category

     username_verify.set('')
     password_verify.set('')
     Category.set('')

     Label(login_screen,text="Select Type", width=10,font=("Forte", 25),fg='white',bg="black").place(x=530,y=130)

     Category = StringVar()
     menu_category = ['Admin','Customer']
     ttk.Combobox(login_screen,values=menu_category,font=("Eras Bold ITC",20),
                                 textvariable=Category).place(x=800,y=130)

     Label(login_screen,text="Username", font=("Forte",25),fg='white',bg="black",width=10).place(x=530,y=220)
     Label(login_screen, text="Password", font=("Forte",25),fg='white',bg="black",width=10).place(x=530,y=310)
     Entry(login_screen, textvariable=username_verify, width=20,bd=10,relief=FLAT,font=("Eras Bold ITC",20)).place(x=800,y=210)
     Entry(login_screen, textvariable=password_verify, width=20,show = '*',bd=10,relief=FLAT,font=("Eras Bold ITC",20)).place(x=800,y=300)
     
     photo_back= PhotoImage(file="back.png")
     Button(login_screen, image=photo_back, font=("Showcard Gothic",20),fg='black',command = login_screen.destroy).place(x=10,y=20)
     
     photo_login = PhotoImage(file="login.png")
     Button(login_screen, image=photo_login, bd=2,relief=FLAT,font=("Forte",30),bg='red',command = admin_login_verify).place(x=800,y=420)
     login_screen.transient(main_screen)
     login_screen.mainloop()
   
def register():
     global register_screen
     register_screen = Toplevel()
     register_screen.geometry("1350x700+0+0")
     register_screen.title("Register window")
     photo = PhotoImage(file="registerscreen.png")
     Label(register_screen,image=photo).pack()

     global username,password,password_confirm,phone_nos,name

     username.set('')
     password.set('')
     password_confirm.set('')
     phone_nos.set('')
     name.set('')

     #category
     Label(register_screen, font=("Algerian",22),bg="black",fg="white",text="Customer").place(x=890,y=90)

     Label(register_screen, text="Please enter details below to register",font=("Copperplate Gothic Bold",25),fg='white',width=45,bg="green").place(x=0,y=20)
     Label(register_screen, font=("Forte",20),bg="black",fg="white",text="Name ::").place(x=600,y=165)
     Label(register_screen, font=("Forte",20),bg="black",fg="white",text="Username ::").place(x=600,y=245)
     Label(register_screen, font=("Forte",20),bg="black",fg="white",text="Password ::").place(x=600,y=325)
     Label(register_screen, font=("Forte",20),bg="black",fg="white",text="Confirm Password ::").place(x=600,y=405)
     Label(register_screen, font=("Forte",20),bg="black",fg="white",text="Phone number ::").place(x=600,y=485)
     photo_back= PhotoImage(file="back.png")
     Button(register_screen, image=photo_back, font=("Showcard Gothic",20),fg='black',command = register_screen.destroy).place(x=10,y=15)
     Entry(register_screen,width=20,bd=10,relief=FLAT, font=("Eras Bold ITC",18) ,textvariable=name).place(x=885,y=160)
     Entry(register_screen,width=20,bd=10,relief=FLAT, font=("Eras Bold ITC",18) ,textvariable=username).place(x=885,y=240)
     Entry(register_screen,width=20, bd=10,relief=FLAT,font=("Eras Bold ITC",18) ,show = '*',textvariable=password).place(x=885,y=320)
     Entry(register_screen,width=20,bd=10,relief=FLAT, font=("Eras Bold ITC",18) ,show = '*',textvariable=password_confirm).place(x=885,y=400)
     Entry(register_screen,width=20,bd=10,relief=FLAT, font=("Eras Bold ITC",18) ,textvariable=phone_nos).place(x=885,y=480)

     Button(register_screen, text="Register", bd=6,relief=FLAT,font=("Forte",25),fg='black',bg="yellow",command = register_user).place(x=720,y=600)
     Button(register_screen, text="Login here >>", bd=6,relief=FLAT,font=("Forte",25),fg='yellow',bg="blue",command = login).place(x=1020,y=600)

     frame = Frame(register_screen,highlightbackground="red",highlightthickness=6,bg='black')
     frame.place(x=80,y=100,width=460,height=430)

     Label(frame,text="Rules for password",font=("Arial Rounded MT Bold",25)).place(x=60,y=20)
     Label(frame,text="1. At least 8 characters - the more \ncharacters, the better.  ",fg='white',bg='black', font=("Segoe UI Semibold",20,"bold")).place(x=0,y=90)
     Label(frame,text="2. A mixture of both uppercase and \nlowercase letters.", fg='white',bg='black',font=("Segoe UI Semibold",20,"bold")).place(x=0,y=178)
     Label(frame,text="3. A mixture of letters and numbers.",fg='white',bg='black', font=("Segoe UI Semibold",20,"bold")).place(x=0,y=266)
     Label(frame,text="4. Inclusion of atleast one special \ncharacter, eg., ! @ # ? [ ] ", fg='white',bg='black',font=("Segoe UI Semibold",20,"bold")).place(x=0,y=316)

     # To remove the minimize and maximize button
     register_screen.transient(main_screen)
     #To close the window 
     register_screen.mainloop()
    
def admin_login_verify():
     username1 = username_verify.get()
     password1 = password_verify.get()
     category = Category.get()

     if len(username1)==0 and len(password1)==0:
          tmsg.showwarning('Warning','Please enter the details',parent=login_screen)

     elif len(username1)!=0 and len(password1)==0:
          tmsg.showwarning('Warning','Please enter the password',parent=login_screen)

     elif len(username1)==0 and len(password1)!=0:
          tmsg.showwarning('Warning','Please enter the username',parent=login_screen)

     else:
          if category == 'Admin':
             for i in admin_details:
                 if i[0] == username1:
                     if i[-1] == password1:
                         info = 'Welcome admin - ' + i[1]
                         tmsg.showinfo('Welcome',info,parent=login_screen)
                         login_screen.destroy()
                         first_page()
                         break
                     else:
                         tmsg.showwarning('Warning','Invalid Password',parent=login_screen)
                         username_verify.set('')
                         password_verify.set('')
                         Category.set('')
                         break
             else:
                tmsg.showwarning('Warning','User not found',parent=login_screen)
                username_verify.set('')
                password_verify.set('')
                Category.set('')
                    

          else:
               list_of_files = os.listdir()
               file = username1 + '.txt'
               if file in list_of_files:
                    f=open(file ,'rb')
                    while True:
                         try:
                              d=pickle.load(f)
                              for i in d:
                                   if d['Username'] == username1:
                                        if d['Password'] == password1 :
                                             info = 'Welcome - ' + d['Name']
                                             tmsg.showinfo('Welcome',info,parent=login_screen)
                                             temp(d['Name'],d['Phone_number'])
                                             mydb = mm.connect(host="localhost",user="root",passwd="selva",database='hotel')
                                             c = mydb.cursor()
                                             c.execute('select * from t1')
                                             l = c.fetchall()
                                             mydb.close()
                                             
                                             #discount
                                             discount(l,d)
                                             main_screen.destroy()
                                             import billing_page
                                             
                                             break
                                        else:
                                             tmsg.showwarning('Warning','Invalid Password',parent=login_screen)
                                             username_verify.set('')
                                             password_verify.set('')
                                             Category.set('')
                                             break
                                   else:
                                       tmsg.showwarning('Warning','Choose the correct category',parent=login_screen)
                                       username_verify.set('')
                                       password_verify.set('')
                                       Category.set('')
                                       break
                                     
                         except:
     
                              break
                    f.close()
               else:
                    tmsg.showwarning('Warning','User not found',parent=login_screen)
                    username_verify.set('')
                    password_verify.set('')
                    Category.set('')
          
def discount(l,d):
    disc_days = []
    today = date.today()
    my_date = '14/01/2022' # today's date
    y = int(my_date.split('/')[-1])
    for a in holidays.India(years = y).items():
        disc_days += [[a[0],a[1]]]

    for k in disc_days:
        k[0] = k[0].strftime("%d/%m/%Y")# format change to dd/mm/yyyy
        if my_date == k[0]:
            for i in l:
                if  d['Phone_number'] == i[1] :
                    if float(i[-1])>5000.0:
                        f=open('discount.txt','w')
                       
                        if float(i[-1])>15000.0:
                            f.write(i[0]+'\n'+d['Phone_number'] +'\n'+ '5'+ '\n'+k[-1])
                            # customer name, phone number, discount percentage, festival name
                            f.close()
                            break

                        elif float(i[-1])>7000.0:
                            f.write(i[0]+'\n'+d['Phone_number'] +'\n'+ '3'+ '\n'+k[-1])
                            f.close()
                            break
                       
                        f.write(i[0]+'\n'+d['Phone_number'] +'\n'+ '2' + '\n'+k[-1])
                        f.close()
            break
                        
def register_user():

     username_info = username.get()
     password_info = password.get()
     password_confirm_info = password_confirm.get()
     phone_nos_info = phone_nos.get()
     name_info = name.get()

     file_name = username_info

     if len(username_info)==0 and len(password_info)==0 or len(username_info)==0 and len(name_info)==0 and len(password_confirm_info)==0 and str(phone_nos_info)=='0':
          tmsg.showwarning('Warning','Please enter the details',parent=register_screen)

     elif len(password_info)!=0  and len(username_info)==0 and len(password_confirm_info)!=0 and str(phone_nos_info)!='0' and str(name_info)==0:
          tmsg.showwarning('Warning','Please enter the name',parent=register_screen)

     elif len(password_info)!=0  and len(username_info)==0 and len(password_confirm_info)!=0 and str(phone_nos_info)!='0' and str(name_info)!=0:
          tmsg.showwarning('Warning','Please enter the username',parent=register_screen)

     elif len(password_info)==0  and len(username_info)!=0 and len(password_confirm_info)==0 and str(phone_nos_info)!='0' and str(name_info)!=0:
          tmsg.showwarning('Warning','Please enter the password',parent=register_screen)

     elif len(password_info)!=0  and len(username_info)!=0 and len(password_confirm_info)!=0 and str(phone_nos_info)=='0' and str(name_info)!=0:
          tmsg.showwarning('Warning','Please enter the phone number',parent=register_screen)

     elif len(str(phone_nos_info)) > 10 or len(str(phone_nos_info)) < 10 :
          tmsg.showwarning('Warning','Please enter a valid phone number',parent=register_screen)

     elif len(password_info)!=0  and len(username_info)!=0 and len(password_confirm_info)!=0 and len(str(phone_nos_info))==10:
          if len(password_info or password_confirm_info) >= 8 :
               if password_confirm_info!=password_info and len(username_info)!=0 and str(phone_nos_info)!='0':
                    tmsg.showwarning('Warning','Please enter the same password',parent=register_screen)

               elif os.path.exists(file_name + ".txt") :
                    f=open(file_name + ".txt","rb")
                    check = False
                    while True:
                         try:
                              d=pickle.load(f)
                              for i in d:
                                   if d['Username'] == username_info:
                                        if d['Password'] == password_info :
                                             check =True
                                             break
                         except:
                              break
                    f.close()
                    
                    if check :
                         tmsg.showinfo('Warning','Already registered, Please login !!',parent=register_screen)
                         username.set('')
                         password.set('')
                         password_confirm.set('')
                         phone_nos.set('')
                         name.set('')

                    else:
                         
                         f = open(file_name + ".txt","wb")
                         d={}
                         d['Name'] = name_info
                         d['Username'] = username_info
                         d['Password'] = password_info
                         d['Phone_number'] = phone_nos_info
                         pickle.dump(d,f)
                         f.close()                         
                         tmsg.showinfo('Registered','REGISTERED SUCCESSFULLY\nPLEASE LOGIN',parent=register_screen)
                         username.set('')
                         password.set('')
                         password_confirm.set('')
                         phone_nos.set('')
                         name.set('')

               else:
                    
                    f = open(file_name + ".txt","wb")
                    d={}
                    d['Name'] = name_info
                    d['Username'] = username_info
                    d['Password'] = password_info
                    d['Phone_number'] = phone_nos_info
                    pickle.dump(d,f)
                    f.close()
                    tmsg.showinfo('Registered','REGISTERED SUCCESSFULLY\nPLEASE LOGIN',parent=register_screen)
                    username.set('')
                    password.set('')
                    password_confirm.set('')
                    phone_nos.set('')
                    name.set('')
                    
          else:
              
               tmsg.showwarning('Warning','Password is weak',parent=register_screen)
               

def close():
     c = tmsg.askyesno('Warning','Do you want to exit',parent=main_screen)
     if c:
          main_screen.destroy()

def temp(n,ph):
    f=open('temp.txt','w')
    f.write(n+'\n'+str(ph))
    f.close()    


def load_staff_details():
     global staff_table
     mydb = mm.connect(host="localhost",user="root",passwd="selva",database='hotel')
     c = mydb.cursor()
     c.execute('select * from t1')
     l = c.fetchall()
     for i in l:
          staff_table.insert('',END,values=[i[0],i[-2],i[-1]])
     mydb.close()

def load_dis():
     global menu_tabel1
     mydb = mm.connect(host="localhost",user="root",passwd="selva",database='hotel')
     c = mydb.cursor()
     c.execute('select * from t2')
     l = c.fetchall()
     for i in l:
          menu_tabel1.insert('',END,values=[i[0],i[2],i[4],i[-1]])
     mydb.close()
    
def discount_details():
    global staff_frame,menu_tabel1
    for i in staff_frame.winfo_children():
      i.destroy()
    for i in button_list:
         i.config(state=DISABLED)

    dis_tabel_frame = Frame(staff_frame)
    dis_tabel_frame.place(x=0,y=0,height=400,width=950)
    Label(dis_tabel_frame,text="Discount Details", fg='yellow',height=2,bg="black",font=("Showcard Gothic",15,"bold")).pack(fill = X)

    scrollbar_menu_y = Scrollbar(dis_tabel_frame,orient=VERTICAL)

    menu_tabel1 = ttk.Treeview(dis_tabel_frame,columns =("name","total","dis",'date'),yscrollcommand=scrollbar_menu_y.set)

    style = ttk.Style()
    style.configure("Treeview.Heading",font=("Forte",13))
    style.configure("Treeview",font=("Baskerville Old Face",12,'bold'),rowheight=25)

    menu_tabel1["columns"]=("name","total","dis",'date') # columns
    menu_tabel1.column("#0",width=0,stretch=NO) # first column which is complusory 
    menu_tabel1.column("dis",width=50,anchor='center') # updating the column
    menu_tabel1.column("date",width=50,anchor='center')
    menu_tabel1.column("total",width=50,anchor='center') 
    menu_tabel1.column("name",width=50,anchor='center') 

    #heading
    menu_tabel1.heading("name",text="Name")
    menu_tabel1.heading("total",text="Total Price")
    menu_tabel1.heading("dis",text="Discount Amount")
    menu_tabel1.heading("date",text="Date")

    scrollbar_menu_y.pack(side=RIGHT,fill=Y)
    #configure the scrollbar
    scrollbar_menu_y.configure(command=menu_tabel1.yview)

    menu_tabel1.pack(fill=BOTH,expand=1)

    load_dis()
    
def comment_details():
    global staff_frame,comment_table
    for i in staff_frame.winfo_children():
      i.destroy()

    global Display1
    for i in button_list:
         i.config(state=DISABLED)

    comment_tabel_frame = Frame(staff_frame)
    comment_tabel_frame.place(x=0,y=0,height=400,width=950)
    Label(comment_tabel_frame,text="Comment Details", fg='yellow',height=2,bg="black",font=("Showcard Gothic",15,"bold")).pack(fill = X)

    scrollbar_menu_y = Scrollbar(comment_tabel_frame,orient=VERTICAL)
    comment_table = ttk.Treeview(comment_tabel_frame,columns =('dat',"name",'em','cc'),yscrollcommand=scrollbar_menu_y.set)

    comment_table["columns"]=('dat',"name",'em','cc') # columns
    comment_table.column("#0",width=0,stretch=NO) # first column which is complusory
    comment_table.column("dat",width=100,anchor='center') # updating the column
    comment_table.column("name",width=100,anchor='center') # updating the column
    comment_table.column("em",width=100,anchor='center') # updating the column
    #heading
    comment_table.heading("dat",text="Date")
    comment_table.heading("name",text="Customer name")
    comment_table.heading("em",text="Email")
    comment_table.heading("cc",text="Comment")
    
    display_details1 = Frame(staff_frame)
    display_details1.place(x=0,y=450,height=200,width=950)
    display_details1.config(background = 'lightyellow')
    scrollbar = Scrollbar(display_details1,orient=VERTICAL)
    Display1 = Text(display_details1,width=950,height=200,font=('arial', 16,'bold'), yscrollcommand=scrollbar.set,state='normal')
    Display1.insert(END,'\n\t\tDisplay Box')
    Display1.pack(side=LEFT,expand=1)
    scrollbar.configure(command=Display1.yview)
    scrollbar.pack(side=RIGHT,fill=Y)

    scrollbar_menu_y.configure(command=comment_table.yview)
    scrollbar_menu_y.pack(side=RIGHT,fill=Y)
    comment_table.bind("<ButtonRelease>",comment)
    load_comment()

    comment_table.pack(fill=BOTH,expand=1)

def comment(c):
    cursor_row = comment_table.focus() # get the index position of the values
    contents = comment_table.item(cursor_row) # get the values using the index position
    row = contents["values"]
    Display1.config(state='normal')
    Display1.delete('1.0',END)
    Display1.insert(END,'\n' + ' '*4 + 'Date ::  ' + str(row[0]))
    Display1.insert(END,'\n\n' + ' '*4 + 'Customer Name ::  ' + row[1])
    Display1.insert(END,'\n\n' + ' '*4 + 'Email ::  ' + row[2])
    message = ' '*4
    for i in row[-1].split('\n'):
         message = message+ '\n' +' '*4 +  i
    Display1.insert(END,'\n\n' + ' '*4 + 'Comment ::  \n' + message)
    Display1.config(state='disabled')

def load_comment():
     global comment_table
     mydb = mm.connect(host="localhost",user="root",passwd="selva",database='hotel')
     c = mydb.cursor()
     c.execute('select * from t3')
     l = c.fetchall()
     for i in l:
          comment_table.insert('',END,values=[i[0],i[1],i[2],i[-1]])
     mydb.close()


def Staff_details():
    global staff_frame,staff_table
    for i in staff_frame.winfo_children():
      i.destroy()

    global Display
    for i in button_list:
         i.config(state=DISABLED)
    staff_tabel_frame = Frame(staff_frame)
    staff_tabel_frame.place(x=0,y=0,height=400,width=950)
    Label(staff_tabel_frame,text="Customer Details", fg='yellow',height=2,bg="black",font=("Showcard Gothic",15,"bold")).pack(fill = X)

    scrollbar_menu_y = Scrollbar(staff_tabel_frame,orient=VERTICAL)
    staff_table = ttk.Treeview(staff_tabel_frame, columns =("name",'no','am'),yscrollcommand=scrollbar_menu_y.set)

    staff_table["columns"]=("name",'no','am') # columns
    staff_table.column("#0",width=0,stretch=NO) # first column which is complusory 
    staff_table.column("name",width=100,anchor='center') # updating the column
    staff_table.column("no",width=100,anchor='center') # updating the column
    staff_table.column('am',width=150,anchor='center') # updating the column
    #heading
    staff_table.heading("name",text="Customer name")
    staff_table.heading("no",text="No. of times purchased")
    staff_table.heading("am",text="Total Amount")
    
    display_details = Frame(staff_frame)
    display_details.place(x=0,y=450,height=200,width=950)
    display_details.config(background = 'lightyellow')
    Display = Text(display_details,width=950,height=200,font=('arial', 16,'bold'),state='normal')
    Display.insert(END,'Display Box')
    Display.pack(side=LEFT)
    
    scrollbar_menu_y.pack(side=RIGHT,fill=Y)
    #configure the scrollbar
    scrollbar_menu_y.configure(command=staff_table.yview)
    staff_table.bind("<ButtonRelease>",load_staff)
    load_staff_details()

    staff_table.pack(fill=BOTH,expand=1)
    
def load_staff(c):
    cursor_row = staff_table.focus() # get the index position of the values
    contents = staff_table.item(cursor_row) # get the values using the index position
    row = contents["values"]
    Display.config(state='normal')
    Display.delete('1.0',END)
    Display.insert(END,'\n  Customer Name ::  ' + row[0])
    Display.insert(END,'\n\n  No. of times purchased ::  ' + str(row[1]))
    Display.insert(END,'\n\n  Total amount purchased ::  ' + str(row[-1]))
    
    Display.config(state='disabled')

def load_menu1(menu_tabel): 
     for file in menu_category_dict: # opening all the files
          f = open(menu_category_dict[file] , "r")
          csvr = list(csv.reader(f))
          category="==================="+file
          menu_tabel.insert(parent='',index=END,values=['',category])
          for i in range(len(csvr)):
               menu_tabel.insert(parent='',index=END,values=[csvr[i][0],csvr[i][1],csvr[i][2],csvr[i][3],category])

          
def load_item(c): # any name
    global menu_tabel
    cursor_row = menu_tabel.focus() # get the index position of the values
    contents = menu_tabel.item(cursor_row,'values') # get the values using the index position

    global Name, Rate, Category, Quantity, Code
    if contents[1][0]=='=':
        Name.set('')
        Rate.set('')
        Category.set('')
        Quantity.set('')
        Code =''
    else:
        Name.set(contents[1])
        Rate.set(contents[2])
        Category.set(contents[-1][19:])
        Quantity.set(contents[3])
        Code =contents[0]
   

def first_page():
    first_page = Toplevel()
    first_page.geometry("1350x700+0+0")
    first_page.resizable(0,0) # Not allow to maximise the screen
    first_page.title("Admin Page")
    first_page.config(background = 'dark blue')


    def Update():
        global Category,Name,Rate,Quantity,Code
        file = Category.get()
        name = Name.get()
        rate = Rate.get()
        quantity = Quantity.get()
        f = open(menu_category_dict[file]  , "r")

        csvr = list(csv.reader(f))
        for i in csvr:
             if i[0] == Code:
                  i[1] = name
                  i[2] = rate
                  i[3] = quantity
        f.close()
        f = open(menu_category_dict[file]  , "w",newline='')
        csvw = csv.writer(f)
        csvw.writerows(csvr)
        f.close()
        tmsg.showinfo('Update','Successfully updated',parent=first_page)
        Food_details()
        
    def Add():
        global Category,Name,Rate,Quantity,Buttons
        file = Category.get()
        name = Name.get()
        rate = Rate.get()
        quantity = Quantity.get()

        try:
             f = open(menu_category_dict[file]  , "r")
             csvr = list(csv.reader(f))
             code = 'PH' + str(int(csvr[-1][0][2:]) + 1)
             f.close()
             csvr+=[[code,name,rate,quantity]]
             f = open(menu_category_dict[file]  , "w",newline='')
             csvw = csv.writer(f)
             csvw.writerows(csvr)
             f.close()
             tmsg.showinfo('Add','Successfully item added',parent=first_page)
             Food_details()
        except:
             tmsg.showinfo("Warning","You can't add new category",parent=Buttons)
             
                      
    def Delete():
        file = Category.get()
        name = Name.get()
        rate = Rate.get()
        quantity = Quantity.get()
        f = open(menu_category_dict[file]  , "r")

        csvr = list(csv.reader(f))
        for i in csvr:
             if i[0] == Code:
                  csvr.pop(csvr.index(i))
        f.close()
        f = open(menu_category_dict[file]  , "w",newline='')
        csvw = csv.writer(f)
        csvw.writerows(csvr)
        f.close()
        tmsg.showinfo('Deleted','Successfully item deleted',parent=first_page)
        Food_details()
        
    def Clear():
        global Category,Name,Rate,Quantity
        file = Category.set('')
        name = Name.set('')
        rate = Rate.set('')
        quantity = Quantity.set('')

    def logout():
         c = tmsg.askyesno('Warning','Do you want to logout ?',parent=first_page)
         if c:
              first_page.destroy()
        

    def Food_details():
        global Name, Rate, Category, Quantity,menu_tabel,staff_frame

        staff_frame = Frame(first_page)
        staff_frame.place(x=400,y=0,height=800,width=950)
        staff_frame.config(background = 'light yellow')
        for i in staff_frame.winfo_children():
            i.destroy()
        
        global Buttons
        Buttons = Frame(first_page)
        Buttons.place(x=0,y=0,height=750,width=400)
        
        Button(Buttons,text="Food details", font=("Copperplate Gothic Bold",15),bg='green',fg='white',command=Food_details).pack(anchor = 'center',fill=Y,pady=40)
        Button(Buttons,text="Customer details", font=("Copperplate Gothic Bold",15),bg='green',fg='white',command=Staff_details).pack(anchor = 'center',fill=Y,pady=20)
        Button(Buttons,text="Discount details", font=("Copperplate Gothic Bold",15),bg='green',fg='white',command=discount_details).pack(anchor = 'center',fill=Y,pady=20)
        Button(Buttons,text="Comment details", font=("Copperplate Gothic Bold",15),bg='green',fg='white',command=comment_details).pack(anchor = 'center',fill=Y,pady=20)
        add = Button(Buttons,text="Add", font=("Forte",15),bg='yellow',fg='blue',command=Add)
        add.pack(anchor = 'center',fill=Y,pady=20)
        dele = Button(Buttons,text="Delete", font=("Forte",15),bg='yellow',fg='blue',command=Delete)
        dele.pack(anchor = 'center',fill=Y,pady=20)
        upd = Button(Buttons,text="Update", font=("Forte",15),bg='yellow',fg='blue',command=Update)
        upd.pack(anchor = 'center',fill=Y,pady=20)
        global button_list
        button_list=[add,dele,upd]
        photo = PhotoImage(file="logout.png")
        Buttons.photo=photo
        Button(Buttons,image=photo,command=logout).pack(anchor = 'center',fill=Y,pady=20)

        menu_tabel_frame = Frame(staff_frame)
        menu_tabel_frame.place(x=0,y=0,height=400,width=950)
        Label(menu_tabel_frame,text="Food Details", fg='yellow',height=2,bg="black",font=("Showcard Gothic",15,"bold")).pack(fill = X)

        scrollbar_menu_y = Scrollbar(menu_tabel_frame,orient=VERTICAL)

        menu_tabel = ttk.Treeview(menu_tabel_frame,columns =("code","name","price",'stock'),yscrollcommand=scrollbar_menu_y.set)

        style = ttk.Style()
        style.configure("Treeview.Heading",font=("Forte",13))
        style.configure("Treeview",font=("Baskerville Old Face",12,'bold'),rowheight=25)

        menu_tabel["columns"]=('code',"name", "price",'stock') # columns
        menu_tabel.column("#0",width=0,stretch=NO) # first column which is complusory 
        menu_tabel.column("price",width=50,anchor='center') # updating the column
        menu_tabel.column("code",width=50,anchor='center')
        menu_tabel.column("stock",width=50,anchor='center') 
        #heading
        menu_tabel.heading("name",text="Name")
        menu_tabel.heading("price",text="Price")
        menu_tabel.heading("code",text="Code No.")
        menu_tabel.heading("stock",text="In Stock")

        scrollbar_menu_y.pack(side=RIGHT,fill=Y)
        #configure the scrollbar
        scrollbar_menu_y.configure(command=menu_tabel.yview)

        menu_tabel.pack(fill=BOTH,expand=1)
        # to choose a item from the menu table
        menu_tabel.bind("<ButtonRelease>",load_item)

        load_menu1(menu_tabel)

        #####################################################################
        global Category,Name,Rate,Quantity

        change_product_details = Frame(staff_frame)
        change_product_details.place(x=0,y=450,height=200,width=950)
        change_product_details.config(background = 'lightyellow')
        Category = StringVar()
        Label(change_product_details, text="Category", font=("Times new roman", 17, "bold"),bg = "lightyellow", fg="blue").grid(row=0,column=1,padx=40)
        category_ = Entry(change_product_details, font="arial 17",textvariable=Category,state=DISABLED,width=30).grid(row=0,column=2,padx=10,pady=10)

        Name = StringVar()
        Label(change_product_details, text="Name",font=("Times new roman", 17, "bold"),bg = "lightyellow", fg="blue").grid(row=1,column=1,padx=40)
        name_ = Entry(change_product_details, font="arial 17",textvariable=Name,width=25).grid(row=1,column=2,padx=10,pady=10)

        Rate = StringVar()
        Label(change_product_details, text="Rate",font=("Times new roman", 17, "bold"),bg = "lightyellow", fg="blue").grid(row=2,column=1,padx=40)
        rate_ = Entry(change_product_details, font="arial 17",textvariable=Rate,width=10).grid(row=2,column=2,padx=10,pady=10)

        Quantity = StringVar()
        Label(change_product_details, text="In Stock", font=("Times new roman", 17, "bold"),bg = "lightyellow", fg="blue").grid(row=3,column=1,padx=30,pady=15)
        quantity_ = Entry(change_product_details, font="arial 17",textvariable=Quantity,width=10).grid(row=3,column=2,padx=10,pady=10)

        Button(change_product_details,font="Broadway 17",text="Clear",command = Clear).grid(row=3,column=3,padx=10,pady=10)


    Food_details()

########################################################################
# MAIN SEGMENT #


#==========================================
# to determine whether the category is there in the list AND
# to display in the category list
menu_category = ["Beverages", "Fast Food", "South Indian", "Snacks", "Main Course", "Dessert"]

# to open the file 
menu_category_dict = {"Beverages":"Beverages.csv",
                "Fast Food":"Fast Food.csv","South Indian":"South Indian.csv",
                "Snacks":"Snacks.csv","Main Course":"Main Course.csv",
                "Dessert":"Dessert.csv"}
order_dict = {}
for i in menu_category:
    order_dict[i] = {}

#Admin
admin_details = [['sel@a','sel','sel123.456'],['a','arun','a'],['shrikumar@gmail.com','shrikumar','shrikumar456']]

          
#===============================================
 
main_screen = Tk()
main_screen.geometry("1350x700+0+0")
main_screen.resizable(0,0) # Not allow to maximise the screen
main_screen.title("Main page")
photo = PhotoImage(file="main.png")
Label(main_screen,image=photo).pack()

Label(main_screen,text="RESTAURENT MANAGEMENT SYSTEM", bd=15,relief=FLAT,width=41,fg='yellow',height=2,bg="black",font=("Showcard Gothic",35,"bold")).place(x=0,y=0)
username_verify = StringVar()
password_verify = StringVar()
name = StringVar()
username = StringVar()
password = StringVar()
password_confirm = StringVar()
phone_nos = StringVar()
Category = StringVar()

Button(text="Login",  bd=7,relief=GROOVE,font=("Copperplate Gothic Bold",25),bg='green',fg='white',width=30,command=login).place(x=320,y=270)
Button(text="New user - Register here",  bd=7,relief=GROOVE,font=("Copperplate Gothic Bold",25),bg='green',fg='white',width=30,command=register).place(x=320,y=380)
photo1 = PhotoImage(file="exit.png")
Button(image=photo1,borderwidth=1,command = close).place(x=1120,y=600)

main_screen.mainloop()




