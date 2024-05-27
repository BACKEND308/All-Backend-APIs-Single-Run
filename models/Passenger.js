const mongoose = require('mongoose');

const ParentInfoSchema = new mongoose.Schema({
  Parent_id: { type: String },
  Seat_assigned: { type: String }
}, { _id: false });

const PassengerSchema = new mongoose.Schema({
  Passenger_id: {
    type: String,
    required: true,
    unique: true
  },
  Name: {
    type: String,
    required: true
  },
  Flight_id: {
    type: String,
    required: true
  },
  Age: {
    type: Number,
    required: true
  },
  Gender: {
    type: String,
    required: true
  },
  Nationality: {
    type: String,
    required: true
  },
  Seat_type: {
    type: String,
    required: true,
    enum: ['Economy', 'Business'],
    default: 'None'
  },
  Seat_assigned: {
    type: String,
    default: null
  },
  AffiliatedPassengerIDs: {
    type: [String],
    default: []
  },
  Parent_info: {
    type: [ParentInfoSchema],
    default: []
  }
}, { collection: 'passenger_info' });

const Passenger = mongoose.model('Passenger', PassengerSchema);

module.exports = Passenger;
