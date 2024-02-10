import mysql.connector as mm

########### Password  #######
password = input("Enter your mysql password :: ")
###########################

mydb = mm.connect(host="localhost",user="root",passwd=password)
c = mydb.cursor()
try :
     c.execute('create database hotel')
     c.execute('use hotel')
     c.execute('create table t1(Name char(20),Phone_number char(20),Times_purchased char(10), Amount char(50))')
     c.execute('create table t2(Name char(20),Phone_number char(20),Total_amount char(20), Discount_percentage char(20),Discount_amount char(20),To_be_paid char(20),Date date)')
     c.execute('create table t3(Date date,Name char(30),Email char(50),Comment char(200))')
     mydb.commit()
     mydb.close()
     print("Table created successfully")
except :
     print("Table already exists")
