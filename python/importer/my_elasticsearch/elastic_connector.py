
from elasticsearch import Elasticsearch


class ES_connector:
    def __init__(self) -> None:
        self.es_client = None
        self.connect()

    def connect(self):
        try:
            client  = Elasticsearch("http://localhost:9200")
            self.es_client = client
        except Exception as e:
            print(e)


    def  create_index(self, index_name, index_mapping):
        try:
            self.es_client.indices.create(index=index_name)
        except Exception as e:
            print(f"create_index ERROR : {e}")

    
    def  get_list_of_indexs(self):
        try:
            return self.es_client.indices.get_alias(index="*")
        except Exception as e:
            print(f"show_indexs ERROR : {e}")
            return None


    def insert_document(self, index_name, document):
        try:
            return self.es_client.index(index=index_name, body=document, refresh='wait_for', request_timeout=30)
        except Exception as e:
            print(e)