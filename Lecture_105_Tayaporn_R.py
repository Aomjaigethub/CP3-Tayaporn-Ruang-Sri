class Vehicle:
    lecenseCode = ""
    serialCode = ""
    def turnOnAirConditioner(self):
        print("Turn On : Air")

    def enginestart(self):
        print("engine started")

class Pickup(Vehicle):
    color = ""
    brand = ""
    year = ""

class Van(Vehicle):
    color = ""
    brand = ""
    year = ""
    owner = ""

class Motorbike(Vehicle):
    color = ""
    brand = ""
    year = ""
    owner = ""
    engine = ""



pickup1 = Pickup()
pickup1.turnOnAirConditioner()
pickup1.color = "gray"

Van1 = Van()
Van1.enginestart()
Van1.turnOnAirConditioner()
Van1.owner = "Jakie chan"
Van1.year = "1992"

Motorbike1 = Motorbike()
Motorbike1.enginestart()
Motorbike1.turnOnAirConditioner()
Motorbike1.owner = "Mike Miller"
Motorbike1.engine = "300cc"

