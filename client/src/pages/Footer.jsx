// src/components/Footer.js

import React from "react";
import "./Footer.css"; // Import CSS file

const Footer = () => {
  return (
    <footer className="footer">
      <div className="footer-container">
        <div className="footer-column">
          <h4>Contact Us</h4>
          <ul>
            <li>Phone: (123) 456-7890</li>
            <li>Email: info@phonerepairshop.com</li>
            <li>Address: 123 Main Street, City, State</li>
          </ul>
        </div>

        <div className="footer-column">
          <h4>Opening Hours</h4>
          <ul>
            <li>Mon - Fri: 9:00 AM - 7:00 PM</li>
            <li>Saturday: 10:00 AM - 5:00 PM</li>
            <li>Sunday: Closed</li>
          </ul>
        </div>

        <div className="footer-column">
          <h4>Quick Links</h4>
          <ul>
            <li>
              <a href="/appointment-booking">Booking</a>
            </li>
            <li>
              <a href="/appointment-history">Booking History</a>
            </li>
            <li>
              <a href="/contact-us">Contact</a>
            </li>
            <li>
              <a href="/about-us">About</a>
            </li>
          </ul>
        </div>

        <div className="footer-column">
          <h4>Follow Us</h4>
          <div className="social-icons">
            <a href="https://facebook.com" target="_blank" rel="noopener noreferrer">
              <img src="/icons/facebook.svg" alt="Facebook" />
            </a>
            <a href="https://twitter.com" target="_blank" rel="noopener noreferrer">
              <img src="/icons/twitter.svg" alt="Twitter" />
            </a>
            <a href="https://instagram.com" target="_blank" rel="noopener noreferrer">
              <img src="/icons/instagram.svg" alt="Instagram" />
            </a>
            <a href="https://linkedin.com" target="_blank" rel="noopener noreferrer">
              <img src="/icons/linkedin.svg" alt="LinkedIn" />
            </a>
          </div>
        </div>
      </div>

      <div className="footer-bottom">
        <p>&copy; 2024 Phone Repair Shop. All rights reserved.</p>
      </div>
    </footer>
  );
};

export default Footer;
