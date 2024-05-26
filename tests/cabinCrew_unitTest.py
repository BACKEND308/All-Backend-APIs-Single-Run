import unittest
import requests

BASE_URL = "http://localhost:3000/api"  # Sunucunuzun adresini ve portunu burada belirtin

class TestCabinCrewAPI(unittest.TestCase):

    def setUp(self):
        self.cabin_crew = {
            "CrewID": "1",
            "Role": "Attendant",
            "MemberName": "John Doe",
            "AssignedSeat": "A1",
            "Age": 30,
            "AircraftRestrictions": "None",
            "Gender": "Male",
            "Known_Languages": ["English"],
            "Nationality": "USA"
        }
        self.invalid_cabin_crew = {
            "CrewID": "2",
            "Role": "Attendant",
            "MemberName": "Jane Doe",
            "AssignedSeat": "A2",
            "Age": -5,  # Invalid age
            "AircraftRestrictions": "None",
            "Gender": "Female",
            "Known_Languages": ["English"],
            "Nationality": "USA"
        }
        self.created_id = None

    def test_create_cabin_crew(self):
        response = requests.post(f"{BASE_URL}/cabincrew", json=self.cabin_crew)
        self.assertEqual(response.status_code, 201)
        self.created_id = response.json()["_id"]

    def test_create_invalid_cabin_crew(self):
        response = requests.post(f"{BASE_URL}/cabincrew", json=self.invalid_cabin_crew)
        self.assertNotEqual(response.status_code, 201)
        self.assertIn("error", response.json())

    def test_get_all_cabin_crew(self):
        response = requests.get(f"{BASE_URL}/cabincrew")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_get_cabin_crew_by_id(self):
        if self.created_id is None:
            self.test_create_cabin_crew()  # Ensure we have a created ID
        response = requests.get(f"{BASE_URL}/cabincrew/{self.created_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["_id"], self.created_id)

    def test_get_nonexistent_cabin_crew_by_id(self):
        response = requests.get(f"{BASE_URL}/cabincrew/000000000000000000000000")
        self.assertEqual(response.status_code, 404)

    def test_update_cabin_crew_by_id(self):
        if self.created_id is None:
            self.test_create_cabin_crew()  # Ensure we have a created ID
        update_data = {"MemberName": "Jane Doe"}
        response = requests.patch(f"{BASE_URL}/cabincrew/{self.created_id}", json=update_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["MemberName"], "Jane Doe")

    def test_update_nonexistent_cabin_crew_by_id(self):
        update_data = {"MemberName": "Jane Doe"}
        response = requests.patch(f"{BASE_URL}/cabincrew/000000000000000000000000", json=update_data)
        self.assertEqual(response.status_code, 404)

    def test_delete_cabin_crew_by_id(self):
        if self.created_id is None:
            self.test_create_cabin_crew()  # Ensure we have a created ID
        response = requests.delete(f"{BASE_URL}/cabincrew/{self.created_id}")
        self.assertEqual(response.status_code, 200)

    def test_delete_nonexistent_cabin_crew_by_id(self):
        response = requests.delete(f"{BASE_URL}/cabincrew/000000000000000000000000")
        self.assertEqual(response.status_code, 404)

if __name__ == "__main__":
    unittest.main()
