import NavbarItem from "./navbar-item/NavbarItem";
import './Navbar.css'

function HeaderNavbar() {
    return (
        <>
            <div className="navbar">
                <ul>
                    <NavbarItem content="Home" href=""/>
                    <NavbarItem content="Add Info" href="add-info"/>
                </ul>
            </div>
        </>
    )
}

export default HeaderNavbar;