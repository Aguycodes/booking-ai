LLM-Powered Booking Analytics & QA System

This project is an AI-powered hotel booking analytics system that:
Processes hotel booking data and provides insights.
Enables Q&A using an LLM with Retrieval-Augmented Generation (RAG).
Supports real-time updates, query history tracking, and a health check API.


Features
✔ Hotel Booking Analytics (Revenue trends, cancellations, lead time, etc.)
✔ RAG-based Q&A (Asks booking-related questions using an LLM)
✔ Real-time Database Updates (New bookings update FAISS embeddings)
✔ Query History Tracking (Stores user queries & answers)
✔ System Health Check API (Monitors database, FAISS, and LLM status)

Installation & Setup

1. Clone the Repository

git clone https://github.com/your-username/booking_ai.git
cd booking_ai

2. Create a Virtual Environment & Install Dependencies

python -m venv venv
source venv/bin/activate # On Windows use: venv\Scripts\activate

pip install -r requirements.txt

3. Start the API

uvicorn src.api:app --reload

The API will now be available at http://127.0.0.1:8000.


API Endpoints:
Example API Calls

1️. Get Analytics

curl -X POST http://127.0.0.1:8000/analytics

2️. Ask a Question

curl -X POST http://127.0.0.1:8000/ask -H "Content-Type: application/json" -d '{"question": "Which hotel had the highest revenue?"}'

3️. Add a Booking

curl -X POST "http://127.0.0.1:8000/add_booking" -H "Content-Type: application/json" \
    -d '{"hotel": "Resort Hotel", "arrival_date": "2025-06-10", "country": "USA", "adr": 150.00, "is_canceled": 0}'

4️. Get Query History

curl -X GET http://127.0.0.1:8000/query_history

5️. Check System Health

curl -X GET http://127.0.0.1:8000/health


