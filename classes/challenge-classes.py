class Vehicle:
    def __init__(self, make = 'NaN', model = 'NaN', year = 2019, weight = 0):
        self.vehicleMake = make
        self.vehicleModel = model
        self.vehicleYear = year 
        self.vehicleWeight = weight
        self.vehicleNeedMaintence = False
        self.vehicleTripSinceMaintenance = 0


    def setMake(self, make):
        self.vehicleMake = make

    def setModel(self, model):
        self.vehicleModel = model 
    
    def setYear(self, year):
        self.vehicleYear = year

    def setWeight(self, weight):
        self.vehicleWeight = weight

    
    def repair(self):
        self.vehicleNeedMaintence = False
        self.vehicleTripSinceMaintenance = 0

    
    
class Cars(Vehicle):
    def __init__(self, make="NaN", model="NaN", year=1900, weight=0):
        Vehicle.__init__(self, make, model, year, weight)
        self.carIsDriving = False


    def drive(self):
        self.carIsDriving = True

    def stop(self):
        self.carIsDriving = False
        if self.carIsDriving is True:
            self.vehicleTripSinceMaintenance += 1
        elif self.vehicleTripSinceMaintenance > 100:
            self.vehicleNeedMaintence = True

    def __str__(self):
        return "Car Info: " + self.vehicleMake + "\n" 

bmw = Cars(make='BMW', model='i8', year=2019, weight=4000)
tesla = Cars(make='tesla', model='mode 2', year=2019, weight=4000)
toyota = Cars(make='toyota', model='prius', year=2019, weight=4000)
    

print(bmw)
print(bmw.vehicleMake)
print(bmw.vehicleNeedMaintence)
bmw.drive()
bmw.stop()
bmw.repair()
print(bmw.vehicleNeedMaintence)
print(tesla.vehicleMake)

