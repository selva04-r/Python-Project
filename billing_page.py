from tkinter import *
from tkinter import ttk
import tkinter.messagebox as tmsg
import os
import time as ti
import random as rd
import csv
import mysql.connector as mm
from datetime import date

#===============================================
def b():

    def b2():
        delete_all_menu()
        f = open("Beverages.csv" , "r")
        csvr = list(csv.reader(f))
        category="==================="+"Beverages"
        food_tabel.insert(parent='',index=END,values=['',category])
        for i in range(len(csvr)):
            quantity_dict[csvr[i][0]]=csvr[i][3]
            food_tabel.insert(parent='',index=END,values=[csvr[i][0],csvr[i][1],csvr[i][2],category])

    def b3():
        delete_all_menu()
        f = open("Fast Food.csv" , "r")
        csvr = list(csv.reader(f))
        category="==================="+"Fast Food"
        food_tabel.insert(parent='',index=END,values=['',category])
        for i in range(len(csvr)):
            quantity_dict[csvr[i][0]]=csvr[i][3]
            food_tabel.insert(parent='',index=END,values=[csvr[i][0],csvr[i][1],csvr[i][2],category])
            
    def b4():
        delete_all_menu()
        f = open("South Indian.csv" , "r")
        csvr = list(csv.reader(f))
        category="==================="+"South Indian"
        food_tabel.insert(parent='',index=END,values=['',category])
        for i in range(len(csvr)):
            quantity_dict[csvr[i][0]]=csvr[i][3]
            food_tabel.insert(parent='',index=END,values=[csvr[i][0],csvr[i][1],csvr[i][2],category])
            
    def b5():
        delete_all_menu()
        f = open("Snacks.csv" , "r")
        csvr = list(csv.reader(f))
        category="==================="+"Snacks"
        food_tabel.insert(parent='',index=END,values=['',category])
        for i in range(len(csvr)):
            quantity_dict[csvr[i][0]]=csvr[i][3]
            food_tabel.insert(parent='',index=END,values=[csvr[i][0],csvr[i][1],csvr[i][2],category])
            
    def b6():
        delete_all_menu()
        f = open("Main Course.csv" , "r")
        csvr = list(csv.reader(f))
        category="==================="+"Main Course"
        food_tabel.insert(parent='',index=END,values=['',category])
        for i in range(len(csvr)):
            quantity_dict[csvr[i][0]]=csvr[i][3]
            food_tabel.insert(parent='',index=END,values=[csvr[i][0],csvr[i][1],csvr[i][2],category])
            
    def b7():
        delete_all_menu()
        f = open("Dessert.csv" , "r")
        csvr = list(csv.reader(f))
        category="==================="+"Dessert"
        food_tabel.insert(parent='',index=END,values=['',category])
        for i in range(len(csvr)):
            quantity_dict[csvr[i][0]]=csvr[i][3]
            food_tabel.insert(parent='',index=END,values=[csvr[i][0],csvr[i][1],csvr[i][2],category])

    
    global food_frame,food_tabel,right_frame


    food_tabel = ttk.Treeview(food_frame,columns =('code',"name", "price",'category'))


    food_tabel["columns"]=('code',"name", "price") # columns
    food_tabel.column("#0",width=0,stretch=NO) # first column which is complusory 
    food_tabel.column("price",width=50,anchor='center') # updating the column
    food_tabel.column("code",width=50,anchor='center')
    #food_tabel.column("stock",width=50,anchor='center') 
    #heading
    food_tabel.heading("name",text="Name")
    food_tabel.heading("price",text="MRP")
    food_tabel.heading("code",text="Food Code")
    #food_tabel.heading("stock",text="In Stock")
    food_tabel.pack(fill=BOTH,expand=1)
    # to choose a item from the menu table
    food_tabel.bind("<ButtonRelease>",display_box)

    
    food_button = Frame(food_frame)
    photo2 =  PhotoImage(file="juice.png")
    food_button.photo2 = photo2
    photo3 =  PhotoImage(file="fast food.png")
    food_button.photo3 = photo3
    photo4 =  PhotoImage(file="south indian.png")
    food_button.photo4 = photo4
    photo5 =  PhotoImage(file="snacks.png")
    food_button.photo5 = photo5
    photo6 =  PhotoImage(file="main course.png")
    food_button.photo6 = photo6
    photo7 =  PhotoImage(file="dessert.png")
    food_button.photo7 = photo7
    Button(food_button, image=photo2,relief=FLAT,width=100,bg='white',command=b2).grid(row=0,column=0,padx=32,pady=7)
    Button(food_button, image=photo3,relief=FLAT,width=100,bg='white',command=b3).grid(row=0,column=1,padx=32,pady=7)
    Button(food_button, image=photo4,relief=FLAT,width=100,bg='white',command=b4).grid(row=0,column=2,padx=32,pady=7)
    Button(food_button, image=photo5,relief=FLAT,width=100,bg='white',command=b5).grid(row=1,column=0,padx=32,pady=7)
    Button(food_button, image=photo6,relief=FLAT,width=100,bg='white',command=b6).grid(row=1,column=1,padx=32,pady=7)
    Button(food_button, image=photo7,relief=FLAT,width=100,bg='white',command=b7).grid(row=1,column=2,padx=32,pady=7)
    food_button.pack(fill='both')

