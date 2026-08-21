import csv
import math
import time


class Bus:
    def __init__(self, bus_id, route, latitude, longitude, speed):
        self.bus_id = bus_id
        self.route = route
        self.latitude = float(latitude)
        self.longitude = float(longitude)
        self.speed = float(speed)
        self.status = "Stopped"

    def update_location(self, latitude, longitude):
        self.latitude = float(latitude)
        self.longitude = float(longitude)
        self.status = "Moving"

    def stop_bus(self):
        self.status = "Stopped"

    def get_location(self):
        return self.latitude, self.longitude

    def display_info(self):
        print(f"Bus ID   : {self.bus_id}")
        print(f"Route    : {self.route}")
        print(f"Location : ({self.latitude:.4f}, {self.longitude:.4f})")
        print(f"Speed    : {self.speed:.1f} km/h")
        print(f"Status   : {self.status}")
        print("-" * 35)


def calculate_distance(lat1, lon1, lat2, lon2):
    """
    Calculate approximate distance between two GPS coordinates.
    Result is returned in kilometers.
    """

    earth_radius = 6371

    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)

    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(lat1)
        * math.cos(lat2)
        * math.sin(dlon / 2) ** 2
    )

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return earth_radius * c


def load_buses(filename):
    buses = []

    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            bus = Bus(
                row["bus_id"],
                row["route"],
                row["latitude"],
                row["longitude"],
                row["speed"]
            )
            buses.append(bus)

    return buses


def simulate_tracking(buses, iterations=3):
    print("\nBUS TRACKING SYSTEM")
    print("=" * 35)

    for iteration in range(1, iterations + 1):
        print(f"\nSimulation Update {iteration}")
        print("-" * 35)

        for bus in buses:
            # Small simulated GPS movement
            new_latitude = bus.latitude + 0.001
            new_longitude = bus.longitude + 0.001

            bus.update_location(new_latitude, new_longitude)
            bus.display_info()

        time.sleep(1)


def main():
    filename = "bus_data.csv"

    try:
        buses = load_buses(filename)

        print("Loaded buses:")
        for bus in buses:
            bus.display_info()

        simulate_tracking(buses)

    except FileNotFoundError:
        print(f"Error: {filename} not found.")


if __name__ == "__main__":
    main()
