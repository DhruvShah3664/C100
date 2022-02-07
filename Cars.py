class Car(object):
    def __init__(self, model, color, company, topSpeed):
        self.model = model
        self.color = color
        self.company = company
        self.topSpeed = topSpeed
    
    def start(self):
        print("Started")

    def stop(self):
        print("Stopped")
        
    def accelerate(self):
        print("accelerating...")
        "accelerated functionality here"

    def changeDriveMode(self):
        print("turned on autoDrive")


tesla = Car("ModelX", "white", "Tesla", 262)
print(tesla.start())
print(tesla.accelerate())
print(tesla.changeDriveMode())
print(tesla.stop())




