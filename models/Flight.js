const mongoose = require('mongoose');

const connectingFlightInfoSchema = new mongoose.Schema({
    FlightNumber: String,
    Company: String,
    DepartureTime: String
}, { collection: 'flight_information' });

const sharedFlightInfoSchema = new mongoose.Schema({
    SharedFlightNumber: String,
    SharedFlightCompany: String,
    ConnectingFlightInfo: connectingFlightInfoSchema
}, { collection: 'flight_information' });

const vehicleTypeSchema = new mongoose.Schema({
    Model: String,
    Capacity: Number,
    StandardMenu: String
}, { collection: 'flight_information' });

const locationSchema = new mongoose.Schema({
    Country: String,
    City: String,
    AirportName: String,
    AirportCode: String
}, { collection: 'flight_information' });

const flightSchema = new mongoose.Schema({
    FlightNumber: { type: String, required: true, unique: true },
    Date: { type: Date, required: true },
    FlightDuration: String,
    FlightDistance: Number,
    FlightSource: locationSchema,
    FlightDestination: locationSchema,
    VehicleType: vehicleTypeSchema,
    SharedFlightInfo: sharedFlightInfoSchema
}, { collection: 'flight_information' }); 

const Flight = mongoose.model('Flight', flightSchema);
module.exports = Flight;
