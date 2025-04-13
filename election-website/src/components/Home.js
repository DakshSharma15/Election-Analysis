import React, { useEffect, useState } from 'react';
import './HomePage.css';

function HomePage() {
  const [news, setNews] = useState([]);

  useEffect(() => {
    // Check if news data is already stored in localStorage
    const cachedNews = localStorage.getItem('electionNews');
    if (cachedNews) {
      setNews(JSON.parse(cachedNews)); // Load from storage
    } else {
      fetchNews(); // Fetch new news data
    }
  }, []);

  const fetchNews = () => {
    fetch("https://newsapi.org/v2/everything?q=indian-election&apiKey=38cdf4ee48304f2fa249e3eb138cc8de")
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP Error! Status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        if (data.articles) {
          setNews(data.articles.slice(0, 3)); // Get top 3 news articles
          localStorage.setItem('electionNews', JSON.stringify(data.articles.slice(0, 3))); // Save to localStorage
        }
      })
      .catch(error => console.error("Error fetching news:", error));
  };

  return (
    <div className="home-container">
      {/* Hero Banner */}
      <div className="hero-banner">
        <img 
          src="https://www.india.gov.in/sites/upload_files/npi/files/spotlights/voter_information_services.jpg" 
          alt="Voter Information Services"
          className="banner-image"
        />
      </div>

      {/* Latest Election News */}
      <section className="news-section">
        <h2>Latest Election News</h2>
        <div className="news-container">
          {news.length > 0 ? (
            news.map((article, index) => (
              <div key={index} className="news-card">
                <img src={article.urlToImage} alt="News" className="news-image"/>
                <h3>{article.title}</h3>
                <p>{article.description}</p>
                <a href={article.url} target="_blank" rel="noopener noreferrer">Read More</a>
              </div>
            ))
          ) : (
            <p>Loading news...</p>
          )}
        </div>
      </section>

      {/* Testimonials */}
      <section className="testimonials-section">
        <h2>What People Say</h2>
        <div className="testimonials-container">
          <div className="testimonial">
            <p>"This platform helped me understand voting trends easily!"</p>
            <span>- A Concerned Citizen</span>
          </div>
          <div className="testimonial">
            <p>"Great insights for researchers and policymakers!"</p>
            <span>- Political Analyst</span>
          </div>
        </div>
      </section>

      {/* Call to Action */}
      <section className="cta-section">
        <h2>Get Started with Election Insights</h2>
        <a href="/dashboard" className="cta-button">Explore the Dashboard</a>
      </section>

      {/* Footer */}
      <footer className="footer">
        <div className="footer-container">
          <div className="footer-links">
            <a href="/">Home</a>
            <a href="/about">About</a>
            <a href="/dashboard">Dashboard</a>
          </div>
          <div className="footer-social">
            <a href="https://twitter.com" target="_blank" rel="noopener noreferrer">
              <img src="https://cdn-icons-png.flaticon.com/512/733/733579.png" alt="Twitter"/>
            </a>
            <a href="https://facebook.com" target="_blank" rel="noopener noreferrer">
              <img src="https://cdn-icons-png.flaticon.com/512/733/733547.png" alt="Facebook"/>
            </a>
            <a href="https://linkedin.com" target="_blank" rel="noopener noreferrer">
              <img src="https://cdn-icons-png.flaticon.com/512/733/733561.png" alt="LinkedIn"/>
            </a>
          </div>
          <p>© 2024 Election Analysis. All Rights Reserved.</p>
        </div>
      </footer>
    </div>
  );
}

export default HomePage;
