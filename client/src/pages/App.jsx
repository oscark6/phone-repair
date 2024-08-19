import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import HomePage from './HomePage';
import AboutUsPage from './AboutUsPage';
import ServicesPage from './ServicesPage';
import ContactUsPage from './ContactUsPage';
import LoginPage from './LoginPage';
import RegisterPage from './RegisterPage';
import AppointmentBookingPage from './AppointmentBookingPage';
import AppointmentHistoryPage from './AppointmentHistoryPage';
import ProfilePage from './ProfilePage';
import AdminPanelPage from './AdminPanelPage';
import Navbar from './Navbar';
// import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <Switch>
          <Route path="/" exact component={HomePage} />
          <Route path="/about-us" component={AboutUsPage} />
          <Route path="/services" component={ServicesPage} />
          <Route path="/contact-us" component={ContactUsPage} />
          <Route path="/login" component={LoginPage} />
          <Route path="/register" component={RegisterPage} />
          <Route path="/appointment-booking" component={AppointmentBookingPage} />
          <Route path="/appointment-history" component={AppointmentHistoryPage} />
          <Route path="/profile" component={ProfilePage} />
          <Route path="/admin-panel" component={AdminPanelPage} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;
