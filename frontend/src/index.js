import React,{useState,useEffect} from 'react'
import ReactDOM from 'react-dom'
import 'bootstrap/dist/css/bootstrap.min.css';
import './styles/main.css'
import Header from './components/Header'
import Recipes from './components/Recipes'


const App=()=>{


    const [recipes,setRecipes]=useState([]);


    useEffect(
        ()=>{


            fetch('/recipes').then(response =>response.json())
            .then(data=>{setRecipes(data)
            
                console.log(data)
            })
            .then(response=>console.log(response));

        },[]
    )
    return (
      <div className="App">
        <Header />
        <div className="container">
          <Recipes list={recipes}/>
        </div>
      </div>
    );
}


ReactDOM.render(<App/>,document.getElementById('root'));