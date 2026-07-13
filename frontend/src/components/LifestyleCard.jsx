import { useEffect, useState } from "react";
import axios from "axios";

function LifestyleCard({ disease }) {

    const [data, setData] = useState(null);

    useEffect(() => {

        if (!disease) return;

        axios
            .get(`http://127.0.0.1:8000/lifestyle/${disease}`)
            .then((response) => {
                setData(response.data);
            })
            .catch((error) => {
                console.log(error);
            });

    }, [disease]);

    if (!data) {

        return (
            <div className="card">
                <h2>🥗 Lifestyle Recommendations</h2>
                <p>Loading recommendations...</p>
            </div>
        );

    }

    return (

        <div className="card">

            <h2>🥗 Lifestyle Recommendations</h2>

            <h3>📖 About Disease</h3>

            <p>{data.about}</p>

            <h3>🥦 Healthy Diet</h3>

            <ul>
                {data.diet.map((item, index) => (
                    <li key={index}>{item}</li>
                ))}
            </ul>

            <h3>🏃 Exercise</h3>

            <ul>
                {data.exercise.map((item, index) => (
                    <li key={index}>{item}</li>
                ))}
            </ul>

            <h3>👁 Eye Care</h3>

            <ul>
                {data.eye_care.map((item, index) => (
                    <li key={index}>{item}</li>
                ))}
            </ul>

            <h3>🚫 Things to Avoid</h3>

            <ul>
                {data.avoid.map((item, index) => (
                    <li key={index}>{item}</li>
                ))}
            </ul>

        </div>

    );

}

export default LifestyleCard;