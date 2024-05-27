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

const crewBusySchema = new Schema({
  CrewID: {
    type: Number,
    required: true,
    unique: true
  },
  MemberName: {
    type: String,
    required: true
  },
  Aircraft_Restrictions: {
    type: [String],
    required: true
  },
  crew_type: {
    type: String,
    enum: ['flight', 'cabin'],
    required: true
  },
  Role: {
    type: String,
    required: true
  },
  busy_times: [busyTimeSchema]
}, {
  toObject: { virtuals: true },
  toJSON: { virtuals: true },
  collection: 'Crew_busy'
});

crewBusySchema.virtual('number_of_works').get(function() {
  return this.busy_times.length;
});

crewBusySchema.index({ 'busy_times.length': 1 });

module.exports = mongoose.model('CrewBusy', crewBusySchema);