def display_box(c):
    cursor_row = food_tabel.focus() # get the index position of the values
    contents = food_tabel.item(cursor_row) # get the values using the index position
    row = contents["values"]
    global Display
    global itemQuantity
    Display.config(state='normal')
    item_quantity.config(state='normal')
    Display.delete('1.0',END)
    Display.insert(END,'  Code No. :: ' + row[0])
    Display.insert(END,'\n  Name :: ' + row[1])
    Display.insert(END,'\n  Category :: ' + row[-1][19:])

    try:
        Display.insert(END,'\n  MRP :: ' + str(row[2]))
    except:
        Display.delete('1.0',END)
    
    itemQuantity.set('1')
    item_quantity.config(state='disabled')
    Display.config(state='disabled')

def load_item_from_order(c):
    cursor_row = book_tabel.focus() # get the index position of the values
    contents = book_tabel.item(cursor_row) # list of all the contents in that paticular line
    row = contents["values"]
    global itemQuantity
    Display.config(state='normal')
    item_quantity.config(state='normal')
    itemQuantity.set(row[4])
    Display.delete('1.0',END)
    Display.insert(END,'  Code No. :: ' + str(row[1]))
    Display.insert(END,'\n  Name :: ' + row[2])
    Display.insert(END,'\n  Category :: ' + row[0])
    Display.insert(END,'\n  MRP :: ' + str(row[3]))
    Display.config(state='disabled')
    item_quantity.config(state='disabled')
    
def delete_all_menu():
    for record in food_tabel.get_children():
        food_tabel.delete(record)

def delete_orders():
    for record in book_tabel.get_children():
        book_tabel.delete(record)

def update_button_operation():
    cursor_row = book_tabel.focus() # get the index position of the values
    contents = book_tabel.item(cursor_row) # list of all the contents in that paticular line
    row = contents["values"]
    global itemQuantity
    quantity = itemQuantity.get()
    if int(quantity_dict[row[1]]) < int(quantity):
        tmsg.showinfo("Error", "You have exceeded the stock")
        order[row[0]][row[1]][-2] = quantity_dict[row[1]]
        order[row[0]][row[1]][-1] = str(int(row[-3])*int(quantity_dict[row[1]]))
        update_order()
        return

    order[row[0]][row[1]][-2] = quantity
    order[row[0]][row[1]][-1] = str(int(row[-3])*int(quantity))
    update_order()
    

# to update the order table while inserting,deleting and updating
# as every time the order table is changed.
def update_order(): # to update the order dict
    delete_orders() # every time the order table is cleared and re-entered

    quantity = itemQuantity.get()
            
    for category in order.keys():
        for nos in order[category] :
            # i = category,code,name,mrp,quantity,price
            i = order[category][nos]
            book_tabel.insert('',END,values=i)
    update_total_price()

