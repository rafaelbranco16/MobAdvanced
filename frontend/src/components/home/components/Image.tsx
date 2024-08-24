import './Image.css';
import { Link } from 'react-router-dom'

interface ImageContainerProps {
    god: string;
    god_alt: string;
    class: string;
    class_alt: string;
    color: string;
    text: string;
    text_color: string;
    link: string
}

function ImageContainer(props: ImageContainerProps) {
    return (
        <Link to={props.link} className="image-container">
            <img src={props.god} alt={props.god_alt} className='background-image'/>
            <img src={props.class} alt={props.class_alt} className='overlay-image' />
            <div className='color-overlay' style={{ backgroundColor: props.color }} />
            <p style={{ color: props.text_color }}>{props.text}</p>
        </Link>
    );
}


export default ImageContainer;
