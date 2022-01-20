class My_ABC_Class(object):
    def set_val(self,val):
        return
    def get_val(self):
        return
class MyClass(My_ABC_Class):
    def set_val(self,input):
        self.val=input
    def hello(self):
        print("\nCalling the hello() method")
        print("I'm *not* part of the Abstract Methods defined in My_ABC_Class()")

my_class=MyClass()

my_class.set_val(10)
print(my_class.get_val())
my_class.hello()
class My_ABC_class(object):
    def set_val(self,val):
        return
    def get_val(self,val):
        return
class MyClass(My_ABC_Class)
    def set_val
