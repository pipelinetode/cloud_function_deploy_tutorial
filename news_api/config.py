from datetime import datetime

today = datetime.now()

# INSERT API KEY HERE.

# api_key = ""

str_cols = ["author", "title"]

# If storing creds in GCP. 
# NOTE: The bucket name isn't available. You may call your file whatever you want.

bucket = "news_api_cred_store"

creds = "news_api_creds.json"
