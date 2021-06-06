import React from 'react'
import SearchForm from './SearchForm'


const Header = () => {
    return (
        <div>
            <nav>
                <nav className="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
                    <div className="container-fluid">
                        <a className="navbar-brand" href="#">Clean Recipes</a>
                        <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
                            <span className="navbar-toggler-icon"></span>
                        </button>
                        <div className="collapse navbar-collapse" id="navbarCollapse">
                           <SearchForm/>
                        </div>
                    </div>
                </nav>
            </nav>
        </div>
    )
}

export default Header