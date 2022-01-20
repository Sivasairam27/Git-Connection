class Person:
    name="SivajSaiRam"
    def sayName(self):
        print("My name is...",self.name)

def main():
    aPerson=Person()
    aPerson.sayName()
    aPerson.name="Siva"
    aPerson.sayName()
main()