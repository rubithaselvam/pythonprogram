import json  # store and transfer the data and it is human-readable data

class VehicleRental:
    def __init__(self, filename="rental_data.json"):
        self.filename = filename
        self.vehicles = self.load_data()

    def load_data(self):
        try:
            with open(self.filename, "r") as file:  # r refers to read the file
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {
                "car": {"total": 6, "available": 5, "rented": 1},
                "bike": {"total": 5, "available": 3, "rented": 1},
                "truck": {"total": 5, "available": 5, "rented": 0}
            }

    def save_data(self):
        try:
            with open(self.filename, "w") as file: # w refers to write a file
                json.dump(self.vehicles, file, indent=4)
        except Exception as e:
            print("Error saving rental data:", e)

    def view_vehicles(self):
        print("\n--- Available Vehicles ---")
        for vehicle, data in self.vehicles.items():
            print(f"{vehicle}: {data['available']} available, {data['rented']} rented")

    def rent_vehicle(self):
        self.view_vehicles()
        vehicle_type = input("\nEnter the vehicle type to rent: ").strip().lower()
        if vehicle_type in self.vehicles and self.vehicles[vehicle_type]["available"] > 0:
            self.vehicles[vehicle_type]["available"] -= 1
            self.vehicles[vehicle_type]["rented"] += 1
            self.save_data()
            print(f"{vehicle_type} rented successfully.")

            print("---- Updated Vehicle List ----")
            self.view_vehicles()  # Corrected this line to call view_vehicles()
        else:
            print("Vehicle not available for rent.")

    def return_vehicle(self):
        vehicle_type = input("\nEnter the vehicle type to return: ").strip().lower()  # title()
        if vehicle_type in self.vehicles and self.vehicles[vehicle_type]["rented"] > 0:
            self.vehicles[vehicle_type]["available"] += 1
            self.vehicles[vehicle_type]["rented"] -= 1
            self.save_data()
            print(f"{vehicle_type} returned successfully.")
        else:
            print("Invalid return! Either incorrect vehicle type or no rentals found.")

def main():
    rental_system = VehicleRental()

    while True:
        print("--- Vehicle Rental System ---")
        print("1. View Vehicles")
        print("2. Rent a Vehicle")
        print("3. Return a Vehicle")
        print("4. Exit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                rental_system.view_vehicles()
            elif choice == 2:
                rental_system.rent_vehicle()
            elif choice == 3:
                rental_system.return_vehicle()
            elif choice == 4:
                print("Exiting Vehicle Rental System. Drive safe!")
                break
            else:
                print("Invalid choice! Please enter a number between 1-4.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    main()










