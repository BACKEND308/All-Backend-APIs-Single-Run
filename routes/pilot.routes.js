const express = require('express');
const Pilot= require('../models/Pilot');
const router = express.Router();

// Get all pilots
router.get('/', async (req, res) => {
  try {
    const pilots = await Pilot.find();
    res.json(pilots);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Get a single pilot by ID
router.get('/:id', async (req, res) => {
  try {
    const pilot = await Pilot.findById(req.params.id);
    if (!pilot) {
      return res.status(404).json({ error: 'Pilot not found' });
    }
    res.json(pilot);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Create a new pilot
router.post('/', async (req, res) => {
  try {
    const pilot = new Pilot(req.body);
    await pilot.save();
    res.status(201).json(pilot);
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

// Update a pilot by ID
router.put('/:id', async (req, res) => {
  try {
    const pilot = await Pilot.findByIdAndUpdate(req.params.id, req.body, { new: true, runValidators: true });
    if (!pilot) {
      return res.status(404).json({ error: 'Pilot not found' });
    }
    res.json(pilot);
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

// Delete a pilot by ID
router.delete('/:id', async (req, res) => {
  try {
    const pilot = await Pilot.findByIdAndDelete(req.params.id);
    if (!pilot) {
      return res.status(404).json({ error: 'Pilot not found' });
    }
    res.json({ message: 'Pilot deleted' });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;