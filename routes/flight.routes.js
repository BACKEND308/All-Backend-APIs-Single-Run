const express = require('express');
const Flight = require('../models/Flight'); // Import the updated Flight model

const router = express.Router();

// POST route to create a new flight
router.post('/flights', async (req, res) => {
  // Destructure all fields from req.body
  const {
    FlightNumber,
    Date,
    FlightDuration,
    FlightDistance,
    FlightSource,
    FlightDestination,
    VehicleType,
    SharedFlightInfo
  } = req.body;

  // List of required fields for easy management and error message generation
  const requiredFields = [
    { key: 'FlightNumber', name: 'Flight Number' },
    { key: 'Date', name: 'Date' },
    { key: 'FlightDuration', name: 'Flight Duration' },
    { key: 'FlightDistance', name: 'Flight Distance' },
    { key: 'FlightSource', name: 'Flight Source' },
    { key: 'FlightDestination', name: 'Flight Destination' },
    { key: 'VehicleType', name: 'Vehicle Type' }
  ];

  // Check for missing fields and collect all missing field names
  let missingFields = requiredFields
    .filter(field => req.body[field.key] === undefined)
    .map(field => field.name);

  // If there are missing fields, return an error message with the list of missing fields
  if (missingFields.length > 0) {
    return res.status(400).json({
      message: `Missing required fields: ${missingFields.join(', ')}`
    });
  }

  // Proceed with creation if all fields are present
  try {
    const newFlight = new Flight({
      FlightNumber,
      Date,
      FlightDuration,
      FlightDistance,
      FlightSource,
      FlightDestination,
      VehicleType,
      SharedFlightInfo
    });
    await newFlight.save();
    res.status(201).json(newFlight);
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
});


// GET route to retrieve all flights
router.get('/flights', async (req, res) => {
  try {
    const flights = await Flight.find();
    console.log(flights); // Log the fetched flights to the console
    res.status(200).json(flights);
  } catch (error) {
    console.error("Error fetching flights:", error);
    res.status(500).json({ error: error.message });
  }
});


// GET route to retrieve a single flight by FlightNumber
router.get('/flights/:FlightNumber', async (req, res) => {
  try {
    const flight = await Flight.findOne({ FlightNumber: req.params.FlightNumber });
    if (!flight) {
      return res.status(404).send('Flight not found');
    }
    res.json(flight);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// PATCH route to update a flight by FlightNumber
router.patch('/flights/:FlightNumber', async (req, res) => {
  try {
    const flight = await Flight.findOneAndUpdate(
      { FlightNumber: req.params.FightNumber },
      req.body,
      { new: true }
    );
    if (!flight) {
      return res.status(404).send('Flight not found');
    }
    res.json(flight);
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

// DELETE route to delete a flight by FlightNumber
router.delete('/flights/:FlightNumber', async (req, res) => {
  try {
    const result = await Flight.findOneAndDelete({ FlightNumber: req.params.FlightNumber });
    if (!result) {
      return res.status(404).send('Flight not found');
    }
    res.send({ message: 'Flight deleted successfully' });
  } catch (error) {
    res.status(500).json({ error: error.getCode() });
  }
});

module.exports = router;
