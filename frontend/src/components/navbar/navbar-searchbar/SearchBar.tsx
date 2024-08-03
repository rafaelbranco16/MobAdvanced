import './SearchBar.css'

interface NavbarSearchBarProps {
    content: string,
}

function NavbarSearchBar(props: NavbarSearchBarProps) {
    return (
        <div className="navbar-searchbar">
            <input style={{float: 'right'}} placeholder={props.content} />
            <button type='button'>Search</button>
        </div>
    )
}

export default NavbarSearchBar;
