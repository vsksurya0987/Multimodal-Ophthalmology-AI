import os

from dotenv import load_dotenv
from groq import Groq

from backend.services.rag_service import RAGService


load_dotenv()


class ChatbotService:

    def __init__(self):

        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )

        self.rag = RAGService()

    def ask(self, question):

        # Retrieve relevant chunks
        results = self.rag.search(question)

        context = "\n\n".join(
            chunk["content"]
            for chunk in results
        )

        prompt = f"""
You are an AI Ophthalmology Assistant.

Use ONLY the medical context below.

If the answer is not available in the context,
politely say that you do not know.

Medical Context:
{context}

User Question:
{question}

Answer in simple English that even a 6th class student can understand.

Always follow this format:

1. Explanation
- Explain the disease or problem in simple words.

2. Symptoms
- Mention the common symptoms.

3. Causes
- Explain why this problem happens.

4. Treatment
- Explain the available treatments.
- Recommend consulting an ophthalmologist.

5. Prevention
- Explain how to protect the eyes.

6. Healthy Lifestyle Tips
Mention:
• Eat green leafy vegetables.
• Eat carrots, fish and fruits rich in Vitamin C.
• Drink enough water every day.
• Sleep 7-8 hours daily.
• Exercise regularly.
• Wear UV-protective sunglasses outdoors.
• Follow the 20-20-20 rule during screen usage.
• Avoid smoking and alcohol.
• Reduce continuous mobile and laptop usage.

7. Ask These Questions
If appropriate, ask the user:
• Do you have headaches?
• Is your vision blurry?
• Is it difficult to see nearby objects?
• Is it difficult to see distant objects?
• Do your eyes become red or itchy?
• Do your eyes water frequently?
• Do you wear spectacles?
• How many hours do you use a mobile phone or laptop daily?
• Do you play games or watch movies continuously for long hours?
• Do you work in dusty environments?
• When did these symptoms begin?

Explain briefly why these questions are important.

8. When to Visit a Doctor
Advise the user to visit an ophthalmologist immediately if they experience:
• Sudden vision loss.
• Severe eye pain.
• Flashing lights.
• Persistent redness.
• Sudden increase in blurry vision.

Use friendly, practical and easy-to-understand language.
"""

        response = self.client.chat.completions.create(

            model="llama-3.3-70b-versatile",

            messages=[
                {
                    "role": "system",
                    "content": "You are an expert ophthalmology assistant."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.2,

            max_tokens=900

        )

        return response.choices[0].message.content


# ====================================================
# Create ONE chatbot instance for the whole application
# ====================================================

chatbot = ChatbotService()