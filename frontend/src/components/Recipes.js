import React from 'react'
import Recipe from './Recipe'

const maps = [
    1, 2, 3, 4, 5
]

const Recipes = ({ list }) => {
    return (
        <div className="my-3 p-3 bg-body rounded shadow-sm recipes">
            <h6 className="border-bottom pb-2 mb-0">Suggestions</h6>
            {
                list.map(
                    (item,index) => {
                        return <Recipe
                            key={index}
                            name={item.name}
                            description={item.description}
                            directions={item.directions}

                        />
                    }
                )
            }
            <small className="d-block text-end mt-3">
                <a href="#">All suggestions</a>
            </small>
        </div>
    )
}

export default Recipes;