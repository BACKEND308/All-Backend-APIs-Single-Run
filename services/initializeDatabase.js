const Pilot = require('../models/Pilot');
const PilotBusy = require('../models/PilotBusy');
const CabinCrew = require('../models/CabinCrew');
const Chefs = require('../models/Chefs');
const CrewBusy = require('../models/CrewBusy');
const Flight = require('../models/Flight');
const FlightTable = require('../models/FlightTable');
const Passenger = require('../models/Passenger');
const { generateSeatsDictionary } = require('../utils/seatUtils');
const assignPilotToFlight = require('./assignPilot');
const assignCrewToFlight = require('./assignCrew');

async function markOccupiedSeats() {
  const passengers = await Passenger.find({ Seat_assigned: { $ne: null } });
  for (let passenger of passengers) {
    const flight = await FlightTable.findOne({ FlightNumber: passenger.Flight_id });
    if (flight) {
      flight.Seats.set(passenger.Seat_assigned, 1);
      await flight.save();
    }
  }
}

async function initializeDatabase() {
  // Initialize pilots
  const pilots = await Pilot.find();
  for (let pilot of pilots) {
    await PilotBusy.updateOne(
      { pilot_id: pilot.PilotID },
      {
        pilot_id: pilot.PilotID,
        pilot_name: pilot.PilotName,
        pilot_seniority: pilot.Seniority,
        pilot_vehicle_restrictions: pilot.Vehicle_Restriction.split(', '),
        busy_times: []
      },
      { upsert: true }
    );
  }

  // Initialize cabin crew
  const cabinCrew = await CabinCrew.find();
  for (let crew of cabinCrew) {
    await CrewBusy.updateOne(
      { CrewID: crew.CrewID },
      {
        CrewID: crew.CrewID,
        MemberName: crew.MemberName,
        Aircraft_Restrictions: crew.Aircraft_Restrictions,
        crew_type: 'cabin',
        Role: crew.Role,
        busy_times: []
      },
      { upsert: true }
    );
  }

  // Initialize chefs
  const chefs = await Chefs.find();
  for (let chef of chefs) {
    await CrewBusy.updateOne(
      { CrewID: chef.CrewID },
      {
        CrewID: chef.CrewID,
        MemberName: chef.MemberName,
        Aircraft_Restrictions: chef.Aircraft_Restrictions,
        crew_type: 'cabin',
        Role: chef.Role,
        busy_times: []
      },
      { upsert: true }
    );
  }

  // Assign pilots and crews to all existing flights and update flight_table
  const flights = await Flight.find();
  for (let flight of flights) {
    const seats = generateSeatsDictionary(flight.VehicleType.Capacity);

    await FlightTable.updateOne(
      { FlightNumber: flight.FlightNumber },
      {
        $set: {
          FlightNumber: flight.FlightNumber,
          VehicleType: flight.VehicleType.Model,
          Seats: seats
        }
      },
      { upsert: true }
    );

    await assignPilotToFlight(flight.FlightNumber);
    await assignCrewToFlight(flight.FlightNumber);
  }

  // Mark occupied seats
  await markOccupiedSeats();
}

module.exports = initializeDatabase;
