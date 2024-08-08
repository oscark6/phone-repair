import React from 'react';
import './ServicesPage.css';
import Footer from './Footer';

function ServicesPage() {
  return (
    <div className="services">
      <h1>Our Services</h1>
      <div className="service-container">
        <div className="service-item">
          <h2>Screen Repair</h2>
          <p>
            Cracked or shattered screen? Our experts can quickly replace your phone's screen with high-quality parts. We handle all major brands and models, ensuring a flawless finish.
          </p>
        </div>
        <div className="service-item">
          <h2>Battery Replacement</h2>
          <p>
            Experiencing battery issues? We offer fast and efficient battery replacement services. Our high-quality batteries ensure your phone lasts longer and performs better.
          </p>
        </div>
        <div className="service-item">
          <h2>Water Damage Repair</h2>
          <p>
            Dropped your phone in water? Don't worry, our technicians are skilled in handling water-damaged phones. We'll thoroughly clean and repair your device to restore its functionality.
          </p>
        </div>
        <div className="service-item">
          <h2>Charging Port Repair</h2>
          <p>
            Having trouble charging your phone? Our team can fix or replace faulty charging ports to ensure your phone charges correctly and efficiently.
          </p>
        </div>
        <div className="service-item">
          <h2>Software Issues</h2>
          <p>
            Is your phone running slow or experiencing software glitches? We can diagnose and resolve software issues, including updates, malware removal, and more.
          </p>
        </div>
        <div className="service-item">
          <h2>Data Recovery</h2>
          <p>
            Lost important data? Our data recovery services can help retrieve lost photos, contacts, and other vital information from your damaged or malfunctioning phone.
          </p>
        </div>
      </div>
      <Footer />
    </div>
  );
}

export default ServicesPage;
