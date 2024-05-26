from rosterConnect import connectDB,connect_mysql, fetch_data_from_mongodb, create_table_and_insert_data
import random


# ROSTER ENTRY INSERT FUNCTION
def insert_roster_entry(db, flight_number, pilot_id, crew_ids, date, passenger_ids):
    """Inserts a roster entry document into the MongoDB collection."""
    roster_entry_collection = db.roster_entry
    roster_entry_data = {
        "FlightNumber": flight_number,
        "PilotID": pilot_id,
        "CrewIDs": crew_ids,
        "Date": date,
        "PassengerIDs": passenger_ids
    }
    result = roster_entry_collection.insert_one(roster_entry_data)
    return result.inserted_id

def main():
    db = connectDB()

    sample_roster_entries = [
        {
            "FlightNumber": "FL5271",
            "PilotID": 1,
            "CrewIDs": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "Date": "2024-05-01",
            "PassengerIDs": ["PAS12358"]
        },
        {
            "FlightNumber": "FL2089",
            "PilotID": 2,
            "CrewIDs": [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            "Date": "2024-05-02",
            "PassengerIDs": ["PAS12349", "PAS12359"]
        },
        {
            "FlightNumber": "FL8137",
            "PilotID": 3,
            "CrewIDs": [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
            "Date": "2024-05-03",
            "PassengerIDs": ["PAS12350", "PAS12360"]
        },
        {
            "FlightNumber": "FL3691",
            "PilotID": 4,
            "CrewIDs": [31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
            "Date": "2024-05-04",
            "PassengerIDs": ["PAS12351", "PAS12361"]
        },
        {
            "FlightNumber": "FL4088",
            "PilotID": 5,
            "CrewIDs": [41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
            "Date": "2024-05-05",
            "PassengerIDs": ["PAS12352", "PAS12362"]
        },
        {
            "FlightNumber": "FL1265",
            "PilotID": 6,
            "CrewIDs": [51, 52, 53, 54, 55, 56, 57, 58, 59, 60],
            "Date": "2024-05-07",
            "PassengerIDs": ["PAS12354", "PAS12364"]
        },
        {
            "FlightNumber": "FL5121",
            "PilotID": 7,
            "CrewIDs": [61, 62, 63, 64, 65, 66, 67, 68, 69, 70],
            "Date": "2024-05-06",
            "PassengerIDs": ["PAS12353", "PAS12363"]
        },
        {
            "FlightNumber": "FL5860",
            "PilotID": 8,
            "CrewIDs": [71, 72, 73, 74, 75, 76, 77, 78, 79, 80],
            "Date": "2024-05-08",
            "PassengerIDs": ["PAS12355", "PAS12365"]
        },
        {
            "FlightNumber": "FL3027",
            "PilotID": 9,
            "CrewIDs": [81, 82, 83, 84, 85, 86, 87, 88, 89, 90],
            "Date": "2024-05-09",
            "PassengerIDs": ["PAS12356", "PAS12366"]
        },
        {
            "FlightNumber": "FL3880",
            "PilotID": 10,
            "CrewIDs": [91, 92, 93, 94, 95, 96, 97, 98, 99, 100],
            "Date": "2024-05-10",
            "PassengerIDs": ["PAS12357", "PAS12367"]
        }
    ]

    # for roster_entry in sample_roster_entries:
    #     roster_entry_id = insert_roster_entry(
    #         db,
    #         roster_entry["FlightNumber"],
    #         roster_entry["PilotID"],
    #         roster_entry["CrewIDs"],
    #         roster_entry["Date"],
    #         roster_entry["PassengerIDs"]
    #     )
    #     print(f"Inserted roster entry with ID: {roster_entry_id}")

if __name__ == '__main__':
    main()
