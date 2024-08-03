import React from 'react';
import './AboutUsPage.css';

function AboutUsPage() {
  return (
    <div className="about">
      <h1>About Us</h1>
      <div className="content">
        <p>
          Welcome to our phone repair shop! We are dedicated to providing the best phone repair services in the area. With years of experience, our team of experts can handle any issue your phone may have, from screen repairs to battery replacements and more.
        </p>
        <h2>Our Mission</h2>
        <p>
          Our mission is to offer reliable, fast, and affordable phone repair services. We believe in transparency and honesty, ensuring that our customers understand the repair process and receive the highest quality service.
        </p>
        <h2>Why Choose Us?</h2>
        <ul>
          <li>Experienced Technicians</li>
          <li>Quality Parts</li>
          <li>Fast Turnaround Time</li>
          <li>Competitive Pricing</li>
          <li>Excellent Customer Service</li>
        </ul>
        <h2>Contact Us</h2>
        <p>
          Have questions or need to schedule a repair? Feel free to reach out to us. We're here to help!
        </p>
        <address>
          Phone Repair Shop<br />
          1234 Repair St.<br />
          Repair City, RC 12345<br />
          Phone: (123) 456-7890<br />
          Email: contact@phonerepairshop.com
        </address>
      </div>
    </div>
  );
}

export default AboutUsPage;
