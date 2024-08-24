import './Assassins.css'
import '../../shared_css/shared_css.css'

function Assassins() {
    return (
        <div className="assassins-page">
            <img src="Pele.png" alt="Banner" className="banner-image" />
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

export default Assassins;
