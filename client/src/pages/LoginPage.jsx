import React from 'react';
import './LoginPage.css';

function LoginPage() {
  return (
    <div className="login">
      <h1>Login</h1>
      <form>
        <div>
          <label>Username: </label>
          <input type="text" name="username" />
        </div>
        <div>
          <label>Password: </label>
          <input type="password" name="password" />
        </div>
        <button type="submit">Login</button>
      </form>
    </div>
  );
}

export default LoginPage;
