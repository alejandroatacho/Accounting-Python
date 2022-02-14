import pandas as pd
import os
path = "files//Journal.xlsx"  # Cleaner version

# place "r" before the path string to address special character, such as '\'. Don't forget to put the file name at the end of the path + '.xlsx'
df = pd.read_excel(r'Accounting-Python//files//Journal.xlsx')

'''
if os.path.exists(path):
    print("that location exists!")
elif os.path.isdir(path):
    print("That is a directory")
else:
    print("that location does not exist")
'''

print(df)
