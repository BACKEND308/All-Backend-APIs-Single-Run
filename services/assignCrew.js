const CrewBusy = require('../models/CrewBusy');
const Flight = require('../models/Flight');
const FlightTable = require('../models/FlightTable');
const moment = require('moment');

function computeArrivalTime(departureTime, duration) {
  const [hours, minutes] = duration.split(':').map(Number);
  return moment(departureTime).add(hours, 'hours').add(minutes, 'minutes').toDate();
}

async function assignCrewToFlight(flightId) {
  try {
    const flight = await Flight.findById(flightId).populate('VehicleType');
    const departureTime = new Date(flight.Date);
    const arrivalTime = computeArrivalTime(departureTime, flight.FlightDuration);

    const suitableCrews = await CrewBusy.find({
      Aircraft_Restrictions: flight.VehicleType.Model,
      busy_times: {
        $not: {
          $elemMatch: {
            arrival: { $lt: departureTime },
            departure: { $gt: arrivalTime }
          }
        }
      }
    }).sort({ number_of_works: 1 });

    const chiefs = suitableCrews.filter(crew => crew.Role === 'chief');
    const regulars = suitableCrews.filter(crew => crew.Role === 'regular');
    const chefs = suitableCrews.filter(crew => crew.Role === 'chef');

    if (chiefs.length === 0 || regulars.length < 4) {
      return { success: false, message: 'Not enough crew available.' };
    }

    const selectedChief = chiefs[0];
    selectedChief.busy_times.push({ arrival: arrivalTime, departure: departureTime });
    selectedChief.number_of_works += 1;
    await selectedChief.save();

    const selectedRegulars = regulars.slice(0, 4);
    for (let crew of selectedRegulars) {
      crew.busy_times.push({ arrival: arrivalTime, departure: departureTime });
      crew.number_of_works += 1;
      await crew.save();
    }

    const selectedChef = chefs.length > 0 ? chefs[0] : null;
    if (selectedChef) {
      selectedChef.busy_times.push({ arrival: arrivalTime, departure: departureTime });
      selectedChef.number_of_works += 1;
      await selectedChef.save();
    }

    await FlightTable.updateOne(
      { _id: flight._id },
      {
        $set: {
          chief_crews: [selectedChief.CrewID],
          reg_crews: selectedRegulars.map(crew => crew.CrewID),
          Chef: selectedChef ? [selectedChef.CrewID] : []
        }
      },
      { upsert: true }
    );

    return { success: true, flight };
  } catch (err) {
    return { success: false, message: err.message };
  }
}

module.exports = assignCrewToFlight;
