const express= require('express');
const Passenger=require( '../models/Passenger');

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

// Create a new passenger
router.post('/', async (req, res) => {
  try {
    const { with_a_Child, child, ...passengerData } = req.body;

    // Create the parent passenger
    const parentPassenger = new Passenger({
      ...passengerData,
      with_a_Child: with_a_Child || false
    });
    await parentPassenger.save();

    // If the passenger has a child, create the child passenger
    if (with_a_Child && child) {
      const childPassengerData = {
        ...child,
        Seat_Assigned: parentPassenger.Seat_Assigned, // Assign the same seat number as the parent
        ParentInfo: parentPassenger._id,
        AffiliatedPassengerIDs: []
      };

      const childPassenger = new Passenger(childPassengerData);
      await childPassenger.save();

      // Update the parent passenger with the child's ID
      parentPassenger.AffiliatedPassengerIDs.push(childPassenger._id);
      await parentPassenger.save();
    }

    res.status(201).json(parentPassenger);
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

// Update a passenger by ID
router.put('/:id', async (req, res) => {
  try {
    const passenger = await Passenger.findByIdAndUpdate(req.params.id, req.body, { new: true, runValidators: true });
    if (!passenger) {
      return res.status(404).json({ error: 'Passenger not found' });
    }
    res.json(passenger);
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

// Delete a passenger by ID
router.delete('/:id', async (req, res) => {
  try {
    const passenger = await Passenger.findById(req.params.id);

    if (!passenger) {
      return res.status(404).json({ error: 'Passenger not found' });
    }

    // If the passenger has a child, delete the affiliated passengers (children)
    if (passenger.with_a_Child && passenger.AffiliatedPassengerIDs.length > 0) {
      await Passenger.deleteMany({ _id: { $in: passenger.AffiliatedPassengerIDs } });
    }

    // Delete the parent passenger
    await Passenger.findByIdAndDelete(req.params.id);

    res.json({ message: 'Passenger and affiliated passengers deleted' });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;