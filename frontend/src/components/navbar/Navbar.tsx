import NavbarItem from "./navbar-item/NavbarItem";
import SearchBar from './navbar-searchbar/SearchBar'
import './Navbar.css'

function HeaderNavbar() {
    return (
        <>
            <div className="navbar">
                <ul>
                    <NavbarItem content="Home" href=""/>
                    <NavbarItem content="Add Info" href="add-info"/>
                    <NavbarItem content="Files" href="files"/>
                    <SearchBar content="Something specific?"/>
                </ul>
            </div>
        </>
    )
}

export default HeaderNavbar;