def add_button_operation():    
    global itemQuantity
    cursor_row = food_tabel.focus() # get the index position of the values
    contents = food_tabel.item(cursor_row) # get the values using the index position
    row = contents["values"]
    text = Display.get(1.0,END)
    text = text.split('\n')
    quantity = itemQuantity.get()
    details = []
    for i in text:
        details.append(i.split(' :: '))
        
    # details = [['  Code No.', 'PH109'], ['  Name', 'Watermelon Juice'], ['  Category', 'Beverages'], ['  MRP', '150'], ['']]

    if details[1] == '':
        return
    
    elif details[0][1] in order[details[2][1]]: # whether the item already exist
        tmsg.showinfo("Error", "Item already exist in your order")

    elif int(quantity_dict[details[0][1]]) == 0:
        tmsg.showinfo("Error", "Out of stock")

    elif int(quantity_dict[details[0][1]]) < int(quantity):
        tmsg.showinfo("Error", "You have exceeded the stock add")

    else:
        #category,code,name,mrp,quantity,price
        list1 = [details[2][1],details[0][1],details[1][1],details[3][1],quantity,str(int(details[3][1])*int(quantity))]
        # to get track of the total price and item ordered
        order[details[2][1]][details[0][1]] = list1
        
        # order = {'Beverages': {'PH106': ['Beverages', 'PH106', 'Mineral Water', '55', '1', '55']},
        # 'Fast Food': {}, 'South Indian': {}, 'Snacks': {}, 'Main Course': {}, 'Dessert': {}}
        
        update_order()
        
def clear_button_operation(): # to clear the entry
    Display.config(state='normal')
    Display.delete('1.0',END)
    Display.config(state='disabled')
    
def cancel_button_operation():
    names = []
    for i in menu_category: # to check whether the user has ordered any item 
        names.extend(order[i]) # appending the product name
    if len(names)==0:
        tmsg.showinfo("Error", "Your order list is Empty")
        return
    ans = tmsg.askquestion("Cancel Order", "Are You Sure to Cancel Order?")
    if ans=="no":
        return
    delete_orders()
    for i in menu_category:
        order[i] = {}
    clear_button_operation()
    update_total_price()
    
def remove_button_operation():
    cursor_row = book_tabel.focus() # get the index position of the values
    contents = book_tabel.item(cursor_row) # list of all the contents in that paticular line
    row = contents["values"]
    # category,code,name,mrp,quantity,total
    
    if str(row[1]) not in order[row[0]]:
        tmsg.showinfo("Error", "Item is not in your order list")
        return
    
    del order[row[0]][row[1]]
    Display.config(state='normal')
    Display.delete('1.0',END)
    Display.config(state='disabled')
    item_quantity.config(state='normal')
    itemQuantity.set(1)
    item_quantity.config(state='disabled')

    
    update_order()

def update_total_price():
    price = 0
    for i in menu_category:
        for j in order[i]:
            price += int(order[i][j][-1])
    if price == 0:
        totalPrice.set("")
    else:
        totalPrice.set("Rs. "+str(price)+"  /-")

def update_stock():
    for file in menu_category_dict: # opening all the files
        f = open(menu_category_dict[file] , "r")
        csvr = csv.reader(f)
        r=list(csvr)
        l=r.copy()
        f.close()
        for i in range(len(r)):
            try:
                a = int(l[i][-1]) - int(order[file][l[i][0]][-2])
                l[i][-1] = a
            except:
                pass
            f1=open(menu_category_dict[file] ,'w',newline='')
            csvw = csv.writer(f1)
            csvw.writerows(l)
            f1.close()

def discount_update(n,ph,ta,dp,d,a):
    mydb = mm.connect(host="localhost",user="root",passwd="selva",database='hotel')
    c = mydb.cursor()
    a1 = 'insert into t2 values(%s,%s,%s,%s,%s,%s,%s)'
    dat = date.today().strftime("%Y-%m-%d")# yyyy-mm-dd
    a2 = (n,ph,ta,dp,d,a,dat)
    c.execute(a1,a2)
    mydb.commit()

