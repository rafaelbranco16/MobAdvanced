import './Guardians.css'
import '../../shared_css/shared_css.css'

function Guardians() {
    return (
        <div className="guardians-page">
            <img src="Kuzenbo.jpg" alt="Banner" className="banner-image" />
            <div className="ai-question-div">
                Is there any question about this class? 
                <input 
                    type='text' 
                    placeholder='Type your question here...'
                />
            </div>
            <div className="class-explanation-div">
                {/* Content here */}
            </div>
        </div>
    )
}

export default Guardians;
