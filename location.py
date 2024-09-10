import person
class Address(base):
    __tablename__='address'
    id=column(interger,primary_key=True)
    email=column(string)
    person_id=colum(ForeignKey('person.id'))
    person=relationship('Person',
    back_populates='addresses')