def bill_button_operation():
    names = []
    for i in menu_category: # to check whether the user has placed an order
        names.extend(order[i]) # appending the product name
    if len(names)==0:
        tmsg.showinfo("Error", "Your order list is Empty")
        return
    global bill
    bill = Toplevel()
    bill.title("BILL")
    bill.geometry("670x500+300+100")
    bill_area = Text(bill, font=("Times New Roman", 12))
    update = 0
        
    detail = "=" * 74 + "\n\t\t\t\tPROJECT HOTEL\n"
    detail += "=" * 74
    detail+="\n\t\t\tNo.14/5, C.T.H Road,Thangamani Street " + "\n\t\t\t              Ambattur, Chennai-600053\n"
    detail += "\n\t\tPh : 044-46536688          GST.NO:- 27AHXPP3379HIZH\n\t\t\t\tTAX INVOICE\n"
    detail += "\n" + "=" * 35 + "BILL" + "=" * 35

    # updating the total amount
    cus_name,phone,discount_per,festival_name = amount_update(totalPrice.get())
    
    #Bill no
    nos = rd.randrange(606546,64995483)
    dat = date.today().strftime("%d/%m/%Y") # dd-mm-yyyy
    detail += "\n  Bill No : " + str(nos) + ' '*90 + 'Date - ' +  dat
    time = ti.strftime('%I:%M:%S %p')
    detail += "\n  Customer name : " + cus_name + ' '*90 + 'Time - ' +  time
    detail += "\n  Phone number : " + phone
    
    #product details
    detail += "\n\n" + "-"*111 + "\n" +  "    PRODUCT NAME\t\t\t\t\tRATE\tQUANTITY\t\tAMOUNT\n"
    detail += "-"*111 + "\n" 
    
    for i in menu_category:
        for j in order[i]:
            lis = order[i][j]
            name = lis[2].upper()
            rate = lis[3]
            quantity = lis[4]
            price = lis[-1]
            detail += '    ' + name + "\t\t\t\t\t" + rate + ".00\t      " + quantity + ".00\t\t  " + price + ".00\n\n"
    #total 
    detail += "~" * 74
    if discount_per == '0' :
        detail += "\n\tTOTAL PRICE : \t\t\t\t\t\t\t" + totalPrice.get() + "\n"
    else:
        update = 1
        detail += "\n\tTotal Amount : \t\t\t\t\t\t\t" + totalPrice.get() + "\n\n\n"
        detail += "\tOn account of - " + festival_name
        dis = round(int(str(totalPrice.get()).split(' ')[1])*(int(discount_per)/100),3)
        detail += "\n\tDiscount : \t\t\t\t\t\t\t" + '-' + str(dis) + '/-'+ "\n"
        detail += "~"*74
        total_price = int(str(totalPrice.get()).split(' ')[1])
        am_ount = total_price - round(int(str(totalPrice.get()).split(' ')[1])*(int(discount_per)/100),3)
        detail += ("\n\tTOTAL PRICE : \t\t\t\t\t\t\t" + 'Rs.' + str(am_ount) + '/-' + "\n")
    detail += "~"*74
    detail += "\n\n\n\t\t\tThank you - Visit Again"

    
    bill_area.insert(END, detail)
    bill_area.pack(expand=True, fill=BOTH)
    
    if update:
        discount_update(cus_name,phone,total_price,discount_per,dis,am_ount)
        
    # Clear everything
    delete_orders()
    update_stock()
    clear_button_operation()
    update_total_price()
    k=Frame(bill)
    k.pack()
    try:
        os.remove('discount.txt')
    except:
        pass
    Button(k, text='Close',font=("Arial", 12, "bold"),bg='#FFD700',width=10,bd=5,relief=SUNKEN, command=bill_close).pack()
    
    

def bill_close():
    global bill
    bill.destroy()
    feedback()
    
