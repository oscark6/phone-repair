// import React from 'react';
// import ReactDOM from 'react-dom';
// import App from './pages/App';
// import './index.css';

// ReactDOM.render(
//   <React.StrictMode>
//     <App />
//   </React.StrictMode>,
//   document.getElementById('root')
// );


import React from 'react';
import ReactDOM from 'react-dom';
import App from './pages/App';
import './index.css';
import { AuthProvider } from './AuthContext';

ReactDOM.render(
  <AuthProvider>
    <App />
  </AuthProvider>,
  document.getElementById('root')
);
