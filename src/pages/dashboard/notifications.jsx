import React, { useState } from "react";
import DatePicker from "react-datepicker";
import { format } from "date-fns";  // Import the format function
import "react-datepicker/dist/react-datepicker.css";
import "./notifications.css"; 

export function Notifications() {
  const [startDate, setStartDate] = useState(null);
  const [endDate, setEndDate] = useState(null);
  const [showDates, setShowDates] = useState(false); // New state to control visibility of dates

  const currentDate = new Date();

  const formatDate = (date) => (date ? format(date, "yyyy,M,d") : "");

  const performTrade = async () => {
    // Perform the trade using the selected dates (startDate and endDate)
    const formattedStartDate = formatDate(startDate);
    const formattedEndDate = formatDate(endDate);

    // Use fetch or any other method to send the dates to your backend
    const response = await fetch('/api/performTrade', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        start_date: formattedStartDate,
        end_date: formattedEndDate,
      }),
    });

    // Handle the response as needed
    const result = await response.json();
    console.log(result);
  };

  return (
    <div className="mt-12 mb-8 flex flex-col items-center justify-center text-center">
      <h1 className="text-5xl font-extrabold mb-6">📈 ML Trader 🚀</h1>
      <div className="flex" style={{ marginTop: "20px" }}></div>
      <div className="flex">
        <div className="mr-4">
          <DatePicker
            selected={startDate}
            onChange={(date) => setStartDate(date)}
            selectsStart
            startDate={startDate}
            endDate={endDate}
            inline
            className="custom-datepicker"
            maxDate={currentDate}
          />
          <h2 className="text-3xl font-bold mb-4">📆 Start Date 📆</h2>
        </div>
        <div style={{ marginLeft: '250px' }}>
          <DatePicker
            selected={endDate}
            onChange={(date) => setEndDate(date)}
            selectsEnd
            startDate={startDate}
            endDate={endDate}
            minDate={startDate}
            inline
            className="custom-datepicker"
            maxDate={currentDate}
          />
          <h2 className="text-3xl font-bold mb-4">📆 End Date 📆</h2>
        </div>
      </div>
      <button
        className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mt-4"
        onClick={() => setShowDates(true)}
      >
        💵 Perform Trade 📈
      </button>

      {showDates && (
        <div className="mt-4">
          <p>Selected Start Date: {formatDate(startDate)}</p>
          <p>Selected End Date: {formatDate(endDate)}</p>
        </div>
      )}
    </div>
  );
}

export default Notifications;
