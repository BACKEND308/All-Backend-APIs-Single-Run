const express = require('express');
const cors = require('cors');
require('dotenv').config();
const connectMongo = require('./db/connectMongo');

//routes
const pilotBusyRoutes = require('./routes/pilot.routes');
const cabinCrewRoutes = require('./routes/cabincrew.routes');
const pilotRoutes = require('./routes/pilot.routes');
const flightRoutes = require('./routes/flight.routes');
const passengerRoutes = require('./routes/passenger.routes');
const rosterRoutes = require('./routes/roster.routes');
const userRoutes = require('./routes/user.routes');

const app = express();
//services
const initializeDatabase = require('./services/initializeDatabase');
const assignPilotToFlight  = require('./services/assignPilot');
const  assignCrewToFlight  = require('./services/assignCrew');
const Flight = require('./models/Flight');
// Middleware
app.use(cors());
app.use(express.json()); //for parsing application/json

//MongoDB connection
connectMongo();

// Connect to MySQL using Sequelize

//connect to routes
app.use('/api/pilotBusy', pilotBusyRoutes);
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
initializeDatabase().catch(err => console.error('Error initializing database:', err));

//Set the port and start the server
const port=process.env.PORT || 3000;


app.listen(port, async () => {
  console.log(`Server running on port ${port}`);
});