from persons import Person, Address, engine
from sqlalchemy.orm import sessionmaker

Session=sessionmaker(bind=engine)
session=Session()

cust1=Person(name='Bronson Loni',age=24)
cust2=Person(name='Hayyan Mohamed',age=23)

cust1.addresses=[
    Address(email='Lonithebron@gmail.com'),
    Address(email='hloni@gmail.com'),
]

#append the addreses to the specific customer
cust1.addresses.append(Address(email='bron@gmail.com'))

#use the session maker to add data into the database
session.add(cust1)
session.add(cust2)

#run the commit to save to the database
session.commit()

cust1=session.query(Person).filter(Person.name.like('%Bro%')).first

print(cust1,cust1.addresses)
def disp_info():
    addresses=session.query((Address)).all()

    for address in addresses:
        print(f"{address.person }")