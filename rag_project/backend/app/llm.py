# backend/app/llm.py
import requests
import logging

LLM_API_URL = "https://nonreigning-prettiest-shonta.ngrok-free.dev//generate"
def generate_answer(question: str, context: str) -> str:
    prompt = f"""
You are a factual question-answering system.

Rules you MUST follow:
- Use ONLY the information explicitly stated in the context.
- Do NOT use prior knowledge.
- Do NOT infer or guess.
- Do NOT add explanations, greetings, or extra words.
- Answer in ONE short factual sentence.
- Do NOT guess.
- Do NOT use outside knowledge.
- Quote character names exactly as written.
- If the answer is NOT explicitly stated in the context, reply exactly with:
I don't know.

Context:
{context}

Question:
{question}

Answer:
"""

    try:
        response = requests.post(
            LLM_API_URL,
            json={"prompt": prompt},  # must be "prompt"
            timeout=120
        )

        response.raise_for_status()
        return response.json().get("answer", "I don't know.")

    except requests.exceptions.RequestException as e:
        logging.error(f"LLM request failed: {e}")
        return "I don't know."
