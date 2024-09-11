#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,ForeignKey,create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base

#create the database
engine=create_engine('sqlite:///customer.db')
Base=declarative_base()#this defines our base class for defining our actual models 

class Person(Base):
    __tablename__='person'
    id=Column(Integer,primary_key=True)
    name=Column(String)
    age=Column(Integer)

    addresses=relationship('Address',
            back_populates='person',
            order_by='Address.email',
            cascade='all,delete-orphan'
            )
def __repr__(self):# the __repr__ method provides the offical string represnting the object
    # repr= represntatoion is supposed to represtation that can be used to completely
    #  reconstruct the object to provide an output
    return f"{self.name}(id={self.id})"

class Address(Base):
    __tablename__='address'
    id=Column(Integer,primary_key=True)
    email=Column(String)
    person_id=Column(ForeignKey('person.id'))
    person=relationship('Person',
    back_populates='addresses')
def __str__(self):
    return self.email
__repr__=__str__# used to assign the __str__ method to the __repr__ method of the Address class
#therefore, when you call the __repr__ method ie, repr(), on an Address object 
# it    will also return the email addreses as a string in the representation


#creating tables
Base.metadata.create_all(engine)
#create_all is called to the metadata attribute of Base to create all the defined table 
# in the database we specified 