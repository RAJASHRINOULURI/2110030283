import logo from './logo.svg';
import './App.css';
import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [numberId, setNumberId] = useState('');
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const handleInputChange = (event) => {
    setNumberId(event.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    setError(null);
    setResult(null);
    try {
      const response = await axios.get(`http://20.244.56:144/numbers/${numberId}`);
      setResult(response.data);
    } catch (error) {
      setError('Invalid number ID or server error.');
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Number Average Calculator</h1>
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            value={numberId}
            onChange={handleInputChange}
            placeholder="Enter number ID (e.g., p10, f5, e8, r3)"
          />
          <button type="submit">Calculate Average</button>
        </form>
        {error && <p className="error">{error}</p>}
        {result && (
          <div>
            <p>Average: {result.average}</p>
            <p>Numbers: {result.numbers.join(', ')}</p>
          </div>
        )}
      </header>
    </div>
  );
}

export default App;

