class Nothing:
    pass
print(Nothing)

class Hotel:
    def __init__(self, num_of_floors, num_of_rooms):
        self.num_of_rooms = num_of_floors
        self.num_of_floors = num_of_rooms

mumbai=Hotel(5,100)
print(f"Mumbai Hotel has {mumbai.num_of_rooms} rooms and {mumbai.num_of_floors} floors.")