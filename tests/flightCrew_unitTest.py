import unittest
import requests

BASE_URL = "http://localhost:3000/api"  # Sunucunuzun adresini ve portunu burada belirtin

class TestPilotsAPI(unittest.TestCase):

    def setUp(self):
        self.pilot = {
            "PilotID": "1",
            "Name": "John Smith",
            "Rank": "Captain",
            "FlightHours": 5000,
            "LicenseNumber": "ABC123",
            "AircraftType": "Boeing 737",
            "BaseAirport": "JFK",
            "Nationality": "USA"
        }
        self.invalid_pilot = {
            "PilotID": "2",
            "Name": "Jane Smith",
            "Rank": "Captain",
            "FlightHours": -10,  # Invalid flight hours
            "LicenseNumber": "DEF456",
            "AircraftType": "Airbus A320",
            "BaseAirport": "LAX",
            "Nationality": "USA"
        }
        self.created_id = None

    def test_create_pilot(self):
        response = requests.post(f"{BASE_URL}/pilots", json=self.pilot)
        self.assertEqual(response.status_code, 201)
        self.created_id = response.json()["_id"]

    def test_create_invalid_pilot(self):
        response = requests.post(f"{BASE_URL}/pilots", json=self.invalid_pilot)
        self.assertNotEqual(response.status_code, 201)
        self.assertIn("error", response.json())

    def test_get_all_pilots(self):
        response = requests.get(f"{BASE_URL}/pilots")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_get_pilot_by_id(self):
        if self.created_id is None:
            self.test_create_pilot()  # Ensure we have a created ID
        response = requests.get(f"{BASE_URL}/pilots/{self.created_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["_id"], self.created_id)

    def test_get_nonexistent_pilot_by_id(self):
        response = requests.get(f"{BASE_URL}/pilots/000000000000000000000000")
        self.assertEqual(response.status_code, 404)

    def test_update_pilot_by_id(self):
        if self.created_id is None:
            self.test_create_pilot()  # Ensure we have a created ID
        update_data = {"Name": "Jane Doe"}
        response = requests.put(f"{BASE_URL}/pilots/{self.created_id}", json=update_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["Name"], "Jane Doe")

    def test_update_nonexistent_pilot_by_id(self):
        update_data = {"Name": "Jane Doe"}
        response = requests.put(f"{BASE_URL}/pilots/000000000000000000000000", json=update_data)
        self.assertEqual(response.status_code, 404)

    def test_delete_pilot_by_id(self):
        if self.created_id is None:
            self.test_create_pilot()  # Ensure we have a created ID
        response = requests.delete(f"{BASE_URL}/pilots/{self.created_id}")
        self.assertEqual(response.status_code, 200)

    def test_delete_nonexistent_pilot_by_id(self):
        response = requests.delete(f"{BASE_URL}/pilots/000000000000000000000000")
        self.assertEqual(response.status_code, 404)

if __name__ == "__main__":
    unittest.main()
