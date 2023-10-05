import csv
import sqlite3 as sq
import pandas as pd
import matplotlib.pyplot as plt
#create Table
conn=sq.connect("sales.db")
cur=conn.cursor()
cur.execute(" " "create table if not exists sales(sid int primary key,year int,totalsales int)""")
#A. Insert at least 5-10 records into the sales table.
query="insert into sales values(?,?,?)"
record=[]
for i in range(5):
    num=int(input("Enter sales id:"))
    year_new=int(input("Enter year:"))
    sale=int(input("Enter total sales:"))
    list1=[num,year_new,sale]
    record.append(list1)
cur.executemany(query,record)
#B. Export sales table data into sales.csv file.
cur.execute('select * from sales;')
rec=cur.fetchall()
conn.commit()
h=['sid','year','totalsales']
with open("sales.csv","w",newline='') as csv_file:
    writer=csv.writer(csv_file)
    writer.writerow(h)
    writer.writerows(rec)
#C. Write a python scripts that read the sales.csv file and plot a bar chart that shows totalsales of the year.
df=pd.read_csv("sales.csv")
print(df)
#plot a Bar Chart.
plt.bar(df['year'],df['totalsales'],color=['black','red','purple','blue','green'])
plt.title('Total sales over the 5 year')
plt.xlabel('year')
plt.ylabel('total sales')
plt.xticks(rotation=30)
plt.show()
