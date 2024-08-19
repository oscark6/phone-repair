import React from 'react';
import './ServicesPage.css';
import Footer from './Footer';

function ServicesPage() {
  const services = [
    {
      name: "Screen Repair",
      description: "Cracked or shattered screen? Our experts can quickly replace your phone's screen with high-quality parts. We handle all major brands and models, ensuring a flawless finish.",
      image: "https://howtostartanllc.com/images/business-ideas/business-idea-images/screen-repair-business.jpg" // Replace with the actual image path
    },
    {
      name: "Battery Replacement",
      description: "Experiencing battery issues? We offer fast and efficient battery replacement services. Our high-quality batteries ensure your phone lasts longer and performs better.",
      image: "https://9to5mac.com/wp-content/uploads/sites/6/2023/07/iPhone-battery-replacement.jpg?quality=82&strip=all" // Replace with the actual image path
    },
    {
      name: "Water Damage Repair",
      description: "Dropped your phone in water? Don't worry, our technicians are skilled in handling water-damaged phones. We'll thoroughly clean and repair your device to restore its functionality.",
      image: "https://repairexpress.com/wp-content/uploads/2023/09/MicrosoftTeams-image-30.jpg" // Replace with the actual image path
    },
    {
      name: "Charging Port Repair",
      description: "Having trouble charging your phone? Our team can fix or replace faulty charging ports to ensure your phone charges correctly and efficiently.",
      image: "https://cdn-bjcni.nitrocdn.com/iVNCPdDQeamUVPLwrUUCDenAdntewMKT/assets/images/optimized/rev-25a9eda/www.gophermods.com/wp-content/uploads/2023/07/iPhone-Charging-Port-Repair-Options-Costs-and-Considerations.jpg" // Replace with the actual image path
    },
    {
      name: "Software Issues",
      description: "Is your phone running slow or experiencing software glitches? We can diagnose and resolve software issues, including updates, malware removal, and more.",
      image: "https://jarvee.com/wp-content/uploads/2023/08/Cybersecurity-threats.png" // Replace with the actual image path
    },
    {
      name: "Data Recovery",
      description: "Lost important data? Our data recovery services can help retrieve lost photos, contacts, and other vital information from your damaged or malfunctioning phone.",
      image: "https://www.provendata.com/wp-content/uploads/2023/09/How-Does-a-Hard-Drive-Data-Recovery-Service-Work-What-to-Expect-from-the-Hard-Drive-Recovery-Process.jpg" // Replace with the actual image path
    }
  ];

  return (
    <div className="services">
      <h1>Our Services</h1>
      <div className="service-container">
        {services.map((service, index) => (
          <div className="flip-card" key={index}>
            <div className="flip-card-inner">
              <div className="flip-card-front">
                <img src={service.image} alt={service.name} className="service-image" />
                <h2>{service.name}</h2>
              </div>
              <div className="flip-card-back">
                <h2>{service.name}</h2>
                <p>{service.description}</p>
              </div>
            </div>
          </div>
        ))}
      </div>
      <Footer />
    </div>
  );
}

export default ServicesPage;
