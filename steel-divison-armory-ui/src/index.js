import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import firebase from 'firebase';
import 'firebase/database';
import 'bootstrap/dist/css/bootstrap.css';

const firebaseConfig = {
  apiKey: "AIzaSyAPNPEzEs2ZNj6lzINhRe9eg8DMmjit2U4",
  authDomain: "steel-division-2-armory.firebaseapp.com",
  databaseURL: "https://steel-division-2-armory-default-rtdb.firebaseio.com",
  projectId: "steel-division-2-armory",
  storageBucket: "steel-division-2-armory.appspot.com",
  messagingSenderId: "468806829064",
  appId: "1:468806829064:web:4bc61fa28e11e350627dbd",
  measurementId: "G-147EWHLBMC"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
