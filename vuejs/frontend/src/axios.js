// src/axios.js
import axios from 'axios';

const instance = axios.create({
  baseURL: 'http://127.0.0.1:5000', // URL do seu servidor Flask
  timeout: 1000,
});

export default instance;
