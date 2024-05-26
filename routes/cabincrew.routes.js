const express = require('express');
const CabinCrew = require('../models/CabinCrew'); // Import the updated CabinCrew model

const router = express.Router();

// GET route to retrieve all cabin crew members
router.get('/', async (req, res) => {
    try {
        const cabinCrew = await CabinCrew.find();
        res.json(cabinCrew);
        console.log(cabinCrew);
    } catch (err) {
        console.error('Error retrieving cabin crew members:', err); // Log the error
        res.status(500).json({ message: err.message });
    }
});

// GET route to retrieve a cabin crew member by ID
router.get('/:id', async (req, res) => {
    console.log('Received ID:', req.params.id); // Log the received ID
    try {
        const cabinCrew = await CabinCrew.findById(req.params.id);
        if (!cabinCrew) return res.status(404).json({ message: 'Cabin crew member not found' });
        res.json(cabinCrew);
    }catch (err) {
        console.error('Error retrieving cabin crew member:', err);
        res.status(500).json({ message: err.message });
    }
});

// POST route to create a new cabin crew member
router.post('/', async (req, res) => {
    const cabinCrew = new CabinCrew({
        CrewID: req.body.CrewID,
        Role: req.body.Role,
        MemberName: req.body.MemberName,
        Age: req.body.Age,
        "Aircraft Restrictions": req.body.AircraftRestrictions,
        Assigned_Seat: req.body.Assigned,
        Gender: req.body.Gender,
        "Known Languages": req.body.Known_Languages,
        Nationality: req.body.Nationality
    });
    try {
        const newCabinCrew = await cabinCrew.save();
        res.status(201).json(newCabinCrew);
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
});

// PATCH route to update a cabin crew member's name
router.patch('/:id', async (req, res) => {
    try {
        const cabinCrew = await CabinCrew.findById(req.params.id);
        if (!cabinCrew) return res.status(404).json({ message: 'Cabin crew member not found' });

        cabinCrew.MemberName = req.body.MemberName;
        const updatedCabinCrew = await cabinCrew.save();
        res.json(updatedCabinCrew);
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
});

// PATCH route to update a cabin crew member's role
router.patch('/:id', async (req, res) => {
    try {
        const cabinCrew = await CabinCrew.findById(req.params.id);
        if (!cabinCrew) return res.status(404).json({ message: 'Cabin crew member not found' });

        cabinCrew.Role = req.body.Role;
        const updatedCabinCrew = await cabinCrew.save();
        res.json(updatedCabinCrew);
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
});

// Endpoint to add a new chef
router.post('/chefs', async (req, res) => {
    const { CrewID, MemberName, Age, Gender, Nationality, Known_Languages, Aircraft_Restrictions, Dishes, Featured_Dish } = req.body;
    try {
        const newChef = new Chefs({
            CrewID,
            MemberName,
            Age,
            Gender,
            Nationality,
            Known_Languages,
            Aircraft_Restrictions,
            Dishes,
            Featured_Dish
        });
        await newChef.save();

        // Optionally, create a corresponding CabinCrew entry
        const newCabinCrew = new CabinCrew({
            CrewID,
            Age,
            Aircraft_Restrictions,
            ChefID: newChef._id,
            Gender,
            Known_Languages,
            MemberName,
            Nationality,
            Role: 'chef'
        });
        await newCabinCrew.save();

        res.status(201).json({ message: 'Chef and CabinCrew created successfully', newChef, newCabinCrew });
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

// Endpoint to update a chef
router.patch('/chefs/:id', async (req, res) => {
    const { id } = req.params;
    const updates = req.body;

    try {
        const updatedChef = await Chefs.findByIdAndUpdate(id, updates, { new: true });
        if (!updatedChef) {
            return res.status(404).json({ message: 'Chef not found' });
        }

        // Update the corresponding CabinCrew document if necessary
        const updatedCabinCrew = await CabinCrew.findOneAndUpdate(
            { ChefID: id },
            {
                Age: updatedChef.Age,
                Aircraft_Restrictions: updatedChef.Aircraft_Restrictions,
                Gender: updatedChef.Gender,
                Known_Languages: updatedChef.Known_Languages,
                MemberName: updatedChef.MemberName,
                Nationality: updatedChef.Nationality,
                Role: updatedChef.Role
            },
            { new: true }
        );

        res.json({ message: 'Chef and CabinCrew updated successfully', updatedChef, updatedCabinCrew });
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});


// PATCH route to update a cabin crew member's assigned seat
router.patch('/assign-seat/:id', async (req, res) => {
    // const crewid=req.params.crewid;
    try {
        const { id } = req.params; // Extract ID from URL parameters
        const { Assigned_Seat } = req.body; // Extract Assigned_Seat from request body

        // Validate that Assigned_Seat is provided
        if (!Assigned_Seat) {
            return res.status(400).json({ message: 'Assigned_Seat is required' });
        }

        const cabinCrew = await CabinCrew.findById(id); //CabinCrew.findOne({ CrewID: req.params.CrewID });
        if (!cabinCrew) return res.status(404).json({ message: 'Cabin crew member not found' });

        cabinCrew.Assigned_Seat = Assigned_Seat;
        const updatedCabinCrew = await cabinCrew.save();
        res.json(updatedCabinCrew);
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
});

//PATCH route to update a cabin crew member's age
router.patch('/:id', async (req, res) => {
    try {
        const cabinCrew = await CabinCrew.findById(req.params.id);
        if (!cabinCrew) return res.status(404).json({ message: 'Cabin crew member not found' });

        cabinCrew.Age = req.body.Age;
        const updatedCabinCrew = await cabinCrew.save();
        res.json(updatedCabinCrew);
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
});

//PATCH route to update a cabin crew member's aircraft restrictions
router.patch('/:id', async (req, res) => {
    try {
        const cabinCrew = await CabinCrew.findById(req.params.id);
        if (!cabinCrew) return res.status(404).json({ message: 'Cabin crew member not found' });

        cabinCrew.AircraftRestrictions = req.body.AircraftRestrictions;
        const updatedCabinCrew = await cabinCrew.save();
        res.json(updatedCabinCrew);
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
});

//PATCH route to update a cabin crew member's known languages
router.patch('/:id', async (req, res) => {
    try {
        const cabinCrew = await CabinCrew.findById(req.params.id);
        if (!cabinCrew) return res.status(404).json({ message: 'Cabin crew member not found' });

        cabinCrew.Known_Languages = req.body.Known_Languages;
        const updatedCabinCrew = await cabinCrew.save();
        res.json(updatedCabinCrew);
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
});

//PATCH route to update a cabin crew member's nationality
router.patch('/:id', async (req, res) => {
    try {
        const cabinCrew = await CabinCrew.findById(req.params.id);
        if (!cabinCrew) return res.status(404).json({ message: 'Cabin crew member not found' });  

        cabinCrew.Nationality = req.body.Nationality;
        const updatedCabinCrew = await cabinCrew.save();
        res.json(updatedCabinCrew);
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
});

// DELETE route to delete a cabin crew member by ID
router.delete('/:id', async (req, res) => {
    try {
        const cabinCrew = await CabinCrew.findById(req.params.id);
        if (!cabinCrew) return res.status(404).json({ message: 'Cabin crew member not found' });

        await cabinCrew.remove();
        res.json({ message: 'Cabin crew member deleted' });
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

module.exports = router;