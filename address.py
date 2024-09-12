from persons import Person, Address, engine
from sqlalchemy.orm import sessionmaker

#create a session, which is the object we use to manage the database
Session=sessionmaker(bind=engine)
session=Session()

#create 2 people
cust1=Person(name='Bronson Loni',age=24)
cust2=Person(name='Hayyan Mohamed',age=23)

# add email addresses to both using two different techniques
# this assigns the email addresses as a list
cust1.addresses=[
    Address(email='Lonithebron@gmail.com'),
    Address(email='hloni@gmail.com'),
]

#append the addreses to the specific customer
cust2.addresses.append(Address(email = 'hayan@mail.com'))
cust2.addresses.append(Address(email='hmohamed@gmail.com'))

# so far we have not yet touched the database
#use the session maker to add data into the database
session.add(cust1)
session.add(cust2)

#run the commit to save to the database
session.commit()

# query to get people whose names starts with Bro by using 'like' as used in sql
cust1=session.query(Person).filter(Person.name.like('%Bro%')).first()

print(cust1,cust1.addresses)

#another way to filter try getting the value of cust2 by using an exact match on their name
cust2 = session.query(Person).filter(Person.name=='Hayan Mohamed').first()
print(cust2,cust2.addresses)

# try deleting cust2 by their id
cust2_id = cust2.id
del cust2

def disp_info():
    # get all addresses
    addresses = session.query((Address)).all()

    # display the results
    for address in addresses:
        print(f'{address.person.name}<{address.email}>')

    # find how many objects there are in total
    print('people:{}, addresses:{}'.format(
        session.query(Person).count(),
        session.query(Address).count()
    ))

cust2=session.get(Person,cust2_id)
session.delete(cust2)
session.commit()

disp_info()#prints all the addresses, along with the respective person's name
