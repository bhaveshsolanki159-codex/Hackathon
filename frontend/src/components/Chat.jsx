import React, { useState } from "react";

export default function Chat({ user }) {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!input.trim()) return;

    // Add user message to chat
    const newMessage = { sender: user.name, text: input };
    setMessages([...messages, newMessage]);
    setInput("");
    setLoading(true);

    try {
      // Call Flask backend
      const response = await fetch("http://127.0.0.1:5000/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: newMessage.text }),
      });

      const data = await response.json();
      const aiMessage = { sender: "AI", text: data.reply };

      // Append AI reply
      setMessages((prev) => [...prev, aiMessage]);
    } catch (error) {
      console.error("Error:", error);
      setMessages((prev) => [
        ...prev,
        { sender: "System", text: "⚠️ Failed to reach server" },
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="w-full max-w-md bg-gray-800 p-4 rounded-lg shadow">
      <h2 className="text-xl mb-4">Welcome, {user.name}</h2>

      <div className="h-64 overflow-y-auto bg-gray-700 p-2 rounded mb-4">
        {messages.length === 0 && (
          <p className="text-gray-400">No messages yet...</p>
        )}
        {messages.map((m, i) => (
          <div key={i} className="mb-2">
            <span className="font-bold">{m.sender}: </span>
            <span>{m.text}</span>
          </div>
        ))}
        {loading && <p className="text-gray-400">AI is thinking...</p>}
      </div>

      <div className="flex">
        <input
          className="flex-grow p-2 rounded-l bg-gray-600 text-white"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type a message..."
        />
        <button
          onClick={sendMessage}
          className="bg-green-600 px-4 py-2 rounded-r hover:bg-green-700"
          disabled={loading}
        >
          Send
        </button>
      </div>
    </div>
  );
}
