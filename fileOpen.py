try:
    fh=open('poem.txt','rt',encoding='UTF8')
    fh.write('This is just jiberish content')
#for line in fh.readlines():
 #   print(line.strip())#Removes the trailing and preceding white scapes in the lines 
 
fh.close()

#delete the file
#we use the os.remove()
#import the os module
import os
try(
    if os.path.exists('peom.txt'):
        os.remove('C:/Users/Admin/Documents/Github/PYTHONOOP/poem.txt')

        print('File deleted sucessfully')

    else:
    print('File not found')
)