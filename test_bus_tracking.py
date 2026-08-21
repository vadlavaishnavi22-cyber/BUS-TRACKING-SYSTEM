import unittest
from bus_tracking import Bus, calculate_distance


class TestBusTracking(unittest.TestCase):

    def setUp(self):
        self.bus = Bus(
            "BUS101",
            "Route-A",
            16.5062,
            80.6480,
            35
        )

    def test_bus_creation(self):
        self.assertEqual(self.bus.bus_id, "BUS101")
        self.assertEqual(self.bus.route, "Route-A")
        self.assertEqual(self.bus.speed, 35)

    def test_initial_status(self):
        self.assertEqual(self.bus.status, "Stopped")

    def test_location_update(self):
        self.bus.update_location(16.5072, 80.6490)

        self.assertAlmostEqual(self.bus.latitude, 16.5072)
        self.assertAlmostEqual(self.bus.longitude, 80.6490)
        self.assertEqual(self.bus.status, "Moving")

    def test_stop_bus(self):
        self.bus.update_location(16.5072, 80.6490)
        self.bus.stop_bus()

        self.assertEqual(self.bus.status, "Stopped")

    def test_get_location(self):
        location = self.bus.get_location()

        self.assertEqual(location, (16.5062, 80.6480))

    def test_distance(self):
        distance = calculate_distance(
            16.5062,
            80.6480,
            16.5072,
            80.6490
        )

        self.assertGreater(distance, 0)


if __name__ == "__main__":
    unittest.main()
