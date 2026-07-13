import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()


class ChatbotService:

    def __init__(self):

        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )

    def ask(self, question):

        response = self.client.chat.completions.create(

            model="llama-3.3-70b-versatile",

            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an expert ophthalmology assistant. "
                        "Explain eye diseases in simple English that anyone can understand."
                    )
                },
                {
                    "role": "user",
                    "content": f"""
User Question:
{question}

Answer using this format:

1. Explanation
2. Symptoms
3. Causes
4. Treatment
5. Prevention
6. Healthy Lifestyle Tips
7. When to Visit a Doctor

Keep the answer simple and practical.
"""
                }
            ],

            temperature=0.2,
            max_tokens=900

        )

        return response.choices[0].message.content


# ====================================================
# Create ONE chatbot instance
# ====================================================

chatbot = ChatbotService()