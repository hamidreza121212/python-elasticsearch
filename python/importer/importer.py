import os
import json
from kernel.settings.core.logs import configure_logging
from painless.utils.funcs import create_directories
from kernel.settings import config
import logging
from my_elasticsearch import ElasticConnector

coreLogger = logging.getLogger('core')


ELASTIC_HOST = config.get_value('elasticsearch', 'HOST')

es_connector = ElasticConnector(host=ELASTIC_HOST)


def main():
    base_dir_path = os.path.dirname(os.path.abspath(__file__))
    LOG_DIRECTORIES = config.get_value('log', 'LOG_DIRS')
    CONFIGS_LOG_DIRECTORIES = config.get_value('log', 'CONFIG_PATH')
    create_directories(base_dir=base_dir_path, directories=LOG_DIRECTORIES)
    configure_logging(CONFIGS_LOG_DIRECTORIES)

    # coreLogger.warning("Invalid instance received in set_token_status signal")

    # with open('C:/Users/Admin/Desktop/PROJECT/python_elasticsearch/python/importer/data/file_sources/mapping.json', 'r') as file:
    #     mapping = json.load(file)

    # a = es_connector.create_index('country', body=mapping)

    with open('C:/Users/Admin/Desktop/PROJECT/python_elasticsearch/python/importer/data/file_sources/country.csv', 'r') as file:
        next(file)
        for line in file:
            fields = line.strip().split(',')
            doc_id = fields[0]
            document = {f'field_{idx}': value for idx,
                        value in enumerate(fields[1:], start=1)}
            es_connector.insert_document(
                index_name='country', document=document)


if __name__ == "__main__":
    main()
