# to save to a csv file, we must use the csv module
import csv 
with open('C:/Users/Admin/Documents/records/studentfiles/results1.csv','w',newline="") as results:
    writer=csv.writer(results)#the csv.writer class is used to write data into the csv file 
    #using the writerow() function to write new rows/data into our csv file one by one
    #writer.writerow(['Names','English','Mathematics','Programming','Science'])
    #writer.writerow(['Ahmed','80','88','77','47']),
    #writer.writerow(['Bronson','98','78','86','39']),
    #writer.writerow(['Erick','74','98','87','49']),
    #writer.writerow(['Hayyan','98','87','88','46']),
    #writer.writerow(['Charles','90','86','76','73'])
    #using the writerows() method to fill our data at once 
    student_Results=[['Names','English','Mathematics','Programming','Science'],
                    ['Ahmed','80','88','77','47'],
                    ['Bronson','98','78','86','39'],
                    ['Erick','74','98','87','49'],
                    ['Hayyan','98','87','88','46'],
                    ['Charles','90','86','76','73'],
                ]
    writer.writerows(student_Results)

# using the csv.dictwriter class
student_Dict=[
    {
        'Name':'Bronson',
        'English':'98',
        'Mathematics':'78',
    },
    {   'Name':'Hayyan',
        'English':'89',
        'Mathematics':'78',
    },
    ]
#extract columns
table_colums=['Name','English','Mathematics']
#open the file
with open('C:/Users/Admin/Documents/records/studentfiles/results3.csv','w',newline="") as results:
    writer=csv.DictWriter(results,fieldnames=table_colums)
    writer.writeheader()
    writer.writerows(student_Dict)