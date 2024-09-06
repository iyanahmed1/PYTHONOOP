# INHERITANCE EXAMPLE FOR DIFFERENT ANIMALS
# single inheritance- only inherit one base class
#mutliple inheritance- inherit mutiple base classes
    #must be inside brackets, sepatred by 
    # class dervived class (baseClass1, baseClass2)
#multilevel inheritance- class inherits a base class and another class inherites the previously dervided class
    #parent, child, grandchild relationship
# hierarchial inheritance- only have one base class inherited by multiple 
#hybrid- blend of all the above 
class Animal():# this is our super class
    def eat(self):
        print('I can eat')
    def sleep(self):
        print('I can sleep')
    def sound(self):
        print('Animal sound')


animal = Animal()
#derive a class dog 
class Dog(Animal):
    def bark(self):
        print('I can bark')

# create a dog object that accesss all the members of the animal class
#call it simba
simba=Dog()
simba.eat()#calling from main class
simba.sleep()#calling from main class
simba.bark()# calling from the dervived class

#create a new class for cat that inherits the behaviour of animal
#try acessing the behaviour of dog
class Cat(Animal):
    def meows(self):
        print('I can mew')
    def sound(self):
        print('A cat mews')

kitty=Cat()
animal.sound()
kitty.sound()
kitty.eat()
kitty.sleep()
kitty.meows()
# multlevel inheritance
class GermanShepard(Dog):
    def protect(self):
        print('I am a protector')
Bruno=GermanShepard()
Bruno.bark()
Bruno.sleep() 
Bruno.eat()


