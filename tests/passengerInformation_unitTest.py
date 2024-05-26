import unittest
import requests

BASE_URL = "http://localhost:3000/api"  # Sunucunuzun adresini ve portunu burada belirtin

class TestPassengersAPI(unittest.TestCase):

    def setUp(self):
        self.passenger = {
            "FirstName": "John",
            "LastName": "Doe",
            "PassportNumber": "A12345678",
            "Nationality": "USA",
            "DateOfBirth": "1990-01-01",
            "Gender": "Male",
            "with_a_Child": False
        }
        self.passenger_with_child = {
            "FirstName": "Jane",
            "LastName": "Doe",
            "PassportNumber": "B87654321",
            "Nationality": "USA",
            "DateOfBirth": "1992-02-02",
            "Gender": "Female",
            "with_a_Child": True,
            "child": {
                "FirstName": "Baby",
                "LastName": "Doe",
                "PassportNumber": "C12345678",
                "Nationality": "USA",
                "DateOfBirth": "2022-03-03",
                "Gender": "Female"
            }
        }
        self.invalid_passenger = {
            "FirstName": "Invalid",
            "LastName": "Passenger",
            "PassportNumber": "",  # Invalid passport number
            "Nationality": "USA",
            "DateOfBirth": "2000-01-01",
            "Gender": "Male",
            "with_a_Child": False
        }
        self.created_id = None

    def test_create_passenger(self):
        response = requests.post(f"{BASE_URL}/passengers", json=self.passenger)
        self.assertEqual(response.status_code, 201)
        self.created_id = response.json()["_id"]

    def test_create_passenger_with_child(self):
        response = requests.post(f"{BASE_URL}/passengers", json=self.passenger_with_child)
        self.assertEqual(response.status_code, 201)
        self.assertIn("AffiliatedPassengerIDs", response.json())
        self.assertTrue(len(response.json()["AffiliatedPassengerIDs"]) > 0)

    def test_create_invalid_passenger(self):
        response = requests.post(f"{BASE_URL}/passengers", json=self.invalid_passenger)
        self.assertNotEqual(response.status_code, 201)
        self.assertIn("error", response.json())

    def test_get_all_passengers(self):
        response = requests.get(f"{BASE_URL}/passengers")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_get_passenger_by_id(self):
        if self.created_id is None:
            self.test_create_passenger()  # Ensure we have a created ID
        response = requests.get(f"{BASE_URL}/passengers/{self.created_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["_id"], self.created_id)

    def test_get_nonexistent_passenger_by_id(self):
        response = requests.get(f"{BASE_URL}/passengers/000000000000000000000000")
        self.assertEqual(response.status_code, 404)

    def test_update_passenger_by_id(self):
        if self.created_id is None:
            self.test_create_passenger()  # Ensure we have a created ID
        update_data = {"FirstName": "Jane"}
        response = requests.put(f"{BASE_URL}/passengers/{self.created_id}", json=update_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["FirstName"], "Jane")

    def test_update_nonexistent_passenger_by_id(self):
        update_data = {"FirstName": "Jane"}
        response = requests.put(f"{BASE_URL}/passengers/000000000000000000000000", json=update_data)
        self.assertEqual(response.status_code, 404)

    def test_delete_passenger_by_id(self):
        if self.created_id is None:
            self.test_create_passenger()  # Ensure we have a created ID
        response = requests.delete(f"{BASE_URL}/passengers/{self.created_id}")
        self.assertEqual(response.status_code, 200)

    def test_delete_nonexistent_passenger_by_id(self):
        response = requests.delete(f"{BASE_URL}/passengers/000000000000000000000000")
        self.assertEqual(response.status_code, 404)

if __name__ == "__main__":
    unittest.main()
