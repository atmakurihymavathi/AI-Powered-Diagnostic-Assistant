import React, { useState } from 'react';
import axios from 'axios';

function App() {
    const [file, setFile] = useState(null);
    const [symptoms, setSymptoms] = useState('');
    const [result, setResult] = useState('');

    const handleFileChange = (event) => {
        setFile(event.target.files[0]);
    };

    const handleSymptomChange = (event) => {
        setSymptoms(event.target.value);
    };

    const handleImageSubmit = async () => {
        const formData = new FormData();
        formData.append("file", file);
        const response = await axios.post("http://localhost:8000/predict/image", formData);
        setResult(response.data.diagnosis);
    };

    const handleSymptomSubmit = async () => {
        const formData = new FormData();
        formData.append("symptoms", symptoms);
        const response = await axios.post("http://localhost:8000/predict/symptom", formData);
        setResult(response.data.diagnosis);
    };

    return (
        <div>
            <h1>AI Diagnostic Assistant</h1>
            <input type="file" onChange={handleFileChange} />
            <button onClick={handleImageSubmit}>Analyze Image</button>
            <br />
            <input type="text" placeholder="Enter symptoms" value={symptoms} onChange={handleSymptomChange} />
            <button onClick={handleSymptomSubmit}>Analyze Symptoms</button>
            <h2>Diagnosis Result: {result}</h2>
        </div>
    );
}

export default App;

