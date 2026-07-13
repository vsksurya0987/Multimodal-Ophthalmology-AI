function PredictionCard({ prediction }) {

    return (

        <div className="card">

            <h2>🩺 AI Prediction Result</h2>

            <h3>

                Disease:
                <span style={{ color: "#d9534f" }}>
                    {" "}{prediction.prediction}
                </span>

            </h3>

            <h3>

                Confidence:
                <span style={{ color: "#198754" }}>
                    {" "}{prediction.confidence}%
                </span>

            </h3>

            <br />

            <h3>📊 Top Predictions</h3>

            <table
                style={{
                    width: "100%",
                    borderCollapse: "collapse",
                    marginTop: "10px"
                }}
            >

                <thead>

                    <tr style={{ background: "#0b5ed7", color: "white" }}>

                        <th style={{ padding: "10px" }}>Disease</th>

                        <th style={{ padding: "10px" }}>Confidence</th>

                    </tr>

                </thead>

                <tbody>

                    {prediction.top_predictions.map((item, index) => (

                        <tr key={index}>

                            <td
                                style={{
                                    padding: "10px",
                                    borderBottom: "1px solid #ddd"
                                }}
                            >
                                {item.disease}
                            </td>

                            <td
                                style={{
                                    padding: "10px",
                                    borderBottom: "1px solid #ddd"
                                }}
                            >
                                {item.confidence}%
                            </td>

                        </tr>

                    ))}

                </tbody>

            </table>

        </div>

    );

}

export default PredictionCard;