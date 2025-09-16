class Car:
    def move(self):
        return "Driving on the road!"


class Plane:
    def move(self):
        return " Flying in the sky!"


class Boat:
    def move(self):
        return " Sailing on the water!"


# Polymorphism 
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    print(v.move())
