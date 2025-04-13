import React from 'react';
import './AboutPage.css';

function AboutPage() {
  return (
    <div className="about-container">
      {/* Hero Banner */}
      <div className="about-banner">
        <img 
          src="https://www.shutterstock.com/image-vector/india-national-day-banner-flag-260nw-2333987757.jpg" 
          alt="Election Banner"
          className="about-banner-image"
        />
      </div>

      {/* Introduction Section */}
      <section className="about-content">
        <h2>Our Mission</h2>
        <p>
          The <strong>Election Analysis Platform</strong> is designed to provide **data-driven insights** into elections across India.  
          We leverage **machine learning, AI-powered predictions, and real-time data visualization** to help users understand voting patterns,  
          candidate performance, and electoral trends.
        </p>
      </section>
    {/* What We Offer Section with Card Design */}
    <section className="offer-section">
        <h2>What We Offer</h2>
        <div className="offer-container">
          <div className="offer-card">
            <h3>📊 Data-Driven Insights</h3>
            <p>Analyze historical election data and trends to understand voting behavior.</p>
          </div>
          <div className="offer-card">
            <h3>📍 State-Wise Analysis</h3>
            <p>Explore detailed results for every state and constituency in India.</p>
          </div>
          <div className="offer-card">
            <h3>📈 AI Predictions</h3>
            <p>Use machine learning to predict future election outcomes with accuracy.</p>
          </div>
          <div className="offer-card">
            <h3>📡 Real-Time Updates</h3>
            <p>Get instant updates on election trends, candidates, and results.</p>
          </div>
        </div>
      </section>
      {/* FAQ Section */}
      <section className="faq-section">
        <h2>Frequently Asked Questions</h2>
        <div className="faq-container">
          <details>
            <summary>How does the election prediction work?</summary>
            <p>Our AI models analyze historical data, voting trends, and public sentiment to generate predictive insights.</p>
          </details>
          <details>
            <summary>Is the data accurate and real-time?</summary>
            <p>We use real-time data from official sources and ensure accuracy through multiple validation checks.</p>
          </details>
          <details>
            <summary>Who can benefit from this platform?</summary>
            <p>Citizens, researchers, policymakers, and media personnel can all leverage our insights.</p>
          </details>
        </div>
      </section>

      {/* Contact Section */}
      <section className="contact-section">
        <h2>Contact Us</h2>
        <p>Have questions? Reach out to us at  
          <a href="mailto:d.sharma151204@gmail.com"> d.sharma151204@gmail.com</a>
        </p>
      </section>
    </div>
  );
}

export default AboutPage;
