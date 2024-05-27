function generateSeatsDictionary(capacity) {
    const seats = {};
    const rows = Math.ceil(capacity / 6);
    const seatLetters = ['A', 'B', 'C', 'D', 'E', 'F'];
  
    for (let row = 1; row <= rows; row++) {
      for (let seat of seatLetters) {
        seats[`${row}${seat}`] = 0;
        if (Object.keys(seats).length >= capacity) break;
      }
    }
  
    return seats;
  }
  
  function findClosestAvailableSeat(seats, desiredSeat = null) {
    const seatKeys = Array.from(seats.keys());
  
    if (!desiredSeat) {
      // Find the first available seat
      for (let seat of seatKeys) {
        if (seats.get(seat) === 0) {
          return seat;
        }
      }
      return null; // No available seats
    }
  
    const desiredIndex = seatKeys.indexOf(desiredSeat);
    if (desiredIndex === -1) return null; // Desired seat is not in the list
  
    let closestSeat = null;
    let minDistance = Infinity;
  
    for (let i = 0; i < seatKeys.length; i++) {
      if (seats.get(seatKeys[i]) === 0) { // Check if the seat is available
        const distance = Math.abs(i - desiredIndex);
        if (distance < minDistance) {
          closestSeat = seatKeys[i];
          minDistance = distance;
        }
      }
    }
  
    return closestSeat;
  }
  
  module.exports = {
    generateSeatsDictionary,
    findClosestAvailableSeat
  };
  