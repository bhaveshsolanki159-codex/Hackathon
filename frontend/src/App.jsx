import React, { useState } from "react";
import Auth from "./components/Auth.jsx";
import Chat from "./components/Chat.jsx";

export default function App() {
  const [user, setUser] = useState(null);

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-900 text-white">
      <h1 className="text-3xl font-bold mb-6">🔥 Soulence App</h1>
      {!user ? <Auth setUser={setUser} /> : <Chat user={user} />}
    </div>
  );
}
