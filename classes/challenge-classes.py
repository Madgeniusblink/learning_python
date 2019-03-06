class Vehicle:
    def __init__(self, make = '', model = '', year = 2019, weight = 0):
        self.vehicleMake = make
        self.vehicleModel = model
        self.vehicleYear = year 
        self.vehicleWeight = weight
        self.vechicleNeedMaintence = False
        self.vechicleTripSinceMaintenance = 0

    def setMake(self, make):
        self.vehicleMake = make

    def setModel(self, model):
        self.vehicleModel = model 
    
    def setYear(self, year):
        self.vehicleYear = year

    def setWeight(self, weight):
        self.vehicleWeight = weight
    
    def repair(self):
        self.vechicleNeedMaintence = False
        self.vechicleTripSinceMaintenance = 0

    
    
class Cars(Vehicle):
    def __init__(self, make="", model="", year=1900, weight=0):
        Vehicle.__init__(self, make, model, year, weight)
        self.carIsDriving = False


    def drive(self):
        self.carIsDriving = True

    def stop(self):
        self.carIsDriving = False
        if self.carIsDriving is True:
            self.vechicleTripSinceMaintenance += 1
        elif self.vechicleTripSinceMaintenance > 100:
            self.vechicleNeedMaintence = True



bmw = Cars(make='BMW', model='i8', year=2019, weight=4000)
tesla = Cars(make='tesla', model='mode 2', year=2019, weight=4000)
toyota = Cars(make='toyota', model='prius', year=2019, weight=4000)
    
def drive(car, times):
    for x in range(times):
        car.drive()
        car.stop()

print(bmw)
drive(tesla, 100)
print(tesla)

