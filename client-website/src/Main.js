import {useEffect, useState} from 'react';
import {Row, Col} from "react-bootstrap";
import './App.css';
import Dropdown from './Dropdown';


const secondsInDay = 60*60*24
const timeRanges = {
    "1-day": secondsInDay,
    "1-week": secondsInDay * 7,
    "1-month": secondsInDay * 30,
    "3-months": secondsInDay * 30 * 3,
    "1-year": secondsInDay * 365,
}
const granularity = {
    "1-minute": 60,
    "5-minutes": 300,
    "15-minutes": 900,
    "1-hour": 3600,
    "6-hours": 21600,
    "One-day": 86400,
};
function Main({products}) {
    const [colWidth, setColWidth] = useState(12);

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

    const [selectedProduct, setSelectedProduct] = useState("");
    const [selectedTimeRange, setSelectedTimeRange] = useState(60);
    const [selectedGranularity, setSelectedGranularity] = useState(1);

    useEffect(() => {
        console.log(selectedProduct, selectedTimeRange, selectedGranularity);
    }, [selectedProduct, selectedTimeRange, selectedGranularity]);
    return (
        <div className="mx-3 px-10 py-4 price">
            <Row className="justify-content-lg-start">
                <Col xs={colWidth}>
                    <Dropdown list={products} onValueChange={setSelectedProduct} hint={"Please choose product"} />
                </Col>
                <Col xs={colWidth}>
                    <Dropdown list={Object.keys(timeRanges)} onValueChange={(v) => setSelectedTimeRange(timeRanges[v])} hint={"Please choose time period"} />
                </Col>
                <Col xs={colWidth}>
                    <Dropdown list={Object.keys(granularity)} onValueChange={(v) => setSelectedGranularity(granularity[v])} hint={"Please choose granularity"}/>
                </Col>
            </Row>
        </div>
    );
}

export default Main;
