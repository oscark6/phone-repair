import React, { useState, useEffect } from 'react';
import { Link, useHistory } from 'react-router-dom';
import './Navbar.css';

function Navbar() {
  const [dropdownOpen, setDropdownOpen] = useState(false);
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const history = useHistory();

  useEffect(() => {
    // Check if user is authenticated
    const token = localStorage.getItem('access_token');
    setIsAuthenticated(!!token); // Convert to boolean
  }, []);

  const toggleDropdown = () => {
    setDropdownOpen(!dropdownOpen);
  };

  const handleLogout = () => {
    // Remove the token from local storage
    localStorage.removeItem('access_token');
    setIsAuthenticated(false);
    history.push('/login'); // Redirect to login page
  };

  return (
    <nav className="navbar">
      <div className="navbar-logo">
        <Link to="/">PRoFiX</Link>
      </div>
      <ul className="navbar-links">
        <li><Link to="/">Home</Link></li>
        <li><Link to="/about-us">About Us</Link></li>
        <li><Link to="/services">Services</Link></li>
        <li><Link to="/contact-us">Contact Us</Link></li>
        {isAuthenticated ? (
          <li className="dropdown" onMouseEnter={toggleDropdown} onMouseLeave={toggleDropdown}>
            <span className="dropdown-toggle">Account</span>
            <ul className={`dropdown-menu ${dropdownOpen ? 'show' : ''}`}>
              {/* <li><Link to="/profile">Profile</Link></li>
              <li><Link to="/appointment-history">Appointment History</Link></li> */}
              <li><button onClick={handleLogout} className="logout-button">Logout</button></li>
            </ul>
          </li>
        ) : (
          <li className="dropdown" onMouseEnter={toggleDropdown} onMouseLeave={toggleDropdown}>
            <span className="dropdown-toggle">Account</span>
            <ul className={`dropdown-menu ${dropdownOpen ? 'show' : ''}`}>
              <li><Link to="/login">Login</Link></li>
              <li><Link to="/register">Register</Link></li>
            </ul>
          </li>
        )}
      </ul>
    </nav>
  );
}

export default Navbar;
