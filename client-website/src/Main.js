import {useEffect, useState} from 'react';
import {Row, Col} from "react-bootstrap";
import './App.css';
import Dropdown from './Dropdown';
import Chart from 'react-apexcharts';

const secondsInDay = 60*60*24 // 86400
const timeRanges = {
    "1-day": secondsInDay,
    "1-week": secondsInDay * 7,
    "1-month": secondsInDay * 30,
    "3-months": secondsInDay * 30 * 3,
    "1-year": secondsInDay * 365,
    "5-years": secondsInDay * 365 * 5,
}
const granularity = {
    "1-minute": 60,
    "5-minutes": 300,
    "15-minutes": 900,
    "1-hour": 3600,
    "6-hours": 21600,
    "One-day": 86400,
};

const chart = {
    options: {
        chart: {
            type: 'candlestick',
            height: 350
        },
        title: {
            text: 'Coinbase Exchange Chart',
            align: 'left'
        },
        xaxis: {
            type: 'datetime'
        },
        yaxis: {
            tooltip: {
                enabled: true
            }
        }
    },
};

function Main() {
    const [series, setSeries] = useState([{
        data: []
    }]);
    const [isLoading, setIsLoading] = useState(true);
    const [products, setProducts] = useState([]);
    const [colWidth, setColWidth] = useState(12);
    const [selectedProduct, setSelectedProduct] = useState("");
    const [selectedTimeRange, setSelectedTimeRange] = useState(secondsInDay);
    const [selectedGranularity, setSelectedGranularity] = useState(granularity["1-minute"]);

    useEffect(() => {
        const handleResize = () => {
            if (window.innerWidth < 576) {
                setColWidth(12);
            } else if (window.innerWidth < 768) {
                setColWidth(6);
            } else {
                setColWidth(4);
            }
        }
        handleResize();
        window.addEventListener('resize', handleResize);

        return () => {
            window.removeEventListener('resize', handleResize);
        };
    }, []);

    useEffect(() => {
        if(!isLoading) {
            return;
        }
        async function fetchProductsData() {
            await fetch('/products', {mode: 'no-cors'})
                .then((response) => response.json())
                .then((data) => {
                    setProducts(data);
                    console.log(data);
                    setIsLoading(false);
                    setSelectedProduct(products[0])
                });
        }
        fetchProductsData().then(r => console.log("fetched data"));
    }, []);



    useEffect(() => {
        if (selectedProduct === "" || products.length === 0) {
            return;
        }
        console.log(selectedProduct, selectedTimeRange, selectedGranularity);
        let dateTime = Date.now();
        let endTimestamp = Math.floor(dateTime / 1000);
        let startTimestamp = endTimestamp - selectedTimeRange;
        console.log("endTimeStamp: " + endTimestamp);
        console.log("startTimeStamp: " + startTimestamp);

        async function fetchCandles(){
            await fetch(`/candles/${selectedProduct}/${startTimestamp}/${endTimestamp}/${selectedGranularity}`)
                .then((response) => response.json())
                .then((data) => {
                    console.log(data);
                    let newSeries = [{
                        data: data.map((item) => {
                            let y_items = [];
                            let lo= item[1] , hi = item[2], op = item[3], cls = item[4];
                            y_items.push(op, hi, lo, cls);
                            return {
                                x: new Date(item[0] * 1000),
                                y: y_items.map((number) => number ? +(number.toFixed(2)) : null)
                            }
                        })
                    }];
                    setSeries(newSeries);
                    console.log(newSeries);
                });
        }
        fetchCandles().then(r => console.log("fetched candles"));

    }, [selectedProduct, selectedTimeRange, selectedGranularity]);

    if (isLoading) {
        return <p>Loading...</p>;
    }
    else {
        return (
            <div className="mx-3 px-10 py-4 price">
                <Row className="justify-content-lg-start">
                    <Col xs={colWidth}>
                        <Dropdown list={products} onValueChange={setSelectedProduct} hint={"Please choose product"}/>
                    </Col>
                    <Col xs={colWidth}>
                        <Dropdown list={Object.keys(timeRanges)}
                                  onValueChange={(v) => setSelectedTimeRange(timeRanges[v])}
                                  hint={"Please choose time period"}/>
                    </Col>
                    <Col xs={colWidth}>
                        <Dropdown list={Object.keys(granularity)}
                                  onValueChange={(v) => setSelectedGranularity(granularity[v])}
                                  hint={"Please choose granularity"}/>
                    </Col>
                    <Chart options={chart.options} series={series} type="candlestick" width="100%" height={320} />
                </Row>
            </div>
        );
    }
}

export default Main;
