# Parent Class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"{self.brand} {self.model}"


# Child Class 
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)  # inheritance
        self.storage = storage
        self.battery = battery

    def call(self, number):
        return f" Calling {number} using {self.device_info()}..."

    def charge(self):
        return f" {self.device_info()} is charging..."


# Creating objects
phone1 = Smartphone("Samsung", "S24 Ultra", "256GB", "5000mAh")
phone2 = Smartphone("Apple", "iPhone 15", "128GB", "4200mAh")

print(phone1.call("0712345678"))
print(phone2.charge())
