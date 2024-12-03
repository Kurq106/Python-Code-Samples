# Kimberly Urquiza
# Date
# Problem 6

class Car:
    # Initializes a car with model, year, color, type, and manufacturer attributes
    def __init__(self, model, year, color, car_type, manufacturer):
        self.model = model
        self.year = year
        self.color = color
        self.car_type = car_type
        self.manufacturer = manufacturer

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_color(self):
        return self.color

    def get_type(self):
        return self.car_type

    def get_manufacturer(self):
        return self.manufacturer

    def fullspecs(self):
        # Returns a full description including model, year, color, type, and manufacturer
        return f"{self.manufacturer} {self.model}, {self.year}, {self.color}, Type: {self.car_type}"

# Test
car1 = Car("Sports", 2012, "Blue", "Convertible", "Ford")
car2 = Car("Sedan", 2020, "Black", "SUV", "Toyota")

print(car1.get_color())
print(car1.get_model())
print(car2.get_manufacturer())
print(car1.fullspecs())
print(car2.fullspecs())
