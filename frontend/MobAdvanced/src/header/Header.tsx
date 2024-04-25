import './Header.css'
import { Link } from 'react-router-dom'; // If you're using React Router for navigation
function Header() {
    return (
        <>
            <nav>
                <ul>
                <li>
                    <Link to="/">Home</Link>
                </li>
                <li>
                    <Link to="/gods">Gods</Link>
                </li>
                <li>
                    <Link to="/builds">Builds</Link>
                </li>
                </ul>
            </nav>
        </>
    )
}

export default Header;