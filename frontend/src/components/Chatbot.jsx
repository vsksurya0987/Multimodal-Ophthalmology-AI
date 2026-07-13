import { useState } from "react";
import { askChatbot } from "../api";

function Chatbot() {

    const [question, setQuestion] = useState("");
    const [answer, setAnswer] = useState("");
    const [loading, setLoading] = useState(false);

    const askAI = async () => {

        if (!question.trim()) {
            alert("Please enter a question.");
            return;
        }

        try {

            setLoading(true);

            const response = await askChatbot(question);

            console.log("API Response:", response);

            setAnswer(response.answer);

        }
        catch (error) {

            console.error("========== CHATBOT ERROR ==========");
            console.error(error);

            if (error.response) {

                console.log("Status:", error.response.status);
                console.log("Response:", error.response.data);

                alert(
                    `Server Error (${error.response.status})\n\n` +
                    JSON.stringify(error.response.data, null, 2)
                );

            }
            else if (error.request) {

                console.log("No response received");
                console.log(error.request);

                alert(
                    "Unable to reach the backend.\n\n" +
                    "Please check if Render is running."
                );

            }
            else {

                console.log(error.message);

                alert(error.message);

            }

        }
        finally {

            setLoading(false);

        }

    };

    return (

        <div className="card">

            <h2>🤖 AI Medical Assistant</h2>

            <textarea
                rows="4"
                placeholder="Ask a medical question..."
                value={question}
                onChange={(e) => setQuestion(e.target.value)}
            />

            <br /><br />

            <button
                onClick={askAI}
                disabled={loading}
            >
                {loading ? "Thinking..." : "Ask AI"}
            </button>

            {answer && (

                <div className="answer">

                    <h3>Answer</h3>

                    <p
                        style={{
                            whiteSpace: "pre-wrap"
                        }}
                    >
                        {answer}
                    </p>

                </div>

            )}

        </div>

    );

}

export default Chatbot;