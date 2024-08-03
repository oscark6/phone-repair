import React from 'react';
import './AppointmentBookingPage.css';

function AppointmentBookingPage() {
  return (
    <div className="appointment-booking">
      <h1>Book an Appointment</h1>
      <form>
        <div>
          <label>Date: </label>
          <input type="date" name="date" />
        </div>
        <div>
          <label>Time: </label>
          <input type="time" name="time" />
        </div>
        <div>
          <label>Service: </label>
          <select name="service">
            <option value="screen-repair">Screen Repair</option>
            <option value="battery-replacement">Battery Replacement</option>
            <option value="water-damage-repair">Water Damage Repair</option>
          </select>
        </div>
        <button type="submit">Book Appointment</button>
      </form>
    </div>
  );
}

export default AppointmentBookingPage;
