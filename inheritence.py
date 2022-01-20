class Animal(object):
    def __init__(self,name):
        self.name=name;
    def __int__(self,food):
        self.food=food;
class Dog(Animal):
    def fetch(self,thing):
        print("%s goes after the %s"%(self.name,thing))
class Cat(Animal):
    def swatstring(self):
            print("%s shread the string !"%(self.name, self))
d=Dog("bubbbby")
c=Cat("cutty")
d.fetch("paper")
d.eat("dog food")
print("---------")
c.eat("cat food")
c.swatstring()