from sentence_transformers import SentenceTransformer
import faiss
import pandas as pd
import numpy as np

df = pd.read_csv('data/processed_data.csv')
model = SentenceTransformer('all-MiniLM-L6-v2')

texts = df['hotel'].astype(str) + " " + df['arrival_date_year'].astype(str) + " " + df['arrival_date_month'].astype(str) + " " + df['arrival_date_day_of_month'].astype(str) + " " + df['stays_in_week_nights'].astype(str) + " " + df['country'].astype(str) + " " + df['adr'].astype(str) + " " + df['reservation_status'].astype(str)
embeddings = model.encode(texts.tolist(), convert_to_numpy=True)

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

def search(query, k=5):
    query_embedding = model.encode([query])
    distances, indices = index.search(query_embedding, k)
    return df.iloc[indices[0]]

def update_embeddings():
    from database import fetch_bookings
    global index
    df = fetch_bookings()

    if df.empty:
        return
    texts = df.apply(lambda row: f"Booking at {row['hotel']} from {row['arrival_date_year']}{row['arrival_date_month']}{row['arrival_date_day_of_month']}. Location: {row['country']}. Price: ${row['adr']}. Status: {'Cancelled' if row['reservation_status'] else 'Confirmed'}", axis=1)

    embeddings = model.encode(texts.tolist(), convert_to_numpy=True)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)


if __name__ == "__main__":
    print(search("Show me all bookings in July 2017"))
    update_embeddings()