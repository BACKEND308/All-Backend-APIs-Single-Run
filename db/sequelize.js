const Sequelize = require('sequelize');
const dotenv = require('dotenv');

dotenv.config();

const sequelize = new Sequelize(
  process.env.MYSQL_DATABASE || 'flightinfosystem',
  process.env.MYSQL_USER || 'root',
  process.env.MYSQL_PASSWORD || '1234',
  {
    host: process.env.MYSQL_HOST || '127.0.0.1',
    dialect: 'mysql'
  }
);

module.exports = sequelize;