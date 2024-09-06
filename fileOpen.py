fh=open('poem.txt','rt',encoding='UTF8')

for line in fh.readlines():
    print(line.strip())#Removes the trailing and preceding white scapes in the lines 
fh.close()