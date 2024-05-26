from connect import connectDB,connect_mysql, fetch_data_from_mongodb, create_table_and_insert_data

def insert_flight_information(db, flight_information_data):
    flight_information_collection = db.flight_information
    result = flight_information_collection.insert_one(flight_information_data)
    print(f"Inserted flight information with ID: {result.inserted_id}")

def main():
    db = connectDB()
   
      
    flight_information_data = [
    {
        "FlightNumber": "FL5271",
        "Date": "2024-05-01T15:00:00Z",
        "FlightDuration": "03:00",
        "FlightDistance": 2475,
        "FlightSource": {
            "Country": "USA",
            "City": "New York",
            "AirportName": "John F. Kennedy International Airport",
            "AirportCode": "JFK"
        },
        "FlightDestination": {
            "Country": "USA",
            "City": "Los Angeles",
            "AirportName": "Los Angeles International Airport",
            "AirportCode": "LAX"
        },
        "VehicleType": {
            "Model": "Boeing 737",
            "Capacity": 188,
            "StandardMenu": "Standard Menu"
        },
        "SharedFlightInfo": {
            "SharedFlightNumber": "TR1234",
            "SharedFlightCompany": "Turkish Airlines",
            "ConnectingFlightInfo": {
                "FlightNumber": "LH5678",
                "Company": "Lufthansa",
                "DepartureTime": "2024-05-01T21:00:00Z"
            }
        }
    },
    {
        "FlightNumber": "FL2089",
        "Date": "2024-05-02T16:00:00Z",
        "FlightDuration": "02:45",
        "FlightDistance": 2140,
        "FlightSource": {
            "Country": "USA",
            "City": "Chicago",
            "AirportName": "O'Hare International Airport",
            "AirportCode": "ORD"
        },
        "FlightDestination": {
            "Country": "USA",
            "City": "San Francisco",
            "AirportName": "San Francisco International Airport",
            "AirportCode": "SFO"
        },
        "VehicleType": {
            "Model": "Airbus A320",
            "Capacity": 150,
            "StandardMenu": "Vegetarian Menu"
        },
        "SharedFlightInfo": {
            "SharedFlightNumber": "AA5678",
            "SharedFlightCompany": "American Airlines",
            "ConnectingFlightInfo": {
                "FlightNumber": "BA1234",
                "Company": "British Airways",
                "DepartureTime": "2024-05-02T20:00:00Z"
            }
        }
    },
    {
        "FlightNumber": "FL8137",
        "Date": "2024-05-03T14:30:00Z",
        "FlightDuration": "04:00",
        "FlightDistance": 3000,
        "FlightSource": {
            "Country": "USA",
            "City": "Miami",
            "AirportName": "Miami International Airport",
            "AirportCode": "MIA"
        },
        "FlightDestination": {
            "Country": "Canada",
            "City": "Toronto",
            "AirportName": "Toronto Pearson International Airport",
            "AirportCode": "YYZ"
        },
        "VehicleType": {
            "Model": "Boeing 777",
            "Capacity": 300,
            "StandardMenu": "Premium Menu"
        },
        "SharedFlightInfo": {
            "SharedFlightNumber": "UA6789",
            "SharedFlightCompany": "United Airlines",
            "ConnectingFlightInfo": {
                "FlightNumber": "AC3456",
                "Company": "Air Canada",
                "DepartureTime": "2024-05-03T19:00:00Z"
            }
        }
    },
    {
        "FlightNumber": "FL3691",
        "Date": "2024-05-04T10:00:00Z",
        "FlightDuration": "05:00",
        "FlightDistance": 4000,
        "FlightSource": {
            "Country": "USA",
            "City": "Dallas",
            "AirportName": "Dallas/Fort Worth International Airport",
            "AirportCode": "DFW"
        },
        "FlightDestination": {
            "Country": "Mexico",
            "City": "Mexico City",
            "AirportName": "Benito Juárez International Airport",
            "AirportCode": "MEX"
        },
        "VehicleType": {
            "Model": "Boeing 747",
            "Capacity": 400,
            "StandardMenu": "Mexican Menu"
        },
        "SharedFlightInfo": {
            "SharedFlightNumber": "DL7890",
            "SharedFlightCompany": "Delta Airlines",
            "ConnectingFlightInfo": {
                "FlightNumber": "AM5678",
                "Company": "Aeromexico",
                "DepartureTime": "2024-05-04T16:00:00Z"
            }
        }
    },
    {
        "FlightNumber": "FL4088",
        "Date": "2024-05-05T18:00:00Z",
        "FlightDuration": "02:30",
        "FlightDistance": 1800,
        "FlightSource": {
            "Country": "USA",
            "City": "Houston",
            "AirportName": "George Bush Intercontinental Airport",
            "AirportCode": "IAH"
        },
        "FlightDestination": {
            "Country": "USA",
            "City": "Atlanta",
            "AirportName": "Hartsfield-Jackson Atlanta International Airport",
            "AirportCode": "ATL"
        },
        "VehicleType": {
            "Model": "Airbus A330",
            "Capacity": 250,
            "StandardMenu": "Southern Menu"
        },
        "SharedFlightInfo": {
            "SharedFlightNumber": "SW1234",
            "SharedFlightCompany": "Southwest Airlines",
            "ConnectingFlightInfo": {
                "FlightNumber": "DL3456",
                "Company": "Delta Airlines",
                "DepartureTime": "2024-05-05T21:00:00Z"
            }
        }
    },
    {
        "FlightNumber": "FL5121",
        "Date": "2024-05-06T07:00:00Z",
        "FlightDuration": "01:45",
        "FlightDistance": 1200,
        "FlightSource": {
            "Country": "USA",
            "City": "Boston",
            "AirportName": "Logan International Airport",
            "AirportCode": "BOS"
        },
        "FlightDestination": {
            "Country": "Canada",
            "City": "Montreal",
            "AirportName": "Montreal-Pierre Elliott Trudeau International Airport",
            "AirportCode": "YUL"
        },
        "VehicleType": {
            "Model": "Boeing 757",
            "Capacity": 200,
            "StandardMenu": "Canadian Menu"
        },
        "SharedFlightInfo": {
            "SharedFlightNumber": "AC1234",
            "SharedFlightCompany": "Air Canada",
            "ConnectingFlightInfo": {
                "FlightNumber": "WS5678",
                "Company": "WestJet",
                "DepartureTime": "2024-05-06T10:00:00Z"
            }
        }
    },
    {
        "FlightNumber": "FL1265",
        "Date": "2024-05-07T12:00:00Z",
        "FlightDuration": "02:15",
        "FlightDistance": 1600,
        "FlightSource": {
            "Country": "USA",
            "City": "Denver",
            "AirportName": "Denver International Airport",
            "AirportCode": "DEN"
        },
        "FlightDestination": {
            "Country": "USA",
            "City": "Seattle",
            "AirportName": "Seattle-Tacoma International Airport",
            "AirportCode": "SEA"
        },
        "VehicleType": {
            "Model": "Airbus A380",
            "Capacity": 500,
            "StandardMenu": "Seafood Menu"
        },
        "SharedFlightInfo": {
            "SharedFlightNumber": "UA1234",
            "SharedFlightCompany": "United Airlines",
            "ConnectingFlightInfo": {
                "FlightNumber": "AS3456",
                "Company": "Alaska Airlines",
                "DepartureTime": "2024-05-07T16:00:00Z"
            }
        }
    },
    {
        "FlightNumber": "FL5860",
        "Date": "2024-05-08T19:00:00Z",
        "FlightDuration": "03:30",
        "FlightDistance": 2200,
        "FlightSource": {
            "Country": "USA",
            "City": "Philadelphia",
            "AirportName": "Philadelphia International Airport",
            "AirportCode": "PHL"
        },
        "FlightDestination": {
            "Country": "USA",
            "City": "Orlando",
            "AirportName": "Orlando International Airport",
            "AirportCode": "MCO"
        },
        "VehicleType": {
            "Model": "Boeing 737 Max",
            "Capacity": 190,
            "StandardMenu": "Orlando Menu"
        },
        "SharedFlightInfo": {
            "SharedFlightNumber": "JB1234",
            "SharedFlightCompany": "JetBlue Airways",
            "ConnectingFlightInfo": {
                "FlightNumber": "WN5678",
                "Company": "Southwest Airlines",
                "DepartureTime": "2024-05-08T23:00:00Z"
            }
        }
    },
    {
        "FlightNumber": "FL3027",
        "Date": "2024-05-09T08:00:00Z",
        "FlightDuration": "01:30",
        "FlightDistance": 900,
        "FlightSource": {
            "Country": "USA",
            "City": "Las Vegas",
            "AirportName": "McCarran International Airport",
            "AirportCode": "LAS"
        },
        "FlightDestination": {
            "Country": "USA",
            "City": "Phoenix",
            "AirportName": "Phoenix Sky Harbor International Airport",
            "AirportCode": "PHX"
        },
        "VehicleType": {
            "Model": "Airbus A350",
            "Capacity": 280,
            "StandardMenu": "Desert Menu"
        },
        "SharedFlightInfo": {
            "SharedFlightNumber": "SW3456",
            "SharedFlightCompany": "Southwest Airlines",
            "ConnectingFlightInfo": {
                "FlightNumber": "UA6789",
                "Company": "United Airlines",
                "DepartureTime": "2024-05-09T11:00:00Z"
            }
        }
    },
    {
        "FlightNumber": "FL3880",
        "Date": "2024-05-10T06:00:00Z",
        "FlightDuration": "05:30",
        "FlightDistance": 3500,
        "FlightSource": {
            "Country": "USA",
            "City": "Washington, D.C.",
            "AirportName": "Washington Dulles International Airport",
            "AirportCode": "IAD"
        },
        "FlightDestination": {
            "Country": "UK",
            "City": "London",
            "AirportName": "Heathrow Airport",
            "AirportCode": "LHR"
        },
        "VehicleType": {
            "Model": "Boeing 787",
            "Capacity": 260,
            "StandardMenu": "British Menu"
        },
        "SharedFlightInfo": {
            "SharedFlightNumber": "BA4321",
            "SharedFlightCompany": "British Airways",
            "ConnectingFlightInfo": {
                "FlightNumber": "VS5678",
                "Company": "Virgin Atlantic",
                "DepartureTime": "2024-05-10T12:00:00Z"
            }
        }
    }
]

    # for data in flight_information_data:
    #     insert_flight_information(db, data)

     # # Example: Transfer 'flight_info' from MongoDB to a new MySQL table 'flight_sql'
    # collection_name = 'flight_information'  # Adjust the collection name as needed
    # data = fetch_data_from_mongodb(db, collection_name)  
    # if data:
    #     print(f"Fetched {len(data)} documents from MongoDB collection '{collection_name}'")
    #     create_table_and_insert_data(engine, data, 'flights_sql')  # Adjust the SQL table name as needed
    # else:
    #     print(f"No data found in MongoDB collection '{collection_name}'")

  
if __name__ == '__main__':
    main()
