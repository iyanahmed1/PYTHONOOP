"""import person
# create an object from person
man= person.Person()#qualify the object we want to create from the class
print(man.species)
print(man.alive)
#modifythe alive status of the person to false
person.Person.alive=False
print(man.alive)
#give the man a name
man.name="Bronson"
man.surname='Loni'
print(man.name,man.surname)"""

class sample_class:
    def __init__(self,course):
        self.course=course
    def display(self):
        print(self.course) 
object1= sample_class('python')
object1.display()