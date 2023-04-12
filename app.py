import random

class parking_lot:
    def __init__(self,sq_ft, width = 8, length = 12):
        self.sq_ft = sq_ft
        self.length = length
        self.width = width
        self.area = width*length
        self.spots = sq_ft//self.area
        self.parking_spots = [None]*self.spots

    def look_empty_spot(self):
        empty_spots = []
        for i,s in enumerate(self.parking_spots):
            if s is None:
                empty_spots.append(i)
        if empty_spots:
            return random.choice(empty_spots)
        return None

class Car:
    def __init__(self, license_plate):
        self.license_plate = license_plate
    
    def __str__(self):
        return self.license_plate

    def park(self, parking, spot):
        if parking.parking_spots[spot] is not None:
            return False
        parking.parking_spots[spot] = self
        return True
    
def main():
    parking = parking_lot(2000)  # create a parking lot with 2000 square footage
    cars = [Car ("CAR%05d" % i) for i in range(1, 21)]  # create an array of 20 cars with random license plates
    for car in cars:
        spot = None
        while spot is None:
            spot = parking.look_empty_spot()
        if car.park(parking, spot):
            print(f"Car with license plate {car} parked successfully in spot {spot}")
        else:
            print(f"Car with license plate {car} could not be parked in spot {spot}")

if __name__ == '__main__':
    main()
    
