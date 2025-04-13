import React, { useState } from 'react';
import './Dashboard.css';  // Importing the CSS for styling

function Dashboard() {
  const [stateName, setStateName] = useState('');
  const [candidateName, setCandidateName] = useState('');
  const [electionAnalysisResults, setElectionAnalysisResults] = useState(null);
  const [winningProbabilityResults, setWinningProbabilityResults] = useState(null);
  const [sentimentAnalysisResults, setSentimentAnalysisResults] = useState(null);

  // Handlers for input fields
  const handleStateInput = (event) => {
    setStateName(event.target.value);
  };

  const handleCandidateInput = (event) => {
    setCandidateName(event.target.value);
  };

  // Fetch results for each part
  const fetchElectionAnalysisResults = async () => {
    try {
      const response = await fetch(`/api/election-analysis?state=${stateName}`);
      const data = await response.json();
      setElectionAnalysisResults(data);
    } catch (error) {
      console.error('Error fetching election analysis results:', error);
    }
  };

  const fetchWinningProbabilityResults = async () => {
    try {
      const response = await fetch(`/api/winning-probability?candidate=${candidateName}`);
      const data = await response.json();
      setWinningProbabilityResults(data);
    } catch (error) {
      console.error('Error fetching winning probability results:', error);
    }
  };

  const fetchSentimentAnalysisResults = async () => {
    try {
      const response = await fetch(`/api/sentiment-analysis?candidate=${candidateName}`);
      const data = await response.json();
      setSentimentAnalysisResults(data);
    } catch (error) {
      console.error('Error fetching sentiment analysis results:', error);
    }
  };

  return (
    <div className="dashboard-container">
      <h1>Election Analysis Dashboard</h1>

      <div className="dashboard-sections">
        {/* Part 1: Election Analysis */}
        <div className="dashboard-part">
          <h2>Election Analysis</h2>
          <input 
            type="text" 
            placeholder="Enter State Name" 
            value={stateName}
            onChange={handleStateInput}
          />
          <button onClick={fetchElectionAnalysisResults}>Get Election Analysis</button>
          <div className="result-display">
            {electionAnalysisResults ? (
              <pre>{JSON.stringify(electionAnalysisResults, null, 2)}</pre>
            ) : (
              <p>No results available yet.</p>
            )}
          </div>
        </div>

        {/* Part 2: Winning Probability */}
        <div className="dashboard-part">
          <h2>Winning Probability</h2>
          <input 
            type="text" 
            placeholder="Enter Candidate Name" 
            value={candidateName}
            onChange={handleCandidateInput}
          />
          <button onClick={fetchWinningProbabilityResults}>Get Winning Probability</button>
          <div className="result-display">
            {winningProbabilityResults ? (
              <pre>{JSON.stringify(winningProbabilityResults, null, 2)}</pre>
            ) : (
              <p>No results available yet.</p>
            )}
          </div>
        </div>

        {/* Part 3: Sentiment Analysis */}
        <div className="dashboard-part">
          <h2>Sentiment Analysis</h2>
          <input 
            type="text" 
            placeholder="Enter Candidate Name" 
            value={candidateName}
            onChange={handleCandidateInput}
          />
          <button onClick={fetchSentimentAnalysisResults}>Get Sentiment Analysis</button>
          <div className="result-display">
            {sentimentAnalysisResults ? (
              <pre>{JSON.stringify(sentimentAnalysisResults, null, 2)}</pre>
            ) : (
              <p>No results available yet.</p>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}

export default Dashboard;
