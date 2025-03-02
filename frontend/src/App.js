import React, { useState } from "react";
import axios from "axios";
import { marked } from "marked";
import "./App.css";

const App = () => {
  const [leetcodeUrl, setLeetcodeUrl] = useState("");
  const [question, setQuestion] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!leetcodeUrl || !question) {
      alert("Please enter both a LeetCode URL and your question.");
      return;
    }

    const newMessage = { role: "user", text: `📌 **LeetCode:** ${leetcodeUrl}\n❓ **${question}**` };
    setMessages([...messages, newMessage]);
    setLoading(true);

    try {
      const response = await axios.post("https://gpt-teaching-assistant.onrender.com/ask", {
        leetcode_url: leetcodeUrl,
        question: question,
      });

      const botMessage = { role: "bot", text: response.data.answer };
      setMessages([...messages, newMessage, botMessage]);
    } catch (error) {
      console.error("Error fetching response:", error);
      alert("Something went wrong. Try again!");
    }

    setLeetcodeUrl("");
    setQuestion("");
    setLoading(false);
  };

  return (
    <div className="app-container">
      <h1 className="title">DSA Chat Assistant 🤖</h1>

      <div className="chat-container">
        <div className="chat-box">
          {messages.length === 0 && <p className="empty-message">Start a conversation by asking a question! 🚀</p>}
          {messages.map((msg, index) => (
            <div key={index} className={`message ${msg.role === "user" ? "user-message" : "bot-message"}`}>
              <strong>{msg.role === "user" ? "You" : "Assistant"}:</strong>
              <p dangerouslySetInnerHTML={{ __html: marked.parse(msg.text) }} />
            </div>
          ))}
        </div>

        <form onSubmit={handleSubmit} className="chat-form">
          <input
            type="text"
            className="input-field"
            placeholder="Enter LeetCode URL..."
            value={leetcodeUrl}
            onChange={(e) => setLeetcodeUrl(e.target.value)}
          />
          <textarea
            className="input-field"
            placeholder="Enter your question..."
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
          />
          <button type="submit" className="submit-btn" disabled={loading}>
            {loading ? "Thinking..." : "Ask Question"}
          </button>
        </form>
      </div>
    </div>
  );
};

export default App;
