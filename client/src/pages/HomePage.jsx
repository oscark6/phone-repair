import React from 'react';
import './HomePage.css';
import Footer from './Footer';
import Portfolio from './Portfolio';

const HomePage = () => {
  return (
    <div>
      <div className="hero">
      <div className="container flex flex-column">
        <h1>Welcome to the Auto Repair Shop for Phones</h1>
        <p>Your go-to place for reliable and affordable phone repairs.</p>
        <a href="/services" className="btn">Explore Our Services</a>
        <a href="/appointment-booking" className="btn">Book Appointement here</a>
      </div>
    </div>
    <Portfolio />
    <Footer />

    </div>
    
  );
};

export default HomePage;
