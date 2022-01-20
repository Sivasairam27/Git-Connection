class Encap(object):
    def set_speed(self,speed):
        self.speed=speed

    def get_speed(self,speed):
        print(self.speed)

a=Encap()
b=Encap()
a.set_speed(10)
b.set_speed(1000)
a.Speed=100

a.get_speed()
b.get_speed()