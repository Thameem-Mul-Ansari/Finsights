import React, { useState } from "react";
import axios from "axios";

export function Tables() {

  const [query, setQuery] = useState("");
  const [answer, setAnswer] = useState("");

  const handleSubmit = async () => {
    try {
      const response = await axios.post("http://localhost:5000/get_answer", {
        question: query,
      });
  
      setAnswer(response.data.answer);
    } catch (error) {
      console.error("Error fetching answer:", error.response?.data || error.message);
    }
  };
  

  return (
    <div className="mt-12 mb-8 flex flex-col items-center justify-center text-center">
      <h1 className="text-5xl font-extrabold mb-6">📈 PORTFOLIO GUIDE 🚀</h1>
      <div className="flex" style={{ marginTop: "20px" }}>
      <textarea
        placeholder="Enter your query"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        className="border p-3 rounded-md"
        style={{
          width: "500px",
          height: "300px",
          borderRadius: "30px",
          border: "2px solid black",
          boxSizing: "border-box",
          verticalAlign: "top",
        }}
      />
      <textarea
        placeholder="Answer will be displayed here"
        value={answer}
        readOnly
        className="border p-3 rounded-md"
        style={{
          width: "500px",
          height: "300px",
          borderRadius: "30px",
          border: "2px solid black",
          boxSizing: "border-box",
          verticalAlign: "top",
          marginLeft: "20px", // Add margin to create space
        }}
      />
      </div>
      <div className="mt-4" style={{ marginTop: "40px" }}>
        <button
          className="bg-blue-500 text-white px-4 py-2 rounded-md"
          onClick={handleSubmit}
        >
          PROVIDE YOUR OPINION
        </button>
      </div>
    </div>
  );
}

export default Tables;
