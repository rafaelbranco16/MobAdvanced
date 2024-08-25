import './Guardians.css'
import '../../shared_css/shared_css.css'
import React, { useState } from 'react';

function Guardians() {
    const [text, setText] = useState("");
    
    const handleKeyPress = (event:React.KeyboardEvent) => {
        if(event.key == 'Enter') {
            
        }
    }

    const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setText(event.target.value);
    };

    return (
        <div className="guardians-page">
            <img src="Kuzenbo.jpg" alt="Banner" className="banner-image" />
            <div className="ai-question-div">
                Is there any question about this class? 
                <input 
                    type='text' 
                    placeholder='Type your question here...'
                    onKeyDown={handleKeyPress}
                    onChange={handleChange}
                />
            </div>
            <div className="class-explanation-div">
                {/* Content here */}
            </div>
        </div>
    )
}

export default Guardians;
