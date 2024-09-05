"""#class computer
#double underscore before a variable name creates a private variable 
class Computer():
    def __init__(self):#we used the __init__ method to store the max price
        self.__maxprice=900#this price is only accesed under the computer

    def sell(self):
        print('Selling Price: {}'.format(self.__maxprice))

    def setMaxPrice(self,price):
        self.__maxprice=price

c=Computer()#creating  an object of the class computer
c.sell()#accessing the sell function under computer

#modify the price
c.__maxprice=1000# this selling price is not seen by our function since it is a private variable 
c.sell()

c.setMaxPrice(1000)
c.sell()"""
#encapsulation- data hiding 
#private attribute= we use a single or double underscore to identify a private attribute

#polymorphism- many forms
#same entity(method, or operator or object) performing different operations 
# different scenarios
class Polygon():# this is a superclass
    #create a method ot render a shape
    def render(self):
        print('Rendering a polygon...')

#create another class to create a square out of the polygon
class Square(Polygon):
    #render the square
    def render(self):
        print('Rendering a square...')
# create a  class circle out of the polygon
class circle(Polygon):
    # render the circle
    def render(self):
        print('Rendering the circle...')

#create an object out of the square
s1=Square()
s1.render()

#create an object of circle and assign the render method
c1=circle()
c1.render()