def feedback():
    root = Toplevel()
    heading = Frame(root)
    heading.pack()
    Label(heading, text='CUSTOMER FEEDBACK', bg = "#EEC591", fg="black",font=('Forte', 28)).grid(row=0, column=1)
    Label(heading,text='PLEASE TELL US WHAT YOU THINK',fg='Blue',font=('Times New Roman',14,'bold')).grid(row=1, column=1,pady=10)

    content = Frame(root)
    content.pack()

    name = StringVar()
    email = StringVar()
    Label(content, text='Name', font=('Algerian', 13)).grid(row=0, column=0, padx=5, sticky='sw')
    Entry_name = Entry(content, width=20, font=('Baskerville Old Face', 14), textvariable=name).grid(row=1, column=0,  padx=5,sticky='sw')

    Label(content, text='Email', font=('Algerian', 13)).grid(row=0, column=1, sticky='sw')
    Entry_email = Entry(content, width=20, font=('Baskerville Old Face', 14), textvariable=email).grid(row=1, column=1,sticky='sw')

    Label(content, text='Comment', font=('Algerian', 13)).grid(row=2, column=0, sticky='sw')
    comment = Text(content, width=100, font=('Times New Roman',12,'bold'),height=10)
    comment.grid(row=3, column=0, columnspan=2)

    mydb = mm.connect(host="localhost",user="root",passwd="selva",database='hotel')
    c = mydb.cursor()    
    
    def clear():
        global Entry_name, Entry_email,textcomment
        name.set('')
        email.set('')
        comment.delete(1.0, END)


    def submit():
        global entry_name, entry_email, textcomment, root
        if len(comment.get(1.0, END))==1 or len(name.get())==0 or len(email.get())==0:
               tmsg.showinfo(title='Error', message='Please enter the feedback')
               return 
        dat = date.today().strftime("%Y-%m-%d")# yyyy-mm-dd
        tmsg.showinfo(title='Submitted', message='Thank you for your Feedback')
        a = 'insert into t3 values(%s,%s,%s,%s)'
        a1 = (dat,name.get(),email.get(),comment.get(1.0, END))
        c.execute(a,a1)
        mydb.commit()
        mydb.close()
        
    def cancel():
        global root
        message = tmsg.askyesno(title='Cancellation', message='Do you want to cancel the feedback ?')
        if message:
            content.destroy()
    
    Button(content, text='Submit',font=("Arial", 12, "bold"),bg='#FFD700',width=10,bd=5,relief=SUNKEN, command=submit).grid(row=6,column=0,padx=0)
    Button(content, text='Clear', font=("Arial", 12, "bold"),bg='#FFD700',width=10,bd=5,relief=SUNKEN,command=clear).grid(row=6, column=2,padx=0)
    Button(content, text='Cancel', font=("Arial", 12, "bold"),bg='#FFD700',width=10,bd=5,relief=SUNKEN,command=cancel).grid(row=6, column=1,padx=1,sticky='w')
    
def amount_update(am):
    f1 = open('temp.txt','r')
    lk = f1.readlines()
    f1.close()
    mydb = mm.connect(host="localhost",user="root",passwd="selva",database='hotel')
    c = mydb.cursor()
    c.execute('select * from t1')
    l = c.fetchall()

    am = str(am).split(' ')[1]
    
    try:
        os.system('textfile discount.txt')
        f=open('discount.txt','r')
        lm = f.readlines()
        f.close()
    except:
        lm=['0','0','0']
    q=int(am)
    if lm[-1] != '0':
        q = int(am) - round((int(am)*(int(lm[-2])/100)),3)

    for i in l:
        #name check
        if i[0] == lk[0][:-1]:
            a = 'update t1 set Times_purchased = %s where Phone_number = %s '
            a1 = (str(int(i[2])+1),lk[1])
            c.execute(a,a1)
            mydb.commit()
            b = 'update t1 set Amount = %s where Phone_number = %s '
            b1 = (str(float(i[-1])+q),lk[1])
            c.execute(b,b1)
            mydb.commit()
            break
    else: # first time purchase
        a = 'insert into t1 values(%s,%s,%s,%s)'
        a1 = (lk[0][:-1],lk[1],'1',str(q))
        c.execute(a,a1)
        mydb.commit()
    mydb.close()

    return lk[0][:-1],lk[1],lm[-2],lm[-1]

def plus():
    item_quantity.config(state='normal')
    q = item_quantity.get()
    itemQuantity.set(int(q)+1)
    item_quantity.config(state='disabled')

