import React from 'react';
import './ContactUsPage.css';

function ContactUsPage() {
  return (
    <div className="contact">
      <h1>Contact Us</h1>
      <p>If you have any questions, feel free to reach out to us through any of the methods below:</p>
      
      <div className="contact-methods">
        <div className="contact-method">
          <h2>Phone</h2>
          <p>Call us at <strong>(254) 756-7890</strong></p>
        </div>
        <div className="contact-method">
          <h2>Email</h2>
          <p>Email us at <strong>support@phonerepairshop.com</strong></p>
        </div>
        <div className="contact-method">
          <h2>Visit Us</h2>
          <p>Come visit our store at:</p>
          <p><strong>123 Kasa Street, Nairobi, Kenya</strong></p>
        </div>
        <div className="contact-method">
          <h2>Business Hours</h2>
          <p>Monday - Friday: <strong>9:00 AM - 6:00 PM</strong></p>
          <p>Saturday: <strong>10:00 AM - 4:00 PM</strong></p>
          <p>Sunday: <strong>Closed</strong></p>
        </div>
      </div>
      
      <div className="contact-form">
        <h2>Send Us a Message</h2>
        <form>
          <label htmlFor="name">Name:</label>
          <input type="text" id="name" name="name" required />

          <label htmlFor="email">Email:</label>
          <input type="email" id="email" name="email" required />

          <label htmlFor="message">Message:</label>
          <textarea id="message" name="message" rows="5" required></textarea>

          <button type="submit">Submit</button>
        </form>
      </div>
    </div>
  );
}

export default ContactUsPage;
