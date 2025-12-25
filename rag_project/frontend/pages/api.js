// pages/api.js
export async function askQuestion(question, topK = 8) {
  const response = await fetch("http://localhost:8000/ask", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      question,
      top_k: topK,
    }),
  });

  if (!response.ok) {
    throw new Error("Backend error");
  }

  return response.json();
}
