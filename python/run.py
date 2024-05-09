import pandas as pd
from elasticsearch import ES_connector

es = ES_connector()

# Index name and mapping file
index_name = 'country2'
mapping_file = 'mapping.json'

# Create index with mapping
with open(mapping_file, 'r') as mapping:
    index_mapping = mapping.read()
    # breakpoint()
    # es.create_index(index_name=index_name, index_mapping=index_mapping)

a = es.get_list_of_indexs()

for index in a:
    print(index)

# Read CSV file into a Pandas DataFrame
csv_file = 'country.csv'
df = pd.read_csv(csv_file)

# Convert DataFrame to a list of dictionaries (one dictionary per row)
data_list = df.to_dict(orient='records')

# Bulk index the data into Elasticsearch
for doc in data_list:
    es.insert_document(index_name=index_name, document=doc)

# print(f"CSV data imported to Elasticsearch index '{index_name}' successfully.")
