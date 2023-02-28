class car:
    def __init__(self,model,make,year,engine_capacity):
        self.model = model
        self.make = make
        self.year = year
        self.engine_capacity = engine_capacity

    def get_model(self):
        return self.model

    def get_make(self):
        return self.make

    def get_year(self):
        return self.year

    def get_engine_capacity(self):
        return self.engine_capacity



car1 = car("demio","mazda","2019",1300)
car2 = car("deluxe","toyota","2020",3500)
car3 = car("passat","vw","2009",2600)

print(car1.get_model())
print(car1.get_year())

print(car2.get_model())
print(car2.get_year())

print(car3.get_model())
print(car3.get_year())