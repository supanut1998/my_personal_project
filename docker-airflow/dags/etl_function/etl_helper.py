import pandas as pd 
import requests
import json

# ingestion part

# get API
def fetch_data(url_data):
    data = requests.get(url_data)
    return data

# convert to json
def convert_data_to_json(request):
    return request.json()

# integrated function fetch_data and convert_data_to_json and write file
def ingest(url_data): 
    request = fetch_data(url_data)
    data_json = convert_data_to_json(request)
    
    # write file
    with open("data.json", "w") as outfile:
        json.dump(data_json, outfile)


# transformation part

# convert to dataframe
def convert_json_to_df(data_json):
    return pd.DataFrame(data_json)

# adjust column and set reset index
def adjust_columns(df):
    return df.reset_index().rename(columns={'index':'date'})

def transfrom(file_json): 
    
    #read file
    with open(file_json, 'r') as openfile:

        data_json = json.load(openfile)
    
    # convert to data frame
    df = convert_json_to_df(data_json)

    #adjust column
    df = adjust_columns(df)

    df.index += 1

    # write to csv
    df.to_csv("conversion_rate.csv", index=True)
