#reading excel file using pandsin python
from pymongo import MongoClient
import json
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

client = MongoClient()
db = client.user2

df = pd.read_excel('exceltoread.xlsx', sheet_name='Sheet1')

print("Column headings:")
print(df.columns)

#priting exel content using for loop
for i in df.index:

    print( "Name = " + df["Sname"][i])
    print("Email = " + df['Email'][i])


#######################################
#Inserting values to MongoDB


sr_no = []
name = []
email = []

#looping the excel content to append in list
for j in df.index:

  sr_no.append(str(df['Sr_no'][j]))
  name.append(str(df['Sname'][j]))
  email.append(str(df['Email'][j]))



userinfo = db.users4py

#inserting the content in mongodb
for k in range(0,(len(sr_no))):
  post_data = {
    'Sr_no': sr_no[k],
    'Sname': name[k],
    'Email': email[k]

   }
  userinfo.insert_one(post_data)








