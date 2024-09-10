from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import column,Interger,String,ForeignKey,create_engine
from sqlalchemy.orm import relationship

class Person(base):
    __tablename__='person'
    id=column(Interger,primary_key=True)
    name=column(String)
    age=column(Interger)

addresses=relationship('Address',
            back_populate='person',
            order_by='Address.email',
            cascade='all,delete-orphan')


    