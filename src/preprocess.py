import pandas as pd

def preprocess_data(filepath):
    df = pd.read_csv(filepath)

    df.fillna(0, inplace=True)

    #convert dates to datetime format
    df['reservation_status_date'] = pd.to_datetime(df['reservation_status_date'])

    #save processed data
    df.to_csv('data/processed_data.csv', index=False)
    return df

if __name__ == "__main__":
    preprocess_data("data\hotel_bookings.csv")