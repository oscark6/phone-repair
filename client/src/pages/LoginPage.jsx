import React, { useState } from 'react';
import axios from 'axios';
import './LoginPage.css';

const LoginPage = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null); // Reset error state
    setSuccess(false); // Reset success state

    try {
      const response = await axios.post('http://localhost:5000/login', {
        username: email,
        password: password,
      });

      console.log('Login successful!', response.data);

      // Handle success (e.g., save token, redirect)
      setSuccess(true);
      localStorage.setItem('access_token', response.data.access_token);
      // Redirect or update UI here
    } catch (error) {
      console.error('Login failed:', error.response?.data?.message || error.message);
      setError(error.response?.data?.message || 'An error occurred');
    }
  };

  const handleForgotPassword = () => {
    alert('Forgot password functionality to be implemented.');
  };

  return (
    <div className="form-container">
      <div className="form-header">
        <h2>Login</h2>
      </div>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="email">Email</label>
          <input
            type="email"
            id="email"
            name="email"
            required
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
        </div>
        <div className="form-group">
          <label htmlFor="password">Password</label>
          <input
            type="password"
            id="password"
            name="password"
            required
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </div>
        <button type="submit" className="btn">
          Login
        </button>
      </form>
      {error && <p className="error-message">{error}</p>}
      {success && <p className="success-message">Login successful!</p>}
      <div className="form-footer">
        <p>
          <a href="#!" onClick={handleForgotPassword}>
            Forgot Password?
          </a>
        </p>
        <p>
          Don't have an account? <a href="/register">Register</a>
        </p>
      </div>
    </div>
  );
};

export default LoginPage;
