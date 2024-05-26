const mongoose = require('mongoose');

const RosterSchema = new mongoose.Schema({
    RosterID: {type: Number, required: true, unique: true, default: '-'},
    PilotID: {type: Number, required: true},
    CrewID: {type: Number, required: true},
    FlightNumber: {type: String, required: true},
    Date: {type: Date, required: true}
}, {collection: 'roster_entry'});

const Roster = mongoose.model('roster_entry', RosterSchema);
module.exports=Roster;