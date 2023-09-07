import React, { useState, useEffect } from 'react';
import { Button } from 'react-bootstrap';

function LandingPage() {
    return (
        <>
            <h1>Welcome to the coinbase visualisation app!</h1>
            <Button href="/main">Go to main page</Button>
        </>
    );
}

export default LandingPage;