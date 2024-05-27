const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const flightTableSchema = new Schema({
  FlightNumber: {
    type: String,
    required: true,
    unique: true
  },
  VehicleType: {
    type: String,
    required: true
  },
  pilot_id: {
    type: Number,
    required: false
  },
  reg_crews: [{
    type: Number,
    ref: 'cabin_crew',
    required: false
  }],
  chief_crews: [{
    type: Number,
    ref: 'cabin_crew',
    required: false
  }],
  Chef: [{
    type: Number,
    ref: 'chefs',
    required: false
  }],
  menu: [{
    type: String,
    required: false
  }],
  Seats: {
    type: Map,
    of: Number,
    required: true,
    default: {}
  }
}, { collection: 'flight_table' });

module.exports = mongoose.model('FlightTable', flightTableSchema);
