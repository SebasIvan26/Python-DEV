# Imports necessary libraries
import requests
import pandas as pd
import io

username = 'INSERT_YOUR_WORKDAY_ID' # 10 digit ID
password = 'INSERT_YOUR_WORKDAY_PASSWORD'

url = 'INSERT_THE_COPIED_CSV_URL' # This URL will send Python to your web services enabled report in Workday

with requests.Session() as s:
    download = s.get(url, auth = (username, password))
    decoded_content = download.content.decode('utf-8')
    
    df = pd.read_csv(io.StringIO(decoded_content))