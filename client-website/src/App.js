import React, {useState} from 'react';
import {BrowserRouter, Routes, Route} from "react-router-dom";
import LandingPage from "./LandingPage";
import Main from "./Main";

function App() {
    const [products, setProducts] = useState([]);
    return (
        <BrowserRouter>
            <Routes>
                <Route exact path="/" element={<LandingPage setProducts={setProducts}/>}/>
                <Route exact path="/main" element={<Main products={products}/>}/>
            </Routes>
        </BrowserRouter>
    )
}

export default App;
