import { Link } from 'react-router-dom';
import './NavbarItem.css'

interface NavbarItemProps {
    content:string;
    href:string;
}

function NavbarItem(props:NavbarItemProps) {
    return (
        <>
            <li className="navbar-li"><Link to={props.href}>{props.content}</Link></li>
        </>
    )
}

export default NavbarItem;