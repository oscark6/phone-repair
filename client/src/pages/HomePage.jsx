import React from 'react';
import './HomePage.css';

const HomePage = () => {
  return (
    <div className="hero">
      <div className="container flex flex-column">
        <h1>Welcome to the Auto Repair Shop for Phones</h1>
        <p>Your go-to place for reliable and affordable phone repairs.</p>
        <a href="/services" className="btn">Explore Our Services</a>
      </div>
    </div>
  );
};

export default HomePage;