def minus():
    item_quantity.config(state='normal')
    q = item_quantity.get()
    if int(q)<=1:
        tmsg.showinfo("Error", "Quantity can't be less than 1")
        item_quantity.config(state='disabled')
        return
    else:
        itemQuantity.set(int(q)-1)
    item_quantity.config(state='disabled')

def search_details():
    s = search_box.get()
    if s=='':
        tmsg.showinfo("Error", "Enter a word for searching")
        return
    else:
        details = {}
        code,name,found=[],[],0
        for file in menu_category_dict: # opening all the files
            f = open(menu_category_dict[file] , "r")
            csvr = list(csv.reader(f))
            category="==================="+file
            details[category]=csvr
            for c in csvr:
                name.append(c[1].lower())
                code.append(c[0])
        delete_all_menu()
        for i in name:
            if s.lower() == i.lower()[:len(s)] :
                cc = name.index(i)
                cod = code[cc]
                for k in details:
                    for j in range(len(details[k])):
                        if details[k][j][0] == cod :
                            quantity_dict[details[k][j][0]]=details[k][j][3]
                            food_tabel.insert(parent='',index=END,values=[details[k][j][0],details[k][j][1],details[k][j][2],category])
                            found=1
                            break
    if not found:
        tmsg.showinfo("Error", "No results match")

def logout():
    c = tmsg.askyesno('Warning','Do you want to logout ?',parent=title_frame)
    if c:
        root.destroy()
        import admin_window
            
######################################
# MAIN SEGMENT #

menu_category = ["Beverages", "Fast Food", "South Indian", "Snacks", "Main Course", "Dessert"]
# to open the file 
menu_category_dict = {"Beverages":"Beverages.csv",
                "Fast Food":"Fast Food.csv","South Indian":"South Indian.csv",
                "Snacks":"Snacks.csv","Main Course":"Main Course.csv",
                "Dessert":"Dessert.csv"}

order = {}
for i in menu_category:
    order[i] = {}

# to know the stock details
quantity_dict = {}

#=================================
root = Tk()
root.geometry("1350x700+0+0")
root.resizable(0, 0)

#==============================
# normal, bold, roman, italic, underline, and overstrike
title_frame = Frame(root, background="#EEC591").pack(side=TOP)

Label(title_frame, text="PROJECT HOTEL", font=("Algerian", 25, "italic"),bg = "#EEC591", fg="black" ).pack(fill="both",pady=5)
logout_photo = PhotoImage(file="logout.png")
Button(title_frame, image=logout_photo,bd=3,command=logout).place(x=0,y=0)
#==============================
big_frame = Frame(root,bd=8, bg="#EEE8CD", relief=GROOVE)
big_frame.place(x=680,y=70,height=630,width=670)

right_frame = Frame(big_frame,bg="#EEE8CD",pady=10)
right_frame.pack(fill="x")
Label(right_frame,text="Enter name",font=("arial", 15, "bold"),bg = "#EEE8CD", fg="black").grid(row=1,column=0,padx=5,pady=15)
search = StringVar()
search_box = Entry(right_frame, font=("arial", 15, "bold"),textvariable=search, width=12)
search_box.grid(row=1,column=1,padx=10)

photo_searc = PhotoImage(file="search1.png")
search_button = Button(right_frame, image=photo_searc,bg='#efe7cd',bd=0,relief=FLAT,command=search_details)
search_button.grid(row=1,column=3,stick=W)
## Style - font for treeview

style = ttk.Style()
style.configure("Treeview.Heading",font=("Forte",13))
style.configure("Treeview",font=("Baskerville Old Face",12,'bold'),rowheight=25)

############################# Menu Tabel ##########################################
food_frame = Frame(big_frame)
food_frame.place(y=65,height=530,width=655)
b()

###########################################################################################
top_left_frame = Frame(root,bd=8, bg="#EEE8CD", relief=GROOVE)
top_left_frame.place(x=0,y=70,height=170,width=400)

button_frame = Frame(root,bd=8, bg="#EEE8CD", relief=GROOVE)
button_frame.place(x=400,y=70,height=170,width=280)

