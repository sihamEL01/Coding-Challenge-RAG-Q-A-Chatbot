"use client";

import { useState } from "react";
import Sidebar from "../components/Sidebar";
import ChatMessage from "../components/ChatMessage";
import Suggestions from "../components/Suggestions";

export default function Home() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  const ask = async (question) => {
    const userMsg = { role: "user", text: question };
    setMessages((m) => [...m, userMsg]);

    const res = await fetch("http://localhost:8000/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question, top_k: 8 }),
    });

    const data = await res.json();

    const botMsg = {
      role: "assistant",
      text: data.answer,
      sources: data.sources,
    };

    setMessages((m) => [...m, botMsg]);
  };

  return (
    <div className="app">
      <Sidebar />

      <div className="main">
        <div className="header">
          <h1>Hello 👋</h1>
          <p>Ask questions about Treasure Island</p>
        </div>

        {messages.length === 0 && (
          <Suggestions onSelect={(q) => {
            setInput(q);
            ask(q);
          }} />
        )}

        <div className="chat">
          {messages.map((m, i) => (
            <ChatMessage
              key={i}
              role={m.role}
              text={m.text}
              sources={m.sources}
            />
          ))}
        </div>

        <div className="input-box">
          <textarea
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Ask something..."
          />
          <button
            onClick={() => {
              ask(input);
              setInput("");
            }}
          >
            Send
          </button>
        </div>
      </div>
    </div>
  );
}
