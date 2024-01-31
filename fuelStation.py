class FuelStation:
    def __init__(self, diesel, petrol, electric):
        self.available_slots = {
            'diesel': diesel,
            'petrol': petrol,
            'electric': electric
        }

        self.total_slots = {
            'diesel': diesel,
            'petrol': petrol,
            'electric': electric
        }

    def fuel_vehicle(self, fuel_type):
        if fuel_type not in self.available_slots or self.available_slots[fuel_type] == 0:
            return False

        self.available_slots[fuel_type] -= 1
        return True

    def open_fuel_slot(self, fuel_type):
        if fuel_type not in self.available_slots:
            return False

        if self.available_slots[fuel_type] < self.total_slots[fuel_type]:
            self.available_slots[fuel_type] += 1
            return True

        return False

fuel_station = FuelStation(diesel=2, petrol=2, electric=1)

print(fuel_station.fuel_vehicle("diesel"))
print(fuel_station.fuel_vehicle("petrol"))
print(fuel_station.fuel_vehicle("diesel"))
print(fuel_station.fuel_vehicle("electric"))
print(fuel_station.fuel_vehicle("diesel"))
print(fuel_station.open_fuel_slot("diesel"))
print(fuel_station.fuel_vehicle("diesel"))
print(fuel_station.open_fuel_slot("electric"))
print(fuel_station.open_fuel_slot("electric"))
