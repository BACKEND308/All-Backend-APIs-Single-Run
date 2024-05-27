const mongoose = require('mongoose');

const ChefSchema = new mongoose.Schema({
    CrewID: { type: Number, required: true, unique: true },
    MemberName: { type: String, required: true },
    Age: { type: Number, required: true },
    Gender: { type: String, required: true, enum: ['Female', 'Male'] },
    Nationality: { type: String, required: true },
    Known_Languages: { type: [String], required: true },
    Aircraft_Restrictions: { type: [String], required: true },
    Role: { type: String, required: true, enum: ['chef'], default: 'chef' },
    Dishes: { type: [String], required: true },
    Featured_Dish: { type: String, required: true }
}, { collection: 'chefs' });

const Chef = mongoose.model('chefs', ChefSchema);
module.exports = Chef;
