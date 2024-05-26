from connect import connectDB, connect_mysql, fetch_data_from_mongodb, create_table_and_insert_data
import bson
import random

# Code for Pilot in MongoDB

def insert_pilot(db, pilot_data):
    """Inserts or updates a single pilot document in the MongoDB pilots collection."""
    pilot_collection = db.pilots
    result = pilot_collection.update_one(
        {"PilotID": pilot_data["PilotID"]},  # Query matches documents with the same PilotID
        {"$set": pilot_data},  # Update the document with the data provided
        upsert=True  # Insert a new document if no matching document is found
    )
    if result.upserted_id is not None:
        return result.upserted_id
    else:
        return result.matched_count  # Return the number of documents matched, which should be 1 if updated

def input_document_data(prompts):
    """Collects user inputs based on given prompts"""
    data = {}
    for key, prompt in prompts.items():
        data[key] = input(prompt)  # Input values for each key based on the prompt.

    return data


def main():
    db = connectDB()

    # These are the samples that were added to MongoDB:

    pilot_samples = [
        {
            "PilotID": 1,
            "PilotName": "John Smith",
            "LicenseNumber": "A12345",
            "Age": 45,
            "Gender": "Male",
            "Nationality": "American",
            "Known_Languages": "English, Spanish",
            "Vehicle_Restriction": "Boeing 747, Airbus A320",
            "Seniority": "senior",
            "Pilot_Travel_Range": "Long-haul",
            "Availability": "2024-06-01,2024-06-03,2024-06-05,2024-06-07,2024-06-09"
        },
        {
            "PilotID": 2,
            "PilotName": "Emily Johnson",
            "LicenseNumber": "B23456",
            "Age": 38,
            "Gender": "Female",
            "Nationality": "British",
            "Known_Languages": "English, French",
            "Vehicle_Restriction": "Boeing 777, Airbus A380",
            "Seniority": "junior",
            "Pilot_Travel_Range": "Short-haul",
            "Availability": "2024-06-02,2024-06-04,2024-06-06,2024-06-08,2024-06-10"
        },
        {
            "PilotID": 3,
            "PilotName": "Carlos Ruiz",
            "LicenseNumber": "C34567",
            "Age": 50,
            "Gender": "Male",
            "Nationality": "Spanish",
            "Known_Languages": "Spanish, English",
            "Vehicle_Restriction": "Airbus A330",
            "Seniority": "senior",
            "Pilot_Travel_Range": "Long-haul",
            "Availability": "2024-06-01,2024-06-04,2024-06-07,2024-06-10,2024-06-13"
        },
        {
            "PilotID": 4,
            "PilotName": "Sophie Dubois",
            "LicenseNumber": "D45678",
            "Age": 33,
            "Gender": "Female",
            "Nationality": "French",
            "Known_Languages": "French, English",
            "Vehicle_Restriction": "Boeing 787",
            "Seniority": "trainee",
            "Pilot_Travel_Range": "Short-haul",
            "Availability": "2024-06-02,2024-06-05,2024-06-08,2024-06-11,2024-06-14"
        },
        {
            "PilotID": 5,
            "PilotName": "Liu Wei",
            "LicenseNumber": "E56789",
            "Age": 48,
            "Gender": "Male",
            "Nationality": "Chinese",
            "Known_Languages": "Mandarin, English",
            "Vehicle_Restriction": "Airbus A350",
            "Seniority": "junior",
            "Pilot_Travel_Range": "Long-haul",
            "Availability": "2024-06-01,2024-06-03,2024-06-06,2024-06-09,2024-06-12"
        },
        {
            "PilotID": 6,
            "PilotName": "Fatima Al-Fassi",
            "LicenseNumber": "F67890",
            "Age": 40,
            "Gender": "Female",
            "Nationality": "Moroccan",
            "Known_Languages": "Arabic, French, English",
            "Vehicle_Restriction": "Boeing 747",
            "Seniority": "senior",
            "Pilot_Travel_Range": "Long-haul",
            "Availability": "2024-06-02,2024-06-04,2024-06-06,2024-06-08,2024-06-10"
        },
        {
            "PilotID": 7,
            "PilotName": "Oliver Smith",
            "LicenseNumber": "G78901",
            "Age": 35,
            "Gender": "Male",
            "Nationality": "Australian",
            "Known_Languages": "English",
            "Vehicle_Restriction": "Boeing 737, Airbus A320",
            "Seniority": "junior",
            "Pilot_Travel_Range": "Short-haul",
            "Availability": "2024-06-03,2024-06-06,2024-06-09,2024-06-12,2024-06-15"
        },
        {
            "PilotID": 8,
            "PilotName": "Maria Fernández",
            "LicenseNumber": "H89012",
            "Age": 30,
            "Gender": "Female",
            "Nationality": "Mexican",
            "Known_Languages": "Spanish, English",
            "Vehicle_Restriction": "Airbus A380",
            "Seniority": "trainee",
            "Pilot_Travel_Range": "Long-haul",
            "Availability": "2024-06-04,2024-06-07,2024-06-10,2024-06-13,2024-06-16"
        },
        {
            "PilotID": 9,
            "PilotName": "Ahmad Hassan",
            "LicenseNumber": "I90123",
            "Age": 42,
            "Gender": "Male",
            "Nationality": "Egyptian",
            "Known_Languages": "Arabic, English",
            "Vehicle_Restriction": "Boeing 787",
            "Seniority": "junior",
            "Pilot_Travel_Range": "Short-haul",
            "Availability": "2024-06-02,2024-06-05,2024-06-08,2024-06-11,2024-06-14"
        },
        {
            "PilotID": 10,
            "PilotName": "Aisha Osei",
            "LicenseNumber": "J01234",
            "Age": 37,
            "Gender": "Female",
            "Nationality": "Ghanaian",
            "Known_Languages": "English, French",
            "Vehicle_Restriction": "Airbus A350",
            "Seniority": "senior",
            "Pilot_Travel_Range": "Long-haul",
            "Availability": "2024-06-01,2024-06-04,2024-06-07,2024-06-10,2024-06-13"
        },
        {
            "PilotID": 11,
            "PilotName": "Benjamin Lee",
            "LicenseNumber": "K12345",
            "Age": 43,
            "Gender": "Male",
            "Nationality": "Canadian",
            "Known_Languages": "English, French",
            "Vehicle_Restriction": "Boeing 737",
            "Seniority": "senior",
            "Pilot_Travel_Range": "Long-haul",
            "Availability": "2024-06-01,2024-06-03,2024-06-05,2024-06-07,2024-06-09"
        },
        {
            "PilotID": 12,
            "PilotName": "Nina Williams",
            "LicenseNumber": "L23456",
            "Age": 36,
            "Gender": "Female",
            "Nationality": "British",
            "Known_Languages": "English, German",
            "Vehicle_Restriction": "Airbus A320",
            "Seniority": "junior",
            "Pilot_Travel_Range": "Short-haul",
            "Availability": "2024-06-02,2024-06-04,2024-06-06,2024-06-08,2024-06-10"
        },
        {
            "PilotID": 13,
            "PilotName": "Kenji Yamamoto",
            "LicenseNumber": "M34567",
            "Age": 47,
            "Gender": "Male",
            "Nationality": "Japanese",
            "Known_Languages": "Japanese, English",
            "Vehicle_Restriction": "Boeing 777",
            "Seniority": "senior",
            "Pilot_Travel_Range": "Long-haul",
            "Availability": "2024-06-01,2024-06-03,2024-06-05,2024-06-07,2024-06-09"
        },
        {
            "PilotID": 14,
            "PilotName": "Isabella Rossi",
            "LicenseNumber": "N45678",
            "Age": 39,
            "Gender": "Female",
            "Nationality": "Italian",
            "Known_Languages": "Italian, English",
            "Vehicle_Restriction": "Airbus A330",
            "Seniority": "junior",
            "Pilot_Travel_Range": "Short-haul",
            "Availability": "2024-06-02,2024-06-04,2024-06-06,2024-06-08,2024-06-10"
        },
        {
            "PilotID": 15,
            "PilotName": "Ethan Brown",
            "LicenseNumber": "O56789",
            "Age": 34,
            "Gender": "Male",
            "Nationality": "American",
            "Known_Languages": "English",
            "Vehicle_Restriction": "Boeing 787",
            "Seniority": "trainee",
            "Pilot_Travel_Range": "Short-haul",
            "Availability": "2024-06-03,2024-06-05,2024-06-07,2024-06-09,2024-06-11"
        },
        {
            "PilotID": 16,
            "PilotName": "Hannah Müller",
            "LicenseNumber": "P67890",
            "Age": 41,
            "Gender": "Female",
            "Nationality": "German",
            "Known_Languages": "German, English",
            "Vehicle_Restriction": "Airbus A350",
            "Seniority": "senior",
            "Pilot_Travel_Range": "Long-haul",
            "Availability": "2024-06-01,2024-06-03,2024-06-05,2024-06-07,2024-06-09"
        },
        {
            "PilotID": 17,
            "PilotName": "Muhammad Ali",
            "LicenseNumber": "Q78901",
            "Age": 45,
            "Gender": "Male",
            "Nationality": "Pakistani",
            "Known_Languages": "Urdu, English",
            "Vehicle_Restriction": "Boeing 747",
            "Seniority": "junior",
            "Pilot_Travel_Range": "Long-haul",
            "Availability": "2024-06-02,2024-06-04,2024-06-06,2024-06-08,2024-06-10"
        },
        {
            "PilotID": 18,
            "PilotName": "Sara Gonzalez",
            "LicenseNumber": "R89012",
            "Age": 38,
            "Gender": "Female",
            "Nationality": "Spanish",
            "Known_Languages": "Spanish, English",
            "Vehicle_Restriction": "Airbus A320",
            "Seniority": "trainee",
            "Pilot_Travel_Range": "Short-haul",
            "Availability": "2024-06-03,2024-06-05,2024-06-07,2024-06-09,2024-06-11"
        },
        {
            "PilotID": 19,
            "PilotName": "Liam Patel",
            "LicenseNumber": "S90123",
            "Age": 32,
            "Gender": "Male",
            "Nationality": "Indian",
            "Known_Languages": "Hindi, English",
            "Vehicle_Restriction": "Boeing 777",
            "Seniority": "junior",
            "Pilot_Travel_Range": "Long-haul",
            "Availability": "2024-06-02,2024-06-04,2024-06-06,2024-06-08,2024-06-10"
        },
        {
            "PilotID": 20,
            "PilotName": "Chloe Wilson",
            "LicenseNumber": "T01234",
            "Age": 29,
            "Gender": "Female",
            "Nationality": "Australian",
            "Known_Languages": "English",
            "Vehicle_Restriction": "Boeing 737",
            "Seniority": "trainee",
            "Pilot_Travel_Range": "Short-haul",
            "Availability": "2024-06-01,2024-06-03,2024-06-05,2024-06-07,2024-06-09"
        }
    ]

    # for pilot_data in pilot_samples:
    #     insert_pilot(db, pilot_data)
    #     print(f"Inserted {pilot_data['PilotName']} with ID: {pilot_data['PilotID']}")

    pilot_prompts = {
        "PilotID": "Enter Pilot ID: ",
        "PilotName": "Enter Pilot Name: ",
        "LicenseNumber": "Enter License Number: ",
        "Age": "Enter Age: ",
        "Gender": "Enter Gender: ",
        "Nationality": "Enter Nationality of Pilot: ",
        "Known_Languages": "Enter Known languages: ",
        "Vehicle_Restriction": "Enter Vehicle restriction: ",
        "Seniority": "Enter Seniority Level (senior, junior, trainee): ",
        "Pilot_Travel_Range": "Enter Max distance that pilot can be assigned to: ",
        "Availability": "Enter Pilot's Availability Dates: (comma-separated, YYYY-MM-DD) ",

    }

    pilot_data = input_document_data(pilot_prompts)  # collects user input for each prompt.
    pilot_id = insert_pilot(db, pilot_data)  # Inserts data to mongoDB

    # The following code is for converting a specified MongoDB collection into a MySQL table

    #     engine, session = connect_mysql()
    #
    #     # Example: Transfer 'pilots' from MongoDB to a new MySQL table 'pilots_sql'
    #     collection_name = 'pilots'  # Adjust the collection name as needed
    #     data = fetch_data_from_mongodb(db, collection_name)
    #     if data:
    #         print(f"Fetched {len(data)} documents from MongoDB collection '{collection_name}'")
    #         create_table_and_insert_data(engine, data, 'passengers_sql')  # Adjust the SQL table name as needed
    #     else:
    #         print(f"No data found in MongoDB collection '{collection_name}'")
    #
if __name__ == '__main__':
    main()

