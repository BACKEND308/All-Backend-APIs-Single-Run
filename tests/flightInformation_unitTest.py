import unittest
import requests

BASE_URL = "http://localhost:3000/api"  # Sunucunuzun adresini ve portunu burada belirtin

class TestFlightsAPI(unittest.TestCase):

    def setUp(self):
        self.flight = {
            "FlightNumber": "AA123",
            "DepartureAirport": "JFK",
            "ArrivalAirport": "LAX",
            "FlightDate": "2024-06-01",
            "DepartureTime": "10:00",
            "ArrivalTime": "13:00",
            "Price": 300
        }
        self.invalid_flight = {
            "FlightNumber": "AA124",
            "DepartureAirport": "JFK",
            "ArrivalAirport": "LAX",
            "FlightDate": "2024-06-01",
            "DepartureTime": "10:00",
            "ArrivalTime": "13:00",
            "Price": -100  # Invalid price
        }
        self.created_flight_number = None

    def test_create_flight(self):
        response = requests.post(f"{BASE_URL}/flights", json=self.flight)
        self.assertEqual(response.status_code, 201)
        self.created_flight_number = response.json()["FlightNumber"]

    def test_create_invalid_flight(self):
        response = requests.post(f"{BASE_URL}/flights", json=self.invalid_flight)
        self.assertNotEqual(response.status_code, 201)
        self.assertIn("error", response.json())

    def test_get_all_flights(self):
        response = requests.get(f"{BASE_URL}/flights")
        self.assertEqual(response.status_code, 200)
        self
