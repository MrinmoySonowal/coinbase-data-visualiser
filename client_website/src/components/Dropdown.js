import React from 'react';
import { Form } from 'react-bootstrap';

function Dropdown({ list, onValueChange, hint }) {

    const handleValueChange = (event) => {
        const newValue = event.target.value;
        onValueChange(newValue);
    };

    return (
        <div>
            <Form.Select id="dropdown-select" hint={hint} onChange={handleValueChange}>
                <option disabled={true} selected={false} value={hint}>{hint}</option>
                {list.map((value) => (
                    <option key={value} value={value}>
                        {value}
                    </option>
                ))}
            </Form.Select>
        </div>
    );
}

export default Dropdown;