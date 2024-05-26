const express = require('express');
const cors = require('cors');
require('dotenv').config();
const sequelize =require('./db/sequelize');
const connectMongo = require('./db/connectMongo');

//routes
const cabinCrewRoutes = require('./routes/cabincrew.routes');
const pilotRoutes = require('./routes/pilot.routes');
const flightRoutes = require('./routes/flight.routes');
const passengerRoutes = require('./routes/passenger.routes');
const rosterRoutes = require('./routes/roster.routes');
const userRoutes = require('./routes/user.routes');

const app = express();

// Middleware
app.use(cors());
app.use(express.json()); //for parsing application/json

//MongoDB connection
connectMongo();

// Connect to MySQL using Sequelize
sequelize.authenticate()
  .then(() => console.log('Sequelize successfully connected'))
  .catch(err => console.log('Sequelize connection error:', err));


//connect to routes
app.use('/api/cabincrew', cabinCrewRoutes);
app.use('/api/pilots', pilotRoutes);
app.use('/api', flightRoutes);
app.use('/api/passengers', passengerRoutes);
app.use('/api/roster', rosterRoutes);
app.use('/api/user', userRoutes);


//Define a simple route for testing, ping with 1
app.get('/api', (req, res) => {
    res.send('Hello World! This is the backend API.');
});

//Set the port and start the server
const port=process.env.PORT || 3000;
app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});