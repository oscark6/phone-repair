import React from 'react';
import './Portfolio.css';

const repairWorks = [
  { before: 'https://howtostartanllc.com/images/business-ideas/business-idea-images/screen-repair-business.jpg', after: 'https://media.wired.com/photos/593284aeaef9a462de98365f/master/w_2560%2Cc_limit/2014-09-23-iphone6-gallery-1.jpg', description: 'Screen Repair' },
  { before: 'https://www.shutterstock.com/image-photo/06082022-punta-cana-dominican-republic-260nw-2200577129.jpg', after: 'https://techstory.in/wp-content/uploads/2022/12/Screenshot-2022-12-27-083520.jpg', description: 'Battery Replacement' },
  { before: 'https://www.mobilescreenfix.co.uk/wp-content/uploads/2022/09/phone-water-damaged-1.jpg', after: 'https://media.gettyimages.com/id/1327597496/photo/mobile-phone-on-a-white-surface-with-water-drops.jpg?s=612x612&w=gi&k=20&c=vuRH6uatEpBOcvjwVKnZgr96H90O18tJLufQJKUITAI=', description: 'Water Damage Repair' },
  // Add more repair work items here
];

function Portfolio() {
  return (
    <div className="portfolio-section">
      <h1>Our Repair Work: Before & After</h1>
      <div className="portfolio-container">
        {repairWorks.map((work, index) => (
          <div className="portfolio-item" key={index}>
            <h2>{work.description}</h2>
            <div className="comparison-slider">
              <div className="comparison-image before">
                <img src={work.before} alt={`Before ${work.description}`} />
              </div>
              <div className="comparison-image after">
                <img src={work.after} alt={`After ${work.description}`} />
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Portfolio;
