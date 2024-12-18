import requests
import pandas as pd
import logging
import config as cfg
import google.cloud.logging
from google.cloud import storage
import json

storage_client = storage.Client()

bucket = storage_client.get_bucket(cfg.bucket)
blob = bucket.blob(cfg.creds)

key = blob.download_as_string()
api_key = json.loads(key)
api_key = api_key["46482b33cb294064a4975f93edae7b4f"]

logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', level=logging.INFO, datefmt='%I:%M:%S')

news_url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"

def make_request(url: str):

    logging.info("Making request to top-headlines end point...")
    
    response = requests.get(url)

    if response.status_code == 200:
        
        logging.info(f"Request status: {response.status_code}.")

        data = response.json()
        
        return data

    else:

        logging.info("No data returned.")
        
def format_df():
    
    news_data = make_request(news_url)
    
    df = pd.DataFrame()
    
    for a in news_data["articles"]:
        
        source = a["source"]
        author = a["author"]
        title = a["title"]
        url = a["url"]
        
        df = df.append({
            "source": source,
            "author": author,
            "title": title,
            "url": url
        }, ignore_index=True)
        
    logging.info("Creating data frame...")
        
    return df
    
def news_api(event, context):
    
    df = format_df()
    
    # Format string columns.
    
    for s in df[cfg.str_cols]:
        df[s] = df[s].str.title()

    # Log to see final output.
  
    logging.info(f"{df}")
    
if __name__ == "__main__":
    logging.info(f"Beginning pipeline run for {cfg.today}")
    news_api("", "")
