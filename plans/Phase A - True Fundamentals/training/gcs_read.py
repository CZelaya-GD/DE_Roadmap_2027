from google.cloud import storage
from io import BytesIO
import pandas as pd 

BUCKET_NAME = "data_engineer-2027-imo"  # Replace with your bucket name
BLOB_NAME = "sales.csv" 

def main():
#    # Create a client to interact with Google Cloud Storage
    client = storage.Client()

    # Get the bucket and blob
    bucket = client.bucket(BUCKET_NAME)
    blob = bucket.blob(BLOB_NAME)

    # Download the objects bytes into memory. 
    contents = blob.download_as_bytes()

    # Parse the bytes into a pandas DataFrame
    df = pd.read_csv(BytesIO(contents))

    print(df)
    print(f"\nTotal sales: {df['amount'].sum()}")

if __name__ == "__main__":
    main()