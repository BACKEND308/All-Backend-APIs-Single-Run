const express = require('express');
// const Roster = require('../models/Roster'); // Import the updated CabinCrew model
const PassengerInfo = require('../models/Passenger');
const CabinCrew = require('../models/CabinCrew');
const Pilot = require('../models/Pilot');

const router = express.Router();

//GET route combining all the information
router.get('/all', async (req, res) => {
    try {
        const passengerInfo = await PassengerInfo.find();
        const cabinCrew = await CabinCrew.find();
        const pilots = await Pilot.find();

        res.json({passengerInfo, cabinCrew, pilots});
    } catch (err) {
        console.error('Error retrieving roster entries:', err); // Log the error
        res.status(500).json({ message: err.message });
    }
});

module.exports = router; // Export the router for use in the main app file