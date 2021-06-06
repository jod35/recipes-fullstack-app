import React from 'react';


const Recipe=({name,description,directions})=>{

    return(
        <div className="d-flex text-muted pt-3">
            <svg className="bd-placeholder-img flex-shrink-0 me-2 rounded" width="32" height="32" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Placeholder: 32x32" preserveAspectRatio="xMidYMid slice" focusable="false">
            <title>Placeholder</title><rect width="100%" height="100%" fill="#007bff" /><text x="50%" y="50%" fill="#007bff" dy=".3em">32x32</text></svg>

            <div className="pb-3 mb-0 small lh-sm border-bottom w-100">
                <div className="d-flex justify-content-between">
                    <strong className="text-gray-dark">{name}</strong>
                    <a href="#">details</a>
                </div>
                <span className="d-block">{name}</span>
            </div>
        </div>
    )
}

export default Recipe;