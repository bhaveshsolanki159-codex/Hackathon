import React from "react";

export default function Auth({ setUser }) {
  const handleLogin = () => {
    // Fake login for now
    setUser({ name: "Demo User" });
  };

  return (
    <div className="flex flex-col items-center">
      <p className="mb-4">Please log in</p>
      <button
        onClick={handleLogin}
        className="bg-blue-600 px-4 py-2 rounded hover:bg-blue-700"
      >
        Login with Demo
      </button>
    </div>
  );
}
