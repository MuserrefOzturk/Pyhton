class Circle:
    pi=3.14

    def __init__(self,radius=1):
        self.radius=radius

    def area(self):
        return self.pi*(self.radius**2)

    def circumference(self):
        return 2*self.pi*self.radius

c1=Circle()
c2=Circle(5)

print(f'c1; area:{c1.area()} circumference:{c1.circumference()}')
print(f'c2; area:{c2.area()} circumference:{c2.circumference()}')