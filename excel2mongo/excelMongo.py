#reading excel file using pandsin python
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

df = pd.read_excel('exceltoread.xlsx', sheet_name='Sheet1')

print("Column headings:")
print(df.columns)

#priting one cell content
print(df['Sname'][0])


#priting exel content using for loop
for i in df.index:

    print( "Name = " + df["Sname"][i])
    print("Email = " + df['Email'][i])






