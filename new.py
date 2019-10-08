import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='mydb')
mycursor=mydb.cursor()
#sql='create table customers(name varchar(100), address varchar(100))'
#mycursor.execute(sql)
#sql='alter table customers add column id int auto_increment primary key'
#mycursor.execute(sql)
#mycursor.execute('select version()')
#data=mycursor.fetchone()
#print(data)
#mycursor.execute('drop table if exists employee')
#sql="""create table employee(first_name varchar(100) not null,
#last_name varchar(100),
#age int,
#sex char(1),
#income float)
#"""
#mycursor.execute(sql)
#sql="""insert into employee(first_name, last_name, age, sex, income) values
#('Jack', 'Ali', 12, 'M', 123233.3434)"""
sql='select * from employee'

mycursor.execute(sql)
#mydb.commit()
d=mycursor.fetchall()
for row in d:
    fname=row[0]
    lname=row[1]
    age=row[2]
    sex=row[3]
    income=row[4]
    print("fname=%s, lname=%s, age=%d, sex=%s, income=%d" % \
          (fname, lname, age, sex, income))
    #print(fname," ",lname," ",age," ",sex," ",income)

mydb.close()




