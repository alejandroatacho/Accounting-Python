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
    print(formule2[x])
    x = x+1
    #x_average = formule2[x] + x_average
    if x == formule2.size:
        break
#unit_sold * price
for i in df:
    print(formule3[y])
    y = y+1
    if y == formule3.size:
        break
print(x_average)
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
