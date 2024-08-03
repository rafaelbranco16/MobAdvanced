import './Image.css';

interface ImageContainerProps {
    god: string;
    god_alt: string;
    class: string;
    class_alt: string;
    color: string;
    text: string;
    text_color: string;
}

function ImageContainer(props: ImageContainerProps) {
    return (
        <div className="image-container">
            <img src={props.god} alt={props.god_alt} className='background-image' />
            <img src={props.class} alt={props.class_alt} className='overlay-image' />
            <div className='color-overlay' style={{ backgroundColor: props.color }} />
            <p style={{ color: props.text_color }}>{props.text}</p>
        </div>
    );
}

export default ImageContainer;