minus_quantity = Button(button_frame, text="-",  font=("Rockwell Extra Bold", 13, "bold"),command = minus,bg = "#BFEFFF", fg="blue")
minus_quantity.place(x=10,y=60)

item_quantity_label = Label(button_frame, text="Quantity",  font=("arial", 13, "bold"),bg = "#EEE8CD", fg="blue")
item_quantity_label.place(x=80,y=20)

plus_quantity = Button(button_frame, text="+", font=("Rockwell Extra Bold", 13, "bold"),command = plus,bg = "#BFEFFF", fg="blue")
plus_quantity.place(x=200,y=60)

itemQuantity = StringVar(value = '1')
item_quantity = Entry(button_frame, font=("arial",15),textvariable=itemQuantity,state= 'disabled' ,width=10)
item_quantity.place(x=60,y=62)

Display = Text(top_left_frame,width=35,height=12,font=('arial', 16,'bold'),state='normal')
Display.pack(side=LEFT)

#===================================
book_frame = Frame(root,bd=8, bg="#EEE8CD", relief=GROOVE)
book_frame.place(x=0,y=230,height=475,width=680)

############################## Order Tabel ###################################
book_tabel_frame = Frame(book_frame)
book_tabel_frame.place(x=0,y=100,height=260,width=660)

scrollbar_order_y = Scrollbar(book_tabel_frame,orient=VERTICAL)

book_tabel = ttk.Treeview(book_tabel_frame,columns =('category',"code","name","mrp","quantity","price"),yscrollcommand=scrollbar_order_y.set)

book_tabel["columns"]=('category',"code","name","mrp","quantity","price")
book_tabel.column("#0",width=0,stretch=NO)
book_tabel.column("category",width=90,anchor='center')
book_tabel.column("code",width=90,anchor='center')
book_tabel.column("name",width=170,anchor='center')
book_tabel.column("mrp",width=70,anchor='center')
book_tabel.column("quantity",width=70,anchor='center')
book_tabel.column("price",width=80,anchor='center')

book_tabel.heading("category",text="Category")
book_tabel.heading("code",text="Food Code")
book_tabel.heading("name",text="Name")
book_tabel.heading("mrp",text="MRP")
book_tabel.heading("quantity",text="Quantity")
book_tabel.heading("price",text="Price")

book_tabel.bind("<ButtonRelease>",load_item_from_order)

scrollbar_order_y.pack(side=RIGHT,fill=Y)

scrollbar_order_y.configure(command=book_tabel.yview)

book_tabel.pack(fill=BOTH,expand=1)

###########################################################################################

add_button = Button(book_frame, text="Add Item",font=("arial", 13, "bold"),bg='light grey',width=20,command=add_button_operation)
add_button.place(y=10,x=40)
remove_button = Button(book_frame, text="Remove Item",font=("arial", 13, "bold"),bg='light grey',width=20,command=remove_button_operation)
remove_button.place(y=10,x=370)
update_button = Button(book_frame, text="Update Quantity",font=("arial", 13, "bold"),bg='light grey',width=20,command=update_button_operation)
update_button.place(y=50,x=90)
total_price_label = Label(book_frame, text="Total Price", font=("arial", 18, "bold"),bg = "#EEE8CD", fg="#EE1289")
total_price_label.pack(side=LEFT,anchor=SW,padx=20,pady=20)

totalPrice = StringVar()
total_price_entry = Entry(book_frame, font=("arial", 15, "bold"),textvariable=totalPrice,state=DISABLED,bd=5,relief=SUNKEN,width=10)
total_price_entry.pack(side=LEFT,anchor=SW,padx=0,pady=20)

bill_button = Button(book_frame, text="Place order",font=("Arial", 13, "bold"),bg='#FFD700',width=10,bd=5,relief=SUNKEN,command=bill_button_operation)
bill_button.pack(side=LEFT,anchor=S,padx=40,pady=20)

cancel_button = Button(book_frame, text="Cancel Order",font=("Arial", 13, "bold"),bg='#FFD700',width=12,bd=5,relief=SUNKEN,command=cancel_button_operation)
cancel_button.pack(side=LEFT,anchor=S,pady=20)


root.mainloop()
