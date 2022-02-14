from fileinput import close
import pandas as pd
import os

path = "files//Journal.xlsx"  # Cleaner version
x = 0
x_average = 0
y = 0
y_average = 0

df = pd.read_excel(r'Accounting-Python//files//Journal.xlsx')
formule1 = df['Product'].values
formule2 = df['Units'].values * df['Cost'].values
formule3 = df['Units_Sold'].values * df['Price'].values

#unit * cost
for i in df:
    # print(formule2[x])
    x_average = int(formule2[x]) + x_average
    x = x+1

    if x == formule2.size:
        print(str(x_average) + "$ Cost")
        break
#unit_sold * price
for i in df:
    # print(formule3[y])
    y_average = int(formule3[y]) + y_average
    y = y+1
    if y == formule3.size:
        print(str(y_average)+"$ Profit")
        break
profit = y_average - (x_average)

if profit >= 0:
    print(str(profit) + "$ Profit Made")
else:
    print(str(profit) + "$ Was Lost")


#print(str(profit) + " Profit made")
#print("You made this much "+str(profit))

# read the excel column and puts it out
'''for i in df:
    print(formule1[x])
    x = x+1
    if x == formule1.size:
        break
    '''

# check if the directory actually exist or can be read
'''
if os.path.exists(path):
    print("that location exists!")
elif os.path.isdir(path):
    print("That is a directory")
else:
    print("that location does not exist")
'''

# print(df)
# print(formule1)
