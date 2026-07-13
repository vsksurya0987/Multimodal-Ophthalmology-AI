import { useState } from "react";

import "./App.css";

import UploadSection from "./components/UploadSection";
import PredictionCard from "./components/PredictionCard";
import GradCAMViewer from "./components/GradCAMViewer";
import LifestyleCard from "./components/LifestyleCard";
import Chatbot from "./components/Chatbot";
import ReportButton from "./components/ReportButton";

import {
    predictDisease,
    generateGradCAM,
    downloadReport
} from "./api";

function App() {

    const [image, setImage] = useState(null);

    const [prediction, setPrediction] = useState(null);

    const [gradcam, setGradcam] = useState("");

    const [report, setReport] = useState("");

    const [loading, setLoading] = useState(false);

    const analyzeImage = async () => {

        if (!image) {

            alert("Please upload an eye image.");

            return;

        }

        try {

            setLoading(true);

            const predictionResult =
                await predictDisease(image);

            setPrediction(predictionResult);

            const gradcamResult =
                await generateGradCAM(image);

            setGradcam(gradcamResult);

            const reportResult =
                await downloadReport(image);

            setReport(reportResult);

        }

        catch (error) {

            console.error(error);

            alert("Backend connection failed.");

        }

        finally {

            setLoading(false);

        }

    };

    return (

        <div className="app">

            <h1>

                👁️ Multimodal Ophthalmology AI

            </h1>

            <UploadSection

                image={image}

                setImage={setImage}

                analyzeImage={analyzeImage}

                loading={loading}

            />

            {

                prediction &&

                <PredictionCard

                    prediction={prediction}

                />

            }

            {

                gradcam &&

                <GradCAMViewer

                    image={gradcam}

                />

            }

            {

                prediction &&

                <LifestyleCard

                    disease={prediction.prediction}

                />

            }

            <Chatbot />

            {

                report &&

                <ReportButton

                    report={report}

                />

            }

        </div>

    );

}

export default App;