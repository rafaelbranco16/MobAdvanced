// Assassins.tsx
import './Assassins.css';
import '../../shared_css/shared_css.css';
import { useState, KeyboardEvent, ChangeEvent } from 'react';
import { send_question } from '../../services/question_service';

interface Answer {
  message: string;
}

function Assassins() {
  const [text, setText] = useState<string>('');
  const [answers, setAnswers] = useState<string[]>([]);
  const [gods, setGods] = useState<string[]>([
    // Placeholder god images; replace with dynamic data as needed
    'god1.png',
    'god2.png',
  ]);

  const handleKeyPress = async (event: KeyboardEvent<HTMLInputElement>) => {
    if (event.key === 'Enter') {
      try {
        const answer: Answer = await send_question(text, 'Assassin');
        setAnswers((prevAnswers) => [...prevAnswers, answer.message]);
      } catch (error) {
        console.error('Error fetching answer:', error);
      }
    }
  };

  const handleChange = (event: ChangeEvent<HTMLInputElement>) => {
    setText(event.target.value);
  };

  return (
    <div className="assassins-page">
      <img src="Pele.png" alt="Banner" className="banner-image" />
      <div className="content-container">
        {/* Left Section: Guides / Builds */}
        <div className="left-section">
          <h3>Builds / Guides</h3>
          {/* Dynamic content for builds and guides */}
        </div>

        {/* Center Section: AI Question and Answers */}
        <div className="center-section">
          <div className="ai-question-div">
            <h4>Is there any question about this class?</h4>
            <input
              type="text"
              placeholder="Type your question here..."
              onKeyDown={handleKeyPress}
              onChange={handleChange}
              value={text}
            />
          </div>
          <div className="answers-div">
            {answers.map((answer, index) => (
              <div key={index} className="answer-item">
                {answer}
              </div>
            ))}
          </div>
        </div>

        {/* Right Section: God Images */}
        <div className="right-section">
            <h3>Gods</h3>
          {gods.map((god, index) => (
            <img key={index} src={god} alt={`God ${index}`} className="god-image" />
          ))}
        </div>
      </div>
    </div>
  );
}

export default Assassins;
