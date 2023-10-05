import csv
import matplotlib.pyplot as plt
import pandas as pd
header=['Prod_No','Prod_Name','Jan','Feb','Mar','Apr','May','Jun']
l=[]
with open("selling.csv",'w',newline="") as file:
    insert =csv. writer(file)
    insert.writerow(header)
    for i in range(5):
        prod_no = input("Enter Product Number: ")
        prod_name = input("Enter Product Name: ")
        jan = int(input("Enter January Sales: "))
        feb = int(input("Enter February Sales: "))
        mar = int(input("Enter March Sales: "))
        apr = int(input("Enter April Sales: "))
        may = int(input("Enter May Sales: "))
        jun = int(input("Enter June Sales: "))
        data=[prod_no,prod_name,jan,feb,mar,apr,may,jun]
        l.append(data)
    insert.writerows(l)
df=pd.read_csv("selling.csv")
print(df)
df['total_sell'] = df[['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']].sum(axis=1)
df['average_sell'] = df[['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']].mean(axis=1)
print(df)
name=(['phone','headset','bag','pencil','laptop'])
plt.plot(name,df['total_sell'])
plt.plot(name,df['average_sell'])
plt.xlabel('product_name')
plt.ylabel('no of sales')
plt.title('Sell Over month')
plt.legend(['total_sell','average_sell'])
plt.show()
