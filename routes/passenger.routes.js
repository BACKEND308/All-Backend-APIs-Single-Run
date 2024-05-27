const express= require('express');
const Passenger=require( '../models/Passenger');
const FlightTable = require('../models/FlightTable');
const { findClosestAvailableSeat } = require('../utils/seatUtils');
const mongoose = require('mongoose');

const router = express.Router();

// Get all passengers
router.get('/', async (req, res) => {
  try {
    const passengers = await Passenger.find();
    res.json(passengers);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Get a single passenger by ID
router.get('/:id', async (req, res) => {
  try {
    const passenger = await Passenger.findById(req.params.id);
    if (!passenger) {
      return res.status(404).json({ error: 'Passenger not found' });
    }
    res.json(passenger);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

router.post('/', async (req, res) => {
  try {
    const { with_a_Child, child, Seat_assigned, Flight_id, ...passengerData } = req.body;

    const flight = await FlightTable.findOne({ FlightNumber: Flight_id });
    if (!flight) {
      return res.status(404).json({ error: 'Flight not found' });
    }

    let assignedSeat = Seat_assigned || findClosestAvailableSeat(flight.Seats);

    if (assignedSeat && flight.Seats.get(assignedSeat) === 1) {
      const closestSeat = findClosestAvailableSeat(flight.Seats, assignedSeat);
      if (!closestSeat) {
        return res.status(400).json({ error: 'No available seats' });
      }
      assignedSeat = closestSeat;
      const parentPassenger = new Passenger({
        ...passengerData,
        with_a_Child: with_a_Child || false,
        Seat_assigned: assignedSeat,
        Flight_id
      });
      await parentPassenger.save();
      // Update seat availability
      if (assignedSeat) {
        flight.Seats.set(assignedSeat, 1);
      }
      await flight.save();
      return res.status(400).json({ error: `The seat ${Seat_assigned} is already picked. The nearest one (${closestSeat}) has been reserved for you.` });
    }

    // Create the parent passenger
    const parentPassenger = new Passenger({
      ...passengerData,
      with_a_Child: with_a_Child || false,
      Seat_assigned: assignedSeat,
      Flight_id
    });
    await parentPassenger.save();

    // Update seat availability
    if (assignedSeat) {
      flight.Seats.set(assignedSeat, 1);
    }

    // If the passenger has a child, create the child passenger
    if (with_a_Child && child) {
      let childSeat = assignedSeat; // Assume the same seat for simplicity, can be modified as needed
      if (childSeat && flight.Seats.get(childSeat) === 1) {
        childSeat = findClosestAvailableSeat(flight.Seats, childSeat);
        if (!childSeat) {
          return res.status(400).json({ error: 'No available seats for child' });
        }
      }

      const childPassengerData = {
        ...child,
        Seat_assigned: childSeat,
        Flight_id,
        ParentInfo: parentPassenger._id,
        AffiliatedPassengerIDs: []
      };

      const childPassenger = new Passenger(childPassengerData);
      await childPassenger.save();

      // Update seat availability for the child
      if (childSeat) {
        flight.Seats.set(childSeat, 1);
      }

      // Update the parent passenger with the child's ID
      parentPassenger.AffiliatedPassengerIDs.push(childPassenger._id);
      await parentPassenger.save();
    }

    await flight.save();

    res.status(201).json(parentPassenger);
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});



// Update a passenger by ID


router.put('/:id', async (req, res) => {
  try {
    // Ensure the ID is a valid ObjectId
    if (!mongoose.Types.ObjectId.isValid(req.params.id)) {
      return res.status(400).json({ error: 'Invalid passenger ID' });
    }

    // Step 1: Find the parent passenger by their ID
    const passenger = await Passenger.findById(req.params.id);
    if (!passenger) {
      return res.status(404).json({ error: 'Passenger not found' });
    }

    // Step 2: Find the corresponding flight by FlightNumber
    const flight = await FlightTable.findOne({ FlightNumber: passenger.Flight_id });
    if (!flight) {
      return res.status(404).json({ error: 'Flight not found' });
    }

    // Step 3: Handle seat assignment
    let newSeat = req.body.Seat_assigned || passenger.Seat_assigned;
    const oldSeat = passenger.Seat_assigned;

    if (newSeat && newSeat !== oldSeat) {
      // Check if the new seat is available
      if (flight.Seats.get(newSeat) === 1) {
        // Find the nearest available seat if the desired seat is taken
        const closestSeat = findClosestAvailableSeat(flight.Seats, newSeat);
        if (!closestSeat) {
          return res.status(400).json({ error: 'No available seats' });
        }
        // Assign the closest seat and update the flight's seat map
        flight.Seats.set(closestSeat, 1);
        flight.Seats.set(oldSeat, 0); // Make the old seat available
        newSeat = closestSeat; // Assign the closest seat
        req.body.Seat_assigned = closestSeat; // Update the request body with the new seat
      } else {
        // Update the old seat to be available
        flight.Seats.set(oldSeat, 0);
        // Assign the new seat
        flight.Seats.set(newSeat, 1);
      }
    }

    // Step 4: Update the parent's seat assignment
    passenger.Seat_assigned = newSeat;

    // Step 5: Update child passengers if any
if (passenger.AffiliatedPassengerIDs) {
  for (let childId of passenger.AffiliatedPassengerIDs) {
    // Find the child passenger by their Passenger_id
    const childPassenger = await Passenger.findOne({ Passenger_id: childId });

    if (childPassenger) {

      
      // Update the child's Parent_info to reflect the new seat assignment of the parent
      if (childPassenger.Parent_info && childPassenger.Parent_info.length > 0) {
        childPassenger.Parent_info[0].Seat_assigned = newSeat;
      }

      // Save the updated child passenger document
      await childPassenger.save();
    }
  }
}


    // Update the parent passenger with any additional request body data
    Object.assign(passenger, req.body);
    // Save the updated parent passenger document
    await passenger.save();
    // Save the updated flight document
    await flight.save();

    // Respond with the updated parent passenger document
    res.json(passenger);
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

// Delete a passenger by ID
router.delete('/:id', async (req, res) => {
  try {
    const passenger = await Passenger.findByIdAndDelete(req.params.id);
    if (!passenger) {
      return res.status(404).json({ error: 'Passenger not found' });
    }

    // Find the corresponding flight
    const flight = await FlightTable.findOne({ FlightNumber: passenger.Flight_id });
    if (flight) {
      // Remove the passenger's seat assignment
      if (passenger.Seat_assigned) {
        flight.Seats.set(passenger.Seat_assigned, 0); // Set the seat as available
        await flight.save();
      }
    }

    res.json({ message: 'Passenger deleted' });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;