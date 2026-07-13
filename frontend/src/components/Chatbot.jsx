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

            setAnswer(response.answer);

        }

        catch (error) {

            console.error(error);

            alert("Unable to connect to chatbot.");

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

                onChange={(e) =>
                    setQuestion(e.target.value)
                }

            />

            <br /><br />

            <button onClick={askAI}>

                {

                    loading

                        ? "Thinking..."

                        : "Ask AI"

                }

            </button>

            {

                answer &&

                <div className="answer">

                    <h3>Answer</h3>

                    <p style={{ whiteSpace: "pre-wrap" }}>

                        {answer}

                    </p>

                </div>

            }

        </div>

    );

}

export default Chatbot;