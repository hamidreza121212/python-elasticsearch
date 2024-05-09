import os
from kernel.settings.core.logs import configure_logging
from painless.utils.funcs import create_directories
from kernel.settings import config
import logging
from my_elasticsearch import ES_connector

coreLogger = logging.getLogger('core')

es = ES_connector()

def main():
    base_dir_path = os.path.dirname(os.path.abspath(__file__))
    LOG_DIRECTORIES = config.get_value('log', 'LOG_DIRS')
    CONFIGS_LOG_DIRECTORIES = config.get_value('log', 'CONFIG_PATH')
    create_directories(base_dir=base_dir_path, directories=LOG_DIRECTORIES)
    configure_logging(CONFIGS_LOG_DIRECTORIES)


    # coreLogger.warning("Invalid instance received in set_token_status signal")

    a = es.get_list_of_indexs()

    # b = es.create_index('citys', )


if __name__ == "__main__":
    main()