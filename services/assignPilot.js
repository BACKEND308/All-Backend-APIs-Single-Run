const PilotBusy = require('../models/PilotBusy');
const Flight = require('../models/Flight');
const FlightTable = require('../models/FlightTable');
const moment = require('moment');

function computeArrivalTime(departureTime, duration) {
  const [hours, minutes] = duration.split(':').map(Number);
  return moment(departureTime).add(hours, 'hours').add(minutes, 'minutes').toDate();
}

async function assignPilotToFlight(flightId) {
  try {
    const flight = await Flight.findById(flightId).populate('VehicleType');
    const departureTime = new Date(flight.Date);
    const arrivalTime = computeArrivalTime(departureTime, flight.FlightDuration);

    const suitablePilots = await PilotBusy.find({
      pilot_vehicle_restrictions: flight.VehicleType.Model,
      busy_times: {
        $not: {
          $elemMatch: {
            arrival: { $lt: departureTime },
            departure: { $gt: arrivalTime }
          }
        }
      }
    }).sort({ number_of_works: 1 });

    if (suitablePilots.length === 0) {
      return { success: false, message: 'No suitable pilot can be found.' };
    }

    const selectedPilot = suitablePilots[0];
    selectedPilot.busy_times.push({ arrival: arrivalTime, departure: departureTime });
    selectedPilot.number_of_works += 1;
    await selectedPilot.save();

    await FlightTable.updateOne(
      { _id: flight._id },
      { $set: { pilot_id: selectedPilot.pilot_id } },
      { upsert: true }
    );

    return { success: true, pilot: selectedPilot };
  } catch (err) {
    return { success: false, message: err.message };
  }
}

module.exports = assignPilotToFlight;
