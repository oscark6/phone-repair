import React, { useState } from 'react';
import './AppointmentBookingPage.css';

function AppointmentBookingPage() {
  const [formData, setFormData] = useState({
    date: '',
    time: '',
    service: '',
  });
  const [error, setError] = useState(null);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
  
    // Format the date and time into a single string
    const formattedDateTime = `${formData.date}T${formData.time}`; 
  
    // Get token from localStorage
    const token = localStorage.getItem('token');
    
    const userId = 1; 
    const technicianId = 1; 
  
    const requestBody = {
      date: formattedDateTime,
      service: formData.service,
      status: 'Pending',
      user_id: userId,
      technician_id: technicianId,
      description: formData.service,
    };

    console.log('formData',requestBody);
  
    fetch('http://localhost:5000/appointments', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify(requestBody),
    })
    .then((response) => {
      if (!response.ok) {
        return response.text().then((text) => {
          throw new Error(text || 'Failed to book the appointment.');
        });
      }
      return response.json();
    })
    .then((data) => {
      alert('Appointment booked successfully!');
      setFormData({ date: '', time: '', service: '' }); 
    })
    .catch((error) => {
      console.error('Error:', error);
      setError(error.message); 
    });
  };
  
  return (
    <div className="appointment-booking">
      <h1>Book an Appointment</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Date: </label>
          <input
            type="date"
            name="date"
            value={formData.date}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <label>Time: </label>
          <input
            type="time"
            name="time"
            value={formData.time}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <label>Service: </label>
          <select
            name="service"
            value={formData.service}
            onChange={handleChange}
            required
          >
            <option value="">Select a service</option>
            <option value="Screen Repair">Screen Repair</option>
            <option value="Battery Replacement">Battery Replacement</option>
            <option value="Water Damage Repair">Water Damage Repair</option>
          </select>
        </div>
        <button type="submit">Book Appointment</button>
      </form>
      {error && <p className="error-message">{error}</p>}
    </div>
  );
}

export default AppointmentBookingPage;
