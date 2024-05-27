const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const busyTimeSchema = new Schema({
  arrival: {
    type: Date,
    required: true
  },
  departure: {
    type: Date,
    required: true
  }
}, { _id: false });

const pilotBusySchema = new Schema({
  pilot_id: {
    type: Number,
    required: true,
    unique: true
  },
  pilot_name: {
    type: String,
    required: true
  },
  pilot_seniority: {
    type: String,
    required: true
  },
  pilot_vehicle_restrictions: {
    type: [String],
    required: true
  },
  busy_times: [busyTimeSchema]
}, {
  toObject: { virtuals: true },
  toJSON: { virtuals: true },
  collection: 'pilot_busy'
});

pilotBusySchema.virtual('number_of_works').get(function() {
  return this.busy_times.length;
});

pilotBusySchema.index({ 'busy_times.length': 1 });

module.exports = mongoose.model('PilotBusy', pilotBusySchema);
