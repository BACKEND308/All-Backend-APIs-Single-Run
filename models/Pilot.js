const mongoose =require ('mongoose');

const PilotSchema = new mongoose.Schema({
  PilotID: { type: Number, required: true },
  PilotName: { type: String, required: true },
  LicenseNumber: { type: String, required: true },
  Age: { type: Number, required: true },
  Availability: { type: [String], required: true },
  Gender: { type: String, required: true },
  Known_Languages: { type: [String], required: true },
  Nationality: { type: String, required: true },
  Pilot_Travel_Range: { type: String, required: true },
  Seniority: { type: String, enum: ['senior', 'junior', 'trainee'], required: true },
  Vehicle_Restriction: { type: String, required: true }
},{collection:'pilots'});

const Pilot = mongoose.model('Pilot', PilotSchema);
module.exports = Pilot;