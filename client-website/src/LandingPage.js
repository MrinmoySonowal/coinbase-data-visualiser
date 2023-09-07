import React, { useState, useEffect } from 'react';
import { Button } from 'react-bootstrap';

function LandingPage({setProducts}) {

    const [isLoading, setIsLoading] = useState(true);

    useEffect(() => {
        // const localCoinBaseServerURL = "http://localhost:8000";
        // Added to proxy in package.json, we can now use relative paths
        fetch('/products')
            .then((response) => response.json())
            .then((data) => {
                setProducts(data);
                console.log(data);
                setIsLoading(false);
            });
    }, []);

    if (isLoading) {
        return <p>Loading...</p>;
    }

    return (
        <>
            <h1>Welcome to the coinbase visualisation app!</h1>
            <Button href="/main">Go to main page</Button>
        </>
    );
}

export default LandingPage;