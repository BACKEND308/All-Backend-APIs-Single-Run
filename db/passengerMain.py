import os
from connect import connectDB,connect_mysql, fetch_data_from_mongodb, create_table_and_insert_data
from enum import Enum
import random
import string 

def insert_passenger_information(db, passenger_data):
    passenger_info_collection = db.passenger_info
    result = passenger_info_collection.insert_one(passenger_data)
    print(f"Inserted passenger information with ID: {result.inserted_id}")

def main():
    db = connectDB()
   
    data = [
        # # {
        # #     "Passenger_id": "PAS12345",
        # #     "Flight_id": "FL3691",
        # #     "Name": "Jane Doe",
        # #     "Age": 35,
        # #     "Gender": "Female",
        # #     "Nationality": "USA",
        # #     "Seat_type": "Business",
        # #     "Seat_assigned": "2B",
        # #     "AffiliatedPassengerIDs": None,
        # #     "Parent_info": None
        # # },
        # # {
        # #     "Passenger_id": "PAS12346",
        # #     "Flight_id": "FL3691",
        # #     "Name": "John Doe Jr.",
        # #     "Age": 5,
        # #     "Gender": "Male",
        # #     "Nationality": "USA",
        # #     "Seat_type": "Economy",
        # #     "Seat_assigned": None,
        # #     "AffiliatedPassengerIDs": ["PAS12345", "PAS12347"],
        # #     "Parent_info": None
        # # },
        # # {
        # #     "Passenger_id": "PAS12347",
        # #     "Flight_id": "FL3691",
        # #     "Name": "Baby Doe",
        # #     "Age": 1,
        # #     "Gender": "Female",
        # #     "Nationality": "USA",
        # #     "Seat_type": "Economy",
        # #     "Seat_assigned": None,
        # #     "AffiliatedPassengerIDs": None,
        # #     "Parent_info": [
        # #         {
        # #             "Parent_id": "PAS12345",
        # #             "Seat_assigned": "2B"
        # #         }
        # #     ]
        # # },
        # # {
        # #     "Passenger_id": "SOASGX",
        # #     "Flight_id": "FL4088",
        # #     "Name": "Passenger1",
        # #     "Age": 37,
        # #     "Gender": "Female",
        # #     "Nationality": "French",
        # #     "Seat_type": "Business",
        # #     "Seat_assigned": "12A",
        # #     "AffiliatedPassengerIDs": None,
        # #     "Parent_info": None
        # # }
        
        #  {
        #     "Passenger_id": "PAS12349",
        #     "Flight_id": "FL2089",
        #     "Name": "Bob Johnson",
        #     "Age": 42,
        #     "Gender": "Male",
        #     "Nationality": "British",
        #     "Seat_type": "Business",
        #     "Seat_assigned": "3A",
        #     "AffiliatedPassengerIDs": None,
        #     "Parent_info": None
        # },
        # {
        #     "Passenger_id": "PAS12350",
        #     "Flight_id": "FL8137",
        #     "Name": "Charlie Brown",
        #     "Age": 33,
        #     "Gender": "Male",
        #     "Nationality": "Australian",
        #     "Seat_type": "Economy",
        #     "Seat_assigned": "18F",
        #     "AffiliatedPassengerIDs": None,
        #     "Parent_info": None
        # },
        # {
        #     "Passenger_id": "PAS12351",
        #     "Flight_id": "FL3691",
        #     "Name": "David Wilson",
        #     "Age": 29,
        #     "Gender": "Male",
        #     "Nationality": "American",
        #     "Seat_type": "Economy",
        #     "Seat_assigned": "22D",
        #     "AffiliatedPassengerIDs": None,
        #     "Parent_info": None
        # },
        # {
        #     "Passenger_id": "PAS12352",
        #     "Flight_id": "FL4088",
        #     "Name": "Emma Taylor",
        #     "Age": 31,
        #     "Gender": "Female",
        #     "Nationality": "German",
        #     "Seat_type": "Business",
        #     "Seat_assigned": "4C",
        #     "AffiliatedPassengerIDs": None,
        #     "Parent_info": None
        # },
        # {
        #     "Passenger_id": "PAS12353",
        #     "Flight_id": "FL5121",
        #     "Name": "Frank Clark",
        #     "Age": 27,
        #     "Gender": "Male",
        #     "Nationality": "Italian",
        #     "Seat_type": "Economy",
        #     "Seat_assigned": "14B",
        #     "AffiliatedPassengerIDs": None,
        #     "Parent_info": None
        # },
        # {
        #     "Passenger_id": "PAS12354",
        #     "Flight_id": "FL1265",
        #     "Name": "Grace Lewis",
        #     "Age": 45,
        #     "Gender": "Female",
        #     "Nationality": "Spanish",
        #     "Seat_type": "Business",
        #     "Seat_assigned": "2D",
        #     "AffiliatedPassengerIDs": None,
        #     "Parent_info": None
        # },
        # {
        #     "Passenger_id": "PAS12355",
        #     "Flight_id": "FL5860",
        #     "Name": "Henry Walker",
        #     "Age": 39,
        #     "Gender": "Male",
        #     "Nationality": "Dutch",
        #     "Seat_type": "Economy",
        #     "Seat_assigned": "19E",
        #     "AffiliatedPassengerIDs": None,
        #     "Parent_info": None
        # },
        # {
        #     "Passenger_id": "PAS12356",
        #     "Flight_id": "FL3027",
        #     "Name": "Isabella Young",
        #     "Age": 34,
        #     "Gender": "Female",
        #     "Nationality": "Swiss",
        #     "Seat_type": "Business",
        #     "Seat_assigned": "1A",
        #     "AffiliatedPassengerIDs": None,
        #     "Parent_info": None
        # },
        # {
        #     "Passenger_id": "PAS12357",
        #     "Flight_id": "FL3880",
        #     "Name": "Jack Harris",
        #     "Age": 50,
        #     "Gender": "Male",
        #     "Nationality": "American",
        #     "Seat_type": "Economy",
        #     "Seat_assigned": "20C",
        #     "AffiliatedPassengerIDs": None,
        #     "Parent_info": None
        # }
        
    #      {
    #         "Passenger_id": "PAS12358",
    #         "Flight_id": "FL5271",
    #         "Name": "Kelly Morgan",
    #         "Age": 25,
    #         "Gender": "Female",
    #         "Nationality": "Canadian",
    #         "Seat_type": "Economy",
    #         "Seat_assigned": "16A",
    #         "AffiliatedPassengerIDs": None,
    #         "Parent_info": None
    #     },
    #     {
    #         "Passenger_id": "PAS12359",
    #         "Flight_id": "FL2089",
    #         "Name": "Leo King",
    #         "Age": 46,
    #         "Gender": "Male",
    #         "Nationality": "British",
    #         "Seat_type": "Business",
    #         "Seat_assigned": "3B",
    #         "AffiliatedPassengerIDs": None,
    #         "Parent_info": None
    #     },
    #     {
    #         "Passenger_id": "PAS12360",
    #         "Flight_id": "FL8137",
    #         "Name": "Mia Adams",
    #         "Age": 32,
    #         "Gender": "Female",
    #         "Nationality": "Australian",
    #         "Seat_type": "Economy",
    #         "Seat_assigned": "18A",
    #         "AffiliatedPassengerIDs": None,
    #         "Parent_info": None
    #     },
    #     {
    #         "Passenger_id": "PAS12361",
    #         "Flight_id": "FL3691",
    #         "Name": "Nathan White",
    #         "Age": 40,
    #         "Gender": "Male",
    #         "Nationality": "American",
    #         "Seat_type": "Economy",
    #         "Seat_assigned": "22A",
    #         "AffiliatedPassengerIDs": None,
    #         "Parent_info": None
    #     },
    #     {
    #         "Passenger_id": "PAS12362",
    #         "Flight_id": "FL4088",
    #         "Name": "Olivia Martin",
    #         "Age": 36,
    #         "Gender": "Female",
    #         "Nationality": "German",
    #         "Seat_type": "Business",
    #         "Seat_assigned": "4A",
    #         "AffiliatedPassengerIDs": None,
    #         "Parent_info": None
    #     },
    #     {
    #         "Passenger_id": "PAS12363",
    #         "Flight_id": "FL5121",
    #         "Name": "Paul Lee",
    #         "Age": 28,
    #         "Gender": "Male",
    #         "Nationality": "Italian",
    #         "Seat_type": "Economy",
    #         "Seat_assigned": "14C",
    #         "AffiliatedPassengerIDs": None,
    #         "Parent_info": None
    #     },
    #     {
    #         "Passenger_id": "PAS12364",
    #         "Flight_id": "FL1265",
    #         "Name": "Quinn Baker",
    #         "Age": 48,
    #         "Gender": "Female",
    #         "Nationality": "Spanish",
    #         "Seat_type": "Business",
    #         "Seat_assigned": "2E",
    #         "AffiliatedPassengerIDs": None,
    #         "Parent_info": None
    #     },
    #     {
    #         "Passenger_id": "PAS12365",
    #         "Flight_id": "FL5860",
    #         "Name": "Ryan Scott",
    #         "Age": 38,
    #         "Gender": "Male",
    #         "Nationality": "Dutch",
    #         "Seat_type": "Economy",
    #         "Seat_assigned": "19C",
    #         "AffiliatedPassengerIDs": None,
    #         "Parent_info": None
    #     },
    #     {
    #         "Passenger_id": "PAS12366",
    #         "Flight_id": "FL3027",
    #         "Name": "Sophie Green",
    #         "Age": 30,
    #         "Gender": "Female",
    #         "Nationality": "Swiss",
    #         "Seat_type": "Business",
    #         "Seat_assigned": "1B",
    #         "AffiliatedPassengerIDs": None,
    #         "Parent_info": None
    #     },
    #     {
    #         "Passenger_id": "PAS12367",
    #         "Flight_id": "FL3880",
    #         "Name": "Thomas Hall",
    #         "Age": 51,
    #         "Gender": "Male",
    #         "Nationality": "American",
    #         "Seat_type": "Economy",
    #         "Seat_assigned": "20D",
    #         "AffiliatedPassengerIDs": None,
    #         "Parent_info": None
    #     }
    ]
    

    # for passenger in data:
    #     insert_passenger_information(db, passenger)
    #     print(f"Inserted {passenger['Name']} with ID: {passenger['Passenger_id']}")




    # # Example: Transfer 'passenger_info' from MongoDB to a new MySQL table 'passenger_sql'
    # collection_name = 'passenger_info'  # Adjust the collection name as needed
    # data = fetch_data_from_mongodb(db, collection_name)  
    # if data:
    #     print(f"Fetched {len(data)} documents from MongoDB collection '{collection_name}'")
    #     create_table_and_insert_data(engine, data, 'passenger_sql')  # Adjust the SQL table name as needed
    # else:
    #     print(f"No data found in MongoDB collection '{collection_name}'")
if __name__ == '__main__':
    main()
