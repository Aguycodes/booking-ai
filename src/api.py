from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from analytics import revenue_trends, cancellation_rate, geographical_distribution , booking_lead_time_distribution
from rag import search
from database import add_booking, log_query, fetch_query_history
import uvicorn

app = FastAPI()

class QueryModel(BaseModel):
    question: str

@app.post("/analytics")
def get_analytics():
    df = pd.read_csv("data/processed_data.csv")
    return {
        "revenue_trends": revenue_trends(df),
        "cancellation_rate": cancellation_rate(df),
        "geographical_distribution": geographical_distribution(df),
        "booking_lead_time_distribution": booking_lead_time_distribution(df)
    }

@app.post("/ask")
def ask_questions(query: QueryModel):
    retrieved_data = search_faiss(query.question, index, text_data)
    answer = generate_answer(query.question, retrieved_data)

    log_query(query.question, answer)

    return {"result": answer}

@app.post("/add_booking")
def insert_booking(hotel: str, arrival_date_year: int, arrival_date_month: int, arrival_date_day_of_month: int, country: str, adr: float, reservation_status: int):
    add_booking(hotel, arrival_date_year, arrival_date_month, arrival_date_day_of_month, country, adr, reservation_status)
    return {"message": "Booking added successfully"}

@app.get("/query_history")
def get_query_history():
    return fetch_query_history().to_dict(orient="records")

@app.get("/health")
def system_health():
    health_status = {
        "database": "OK" if fetch_bookings() is not None else "FAIL",
        "vector_db": "OK"  if index is not None else "FAIL",
        "llm": "OK" if model is not None else "FAIL"
    }
    return health_status

if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)