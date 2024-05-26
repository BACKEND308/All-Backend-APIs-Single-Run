const mongoose = require('mongoose');

const CabinCrewSchema = new mongoose.Schema({
    CrewID: {type: Number, required: true, unique: true},
    Age: {type: Number, required: true},
    Aircraft_Restrictions: {type: [String], required: true, default: []},
    Assigned_Seat: {type: String, required: false, default: '-'},
    ChefID: {type: mongoose.Schema.Types.ObjectId, ref: 'chefs', default: null },
    Dishes: { type: [String], default: [] },
    Featured_Dish: { type: String, default: '-' },
    Gender: {type: String, required: true, enum: ['Female', 'Male', '-'], default: '-'},
    Known_Languages: {type: [String], required: true, default: []},
    MemberName: {type: String, required: true, default: '-'},
    Nationality: {type: String, required: true, default: '-'},
    Role: {type: String, required: true, enum: ['chief', 'regular', 'chef', '-'], default: '-'}
    }, {collection: 'cabin_crew'});

const CabinCrew = mongoose.model('cabin_crew', CabinCrewSchema);
module.exports = CabinCrew;