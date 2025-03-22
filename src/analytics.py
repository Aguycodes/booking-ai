import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def revenue_trends(df):
    df['arrival_date'] = pd.to_datetime(df['reservation_status_date'])
    revenue_by_month = df.groupby(df['arrival_date'].dt.to_period("M"))['adr'].sum()

    plt.figure(figsize=(10, 5))
    revenue_by_month.plot(kind='line', marker='o', color='b')
    plt.title("Revenue Trends Over Time")
    plt.xlabel("Month")
    plt.ylabel("Total Revenue")
    plt.show()

def cancellation_rate(df):
    rate = (df['is_canceled'].sum() / len(df)) * 100
    print(f"Cancellation Rate: {rate: .2f}%")

def geographical_distribution(df):
    country_counts = df['country'].value_counts()

    plt.figure(figsize=(12, 6))
    sns.barplot(x=country_counts.index[:10], y=country_counts.values[:10], palette='viridis')
    plt.xticks(rotation=45)
    plt.xlabel("Country")
    plt.ylabel("Number of bookings")
    plt.title("Top 10 Booking Locations")
    plt.show()

    return country_counts.to_dict()

def booking_lead_time_distribution(df):
    df['lead_time'] = df['lead_time'].astype(int)

    plt.figure(figsize=(10, 5))
    sns.histplot(df['lead_time'], bins=30, kde=True, color='blue')
    plt.xlabel("Booking Lead Time (days)")
    plt.ylabel("Number of Bookings")
    plt.title("Distribution of Booking Lead Time")
    plt.show()

    return df['lead_time'].describe().to_dict()

if __name__ == "__main__":
    df = pd.read_csv("data/processed_data.csv")
    revenue_trends(df)
    cancellation_rate(df)
    print(geographical_distribution(df))
    print(booking_lead_time_distribution(df))