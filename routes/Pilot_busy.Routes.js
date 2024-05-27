const express = require('express');
const router = express.Router();
const PilotBusy = require('../models/PilotBusy');

router.get('/pilot_busy', async (req, res) => {
  try {
    const pilots = await PilotBusy.find().select('pilot_id pilot_name pilot_seniority pilot_vehicle_restrictions number_of_works').sort('number_of_works');
    res.json(pilots);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

module.exports = router;
