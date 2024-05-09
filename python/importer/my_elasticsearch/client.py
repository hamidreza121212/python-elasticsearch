
from elasticsearch import Elasticsearch


import logging

elasticsearchLogger = logging.getLogger('elasticsearch')


class ElasticConnector:
    def __init__(self, host, port=9200, username=None, password=None):
        self.host = host
        self.username = username
        self.password = password
        self._connect()

    def _connect(self):
        try:
            self.client = Elasticsearch(
                self.host,
                http_auth=(
                    self.username, self.password) if self.username and self.password else None
            )

        except ConnectionError as e:
            elasticsearchLogger.error(e)

    def search(self, index, body):
        return self.client.search(index=index, body=body)

    def create_index(self, index_name, body):
        try:
            self.client.indices.create(index=index_name, body=body)
        except Exception as e:
            elasticsearchLogger.error(f"create_index ERROR : {e}")

    def get_list_of_indexs(self):
        try:
            return self.client.indices.get_alias(index="*")
        except Exception as e:
            elasticsearchLogger.error(f"show_indexs ERROR : {e}")
            return None

    def insert_document(self, index_name, document):
        try:
            return self.client.index(index=index_name, body=document, refresh='wait_for', request_timeout=30)
        except Exception as e:
            elasticsearchLogger.error(f"insert_document ERROR : {e}")
