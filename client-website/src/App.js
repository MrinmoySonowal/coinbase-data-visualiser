import React, {useState} from 'react';
import {BrowserRouter, Routes, Route} from "react-router-dom";
import LandingPage from "./LandingPage";
import Main from "./Main";

function App() {

    return (
        <BrowserRouter>
            <Routes>
                <Route exact path="/" element={<LandingPage/>}/>
                <Route exact path="/main" element={<Main/>}/>
            </Routes>
        </BrowserRouter>
    )
}

export default App;
