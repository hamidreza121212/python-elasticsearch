import os
from kernel.settings.core.logs import configure_logging
from painless.utils.funcs import create_directories
from kernel.settings import config
import logging
from my_elasticsearch import ElasticConnector

coreLogger = logging.getLogger('core')

elasticsearchLogger = logging.getLogger('elasticsearch')


ELASTIC_HOST = config.get_value('elasticsearch', 'HOST')

es_connector = ElasticConnector(host=ELASTIC_HOST)


def main():
    base_dir_path = os.path.dirname(os.path.abspath(__file__))
    LOG_DIRECTORIES = config.get_value('log', 'LOG_DIRS')
    CONFIGS_LOG_DIRECTORIES = config.get_value('log', 'CONFIG_PATH')
    create_directories(base_dir=base_dir_path, directories=LOG_DIRECTORIES)
    configure_logging(CONFIGS_LOG_DIRECTORIES)

    coreLogger.warning("Invalid instance received in set_token_status signal")
    elasticsearchLogger.error('sdlkfldskfjldskjflkdjsflk')

    a = es_connector.get_list_of_indexs()

    # b = es.create_index('citys', )


if __name__ == "__main__":
    main()
