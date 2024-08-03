import React from 'react';
import './AppointmentHistoryPage.css';

function AppointmentHistoryPage() {
  return (
    <div className="appointment-history">
      <h1>Appointment History</h1>
      <ul>
        <li>Appointment 1: Screen Repair on 2024-07-20</li>
        <li>Appointment 2: Battery Replacement on 2024-07-21</li>
      </ul>
    </div>
  );
}

export default AppointmentHistoryPage;
