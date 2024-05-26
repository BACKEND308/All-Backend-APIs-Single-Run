const express = require('express');
const Flight = require('../models/Flight'); // Import the updated Flight model

const router = express.Router();

// POST route to create a new flight
router.post('/flights', async (req, res) => {
  try {
    const newFlight = new Flight({
      FlightNumber: req.body.FlightNumber,
      Date: req.body.Date,
      FlightDuration: req.body.FlightDuration,
      FlightDistance: req.body.FlightDistance,
      FlightSource: req.body.FlightSource,
      FlightDestination: req.body.FlightDestination,
      VehicleType: req.body.VehicleType,
      SharedFlightInfo: req.body.SharedFlightInfo
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
