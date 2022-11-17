class Vehicle:
    engine_capacity = "1, 6 Turbo"

    def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.type_of_tank = type_of_tank
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity

    def drive(self):
        print("The vehicle is in driving mode now.")

vios = Vehicle ('4', 'petrol', 5, 180)
print(vios.number_of_wheels)
print(vios.type_of_tank)
print(vios.seating_capacity)
print(vios.maximum_velocity)
vios.drive()

class ElectricCar(Vehicle):
    def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
        Vehicle.__init__(self, number_of_wheels, 'electric', seating_capacity, maximum_velocity)

blueSG = ElectricCar ('4', 'electric', '5', '150')
blueSG.drive()
print(blueSG.number_of_wheels)
print(blueSG.type_of_tank)
print(blueSG.seating_capacity)
print(blueSG.maximum_velocity)


#DIY

class Computer:
    def __init__(self, device_ram, storage_capacity, led_display, type_of_computer):
        self.device_ram = device_ram
        self.storage_capacity = storage_capacity
        self.led_display =  led_display
        self.type_of_computer = type_of_computer

    def playGame(self):
        print("My Computer is playing the game now.")


class Desktop(Computer):
    def __init__(self, device_ram, storage_capacity, led_display, type_of_computer):
        Computer.__init__(self, device_ram, storage_capacity, led_display, 'Desktop')


class Laptop(Computer):
    def __init__(self, device_ram, storage_capacity, led_display, type_of_computer):
        Computer.__init__(self, device_ram, storage_capacity, led_display, 'Laptop')


lenovo = Laptop ('16GB', '512GB', '15.6inch', 'lenovo')
print(lenovo.device_ram)
print(lenovo.storage_capacity)
print(lenovo.led_display)
print(lenovo.type_of_computer)
lenovo.playGame()



