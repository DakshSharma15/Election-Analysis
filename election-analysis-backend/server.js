const express = require('express');
const app = express();
const port = 5000;
const cors = require('cors');
app.use(cors());


// Middleware to parse JSON
app.use(express.json());

// Mock data or API call functions
// For demonstration, we'll use mock data. Replace with actual API calls or model logic

// Election Analysis API (Part 1)
app.get('/api/election-analysis', (req, res) => {
  const { state } = req.query;
  if (!state) {
    return res.status(400).json({ error: 'State name is required' });
  }

  // Replace with actual logic to get election analysis for the state
  const analysis = `Election analysis for ${state}: Prediction data here.`;
  res.json({ state, analysis });
});

// Winning Probability API (Part 2)
app.get('/api/winning-probability', (req, res) => {
  const { candidate } = req.query;
  if (!candidate) {
    return res.status(400).json({ error: 'Candidate name is required' });
  }

  // Replace with logic to calculate winning probability based on candidate name
  const probability = `Winning probability for ${candidate}: 65%`;
  res.json({ candidate, probability });
});

// Sentiment Analysis API (Part 3)
app.get('/api/sentiment-analysis', (req, res) => {
  const { candidate } = req.query;
  if (!candidate) {
    return res.status(400).json({ error: 'Candidate name is required' });
  }

  // Replace with actual sentiment analysis logic for the candidate
  const sentiment = `Sentiment analysis for ${candidate}: Positive`;
  res.json({ candidate, sentiment });
});

// Start the server
app